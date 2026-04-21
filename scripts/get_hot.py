#!/usr/bin/env python3
"""
知乎热榜获取脚本 - 自动获取Top10热门话题
用法: python get_hot.py [category]
"""

import json
import os
import sys
import requests
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)

CATEGORIES = ["经济", "社会", "AI", "科技", "资源和工具"]

def get_zhihu_hot(category=None):
    """获取知乎热榜数据"""

    url = "https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json",
    }

    params = {"limit": 10, "desktop": "true"}
    if category:
        params["category"] = category

    try:
        resp = requests.get(url, headers=headers, params=params, timeout=10)
        data = resp.json()

        items = data.get("data", [])
        hot_list = []

        for i, item in enumerate(items[:10], 1):
            target = item.get("target", {})

            answers = []
            if "answer" in target:
                ans = target["answer"]
                answers.append({
                    "id": ans.get("id", ""),
                    "author": ans.get("author", {}).get("name", "匿名"),
                    "upvote_count": ans.get("voteup_count", 0),
                    "url": f"https://www.zhihu.com/answer/{ans.get('id', '')}"
                })

            hot_list.append({
                "rank": i,
                "id": target.get("id", ""),
                "title": target.get("title", ""),
                "category": target.get("category", {}).get("name", "综合"),
                "answer_count": target.get("answer_count", 0),
                "url": f"https://www.zhihu.com/topic/{target.get('id', '')}",
                "answers": answers
            })

        return {"hot_list": hot_list, "update_time": datetime.now().isoformat()}

    except Exception as e:
        print(f"获取失败: {e}, 使用示例数据")
        return get_example_data()


def get_example_data():
    """获取示例数据"""
    example_file = os.path.join(SCRIPT_DIR, "example.json")
    if os.path.exists(example_file):
        with open(example_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"hot_list": [], "update_time": datetime.now().isoformat()}


def save_and_print(data, answer_count=3):
    """保存并格式化输出"""
    output_file = os.path.join(BASE_DIR, "zhihu_hot.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("\n" + "="*60)
    print("知乎热榜 Top 10")
    print("="*60)

    for topic in data.get("hot_list", []):
        print(f"\n【{topic.get('rank', '?')}】{topic.get('title', '无标题')}")
        print(f"   分类: {topic.get('category', '未分类')} | 回答: {topic.get('answer_count', 0)}")

        answers = topic.get("answers", [])[:answer_count]
        for ans in answers:
            print(f"   - {ans.get('author', '匿名')}: 赞 {ans.get('upvote_count', 0)}")
            if ans.get("url"):
                print(f"     {ans.get('url', '')}")

    print("\n" + "="*60)
    print(f"数据已保存到: {output_file}")
    print(f"更新时间: {data.get('update_time', '')}")
    print("="*60)


if __name__ == "__main__":
    category = sys.argv[1] if len(sys.argv) > 1 else None

    print(f"正在获取知乎热榜{' - '+category if category else ''}...")

    data = get_zhihu_hot(category)
    save_and_print(data)

    if not data.get("hot_list"):
        print("\n获取数据为空，将下载示例数据...")
        data = get_example_data()
        save_and_print(data)