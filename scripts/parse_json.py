#!/usr/bin/env python3
"""
知乎热榜JSON数据解析脚本
将用户提供的JSON数据解析为标准格式
"""

import json
import sys


SUPPORTED_CATEGORIES = [
    "经济", "社会", "AI", "科技", "资源和工具"
]


def parse_zhihu_json(input_file, category=None):
    """
    解析知乎热榜JSON数据

    Args:
        input_file: 输入JSON文件路径
        category: 筛选分类（可选）

    Returns:
        dict: 解析后的标准格式数据
    """
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    hot_list = data.get("hot_list", [])

    if category:
        hot_list = [item for item in hot_list if item.get("category") == category]

    return {"hot_list": hot_list[:10]}


def format_output(data, answer_count=3):
    """
    格式化输出热门话题数据

    Args:
        data: 解析后的数据
        answer_count: 每个话题显示的回答数

    Returns:
        str: 格式化后的字符串
    """
    output = []
    hot_list = data.get("hot_list", [])

    for i, topic in enumerate(hot_list, 1):
        title = topic.get("title", "无标题")
        cat = topic.get("category", "未分类")
        ans_count = topic.get("answer_count", 0)

        output.append(f"\n{i}. {title}")
        output.append(f"   分类: {cat} | 回答数: {ans_count}")

        answers = topic.get("answers", [])[:answer_count]
        for j, ans in enumerate(answers, 1):
            author = ans.get("author", "匿名")
            upvotes = ans.get("upvote_count", 0)
            content = ans.get("content", "")[:100]
            url = ans.get("url", "")

            output.append(f"   回答{j}: {author} (赞: {upvotes})")
            output.append(f"   {content}...")
            if url:
                output.append(f"   链接: {url}")

        output.append("")

    return "\n".join(output)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python parse_json.py <input_json> [category] [answer_count]")
        print("示例: python parse_json.py zhihu_hot.json AI 3")
        sys.exit(1)

    input_file = sys.argv[1]
    category = sys.argv[2] if len(sys.argv) > 2 else None
    answer_count = int(sys.argv[3]) if len(sys.argv) > 3 else 3

    try:
        data = parse_zhihu_json(input_file, category)
        output = format_output(data, answer_count)
        print(output)
    except Exception as e:
        print(f"解析失败: {e}")