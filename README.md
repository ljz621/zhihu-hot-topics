# 知乎热门话题 (Zhihu Hot Topics)

获取知乎网站每天的热门话题及其高赞回答，支持按分类筛选。

## 功能特点

- 获取知乎热榜前10条热门话题
- 获取每个话题下点赞最多的前3个回答
- 支持按分类筛选（经济、社会、AI、科技、资源和工具）
- 支持用户自定义分类
- 不提供自动抓取，专注数据解析和展示

## 使用前提

由于知乎API需要用户自己申请，本Skill**不提供自动抓取功能**，只负责：
- 解析用户提供的JSON数据
- 按分类筛选
- 格式化展示

用户需要通过以下方式获取知乎数据：
1. 使用知乎官方API（需要申请API Key）
2. 使用第三方合法工具
3. 手动粘贴JSON数据

## 使用方法

### 1. 准备JSON数据

确保数据格式如下：

```json
{
  "hot_list": [
    {
      "id": "123456",
      "title": "话题标题",
      "category": "AI",
      "answer_count": 100,
      "url": "话题链接",
      "answers": [
        {
          "id": "answer_1",
          "author": "作者名",
          "content": "回答内容",
          "upvote_count": 500,
          "url": "回答链接"
        }
      ]
    }
  ]
}
```

### 2. 运行解析脚本

```bash
cd scripts
python parse_json.py ../zhihu_hot.json AI 3
```

参数说明：
- `zhihu_hot.json` - 输入的JSON数据文件
- `AI` - 可选，筛选的分类
- `3` - 可选，每个话题显示的回答数，默认3

### 3. 支持的分类

- 经济
- 社会
- AI
- 科技
- 资源和工具
- 用户自定义（直接输入分类名称）

## 目录结构

```
zhihu-hot-topics/
├── SKILL.md                    # Skill定义文件
├── README.md                   # 说明文档
├── scripts/
│   ├── zhihu_api_example.py   # API调用示例
│   └── parse_json.py         # JSON解析脚本
├── references/               # 参考文档（暂无）
└── assets/                   # 静态资源（暂无）
```

## 注意事项

- 本项目不提供任何违法爬取功能
- 使用知乎API需要遵守知乎开发者协议
- 请勿将本项目用于商业用途
- 数据版权归属知乎及回答作者

## 开源协议

MIT License

## 贡献指南

欢迎提交Issue和Pull Request！