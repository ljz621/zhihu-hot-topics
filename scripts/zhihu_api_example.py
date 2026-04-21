#!/usr/bin/env python3
"""
知乎API调用示例脚本
用户需要自己配置API密钥
"""

import json
import requests

def get_zhihu_hot_list(api_key=None, category=None):
    """
    获取知乎热榜数据

    Args:
        api_key: 知乎API密钥（用户自己提供）
        category: 筛选分类（可选）

    Returns:
        dict: 热榜数据JSON
    """
    if not api_key:
        print("请提供知乎API密钥")
        return None

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    url = "https://api.zhihu.com/hot/list"

    params = {}
    if category:
        params["category"] = category

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        hot_list = []
        for item in data.get("data", [])[:10]:
            topic = {
                "id": item.get("id", ""),
                "title": item.get("title", ""),
                "category": item.get("category", ""),
                "answer_count": item.get("answer_count", 0),
                "url": item.get("url", ""),
                "answers": []
            }

            answer_url = item.get("answers_url", "")
            if answer_url:
                ans_response = requests.get(answer_url, headers=headers, timeout=10)
                ans_data = ans_response.json()

                answers = ans_data.get("data", [])[:3]
                for ans in answers:
                    topic["answers"].append({
                        "id": ans.get("id", ""),
                        "author": ans.get("author", {}).get("name", ""),
                        "content": ans.get("content", "")[:200],
                        "upvote_count": ans.get("upvote_count", 0),
                        "url": ans.get("url", "")
                    })

            hot_list.append(topic)

        return {"hot_list": hot_list}

    except requests.RequestException as e:
        print(f"请求失败: {e}")
        return None


def save_to_json(data, filename="zhihu_hot.json"):
    """保存数据到JSON文件"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"数据已保存到 {filename}")


if __name__ == "__main__":
    import sys

    api_key = sys.argv[1] if len(sys.argv) > 1 else None
    category = sys.argv[2] if len(sys.argv) > 2 else None

    if not api_key:
        print("用法: python zhihu_api_example.py <api_key> [category]")
        print("示例: python zhihu_api_example.py your_api_key_here AI")
        sys.exit(1)

    data = get_zhihu_hot_list(api_key, category)
    if data:
        save_to_json(data)
        print(f"成功获取 {len(data['hot_list'])} 条热门话题")