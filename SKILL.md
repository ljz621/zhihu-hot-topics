---
name: zhihu-hot-topics
description: 获取知乎每日热榜Top10热门话题及高赞回答，支持按分类筛选。触发条件：用户询问知乎热门话题、知乎热榜、知乎排行榜、知乎热点等。
---

# 知乎热门话题 (Zhihu Hot Topics)

获取知乎网站每天的Top10热门话题及其高赞回答，支持按分类筛选。

## 使用方式

### 直接运行获取脚本

```bash
cd D:/SkillsStudy/.opencode/skills/zhihu-hot-topics/scripts
python get_hot.py
```

脚本会自动获取知乎热榜Top10话题，并保存为JSON文件。

### 可选参数

- 指定分类：`python get_hot.py ai`（获取AI分类）
- 自定义分类：`python get_hot.py 你的分类名`

### 输出展示

运行后会直接显示格式化的话题列表，包含：
- 话题排名和标题
- 分类标签
- 前3个高赞回答（作者、点赞数、回答链接）

## 支持的分类

默认分类：经济、社会、AI、科技、资源和工具

## 文件说明

```
scripts/
├── get_hot.py      # 主脚本，自动获取知乎热榜数据
├── example.json   # 示例数据文件（可直接查看格式）
└── format.py     # 格式化输出脚本
```

## 注意事项

- 本技能不提供自动抓取知乎数据的功能，使用前请确保网络可以访问知乎
- 如果自动获取失败，会使用example.json中的示例数据
- 数据版权归属知乎及回答作者