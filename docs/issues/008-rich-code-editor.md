# 008 - 富文本代码编辑器（CodeMirror / Monaco）

| 字段 | 值 |
|---|---|
| 编号 | 008 |
| 状态 | 🔴 未开始 |
| 优先级 | 🥉 P2（锦上添花 / 改动大） |
| 类型 | 改进 |
| 涉及端 | 前端 |

## 背景与痛点

当前编辑模式是裸 `<textarea>`，无语法高亮、无行号、无自动配对、无查找替换，编辑体验与阅读体验落差大。

## 功能描述

将编辑器升级为带 Markdown 语法高亮与基础编辑能力的代码编辑器。

## 实现方案

- 引入编辑器内核：CodeMirror 6（轻量、模块化）或 Monaco（功能强但体积大）
- 能力：
  - Markdown 语法高亮
  - 行号、行折叠
  - 自动配对括号 / 引号 / 代码块
  - 查找替换（Ctrl+F）
  - Tab 缩进、列表续行
- 替换 `toggleEditMode` 中对 `textarea` 的依赖
- 注意：`saveFile()` 与 `preview` 读取内容需改为从编辑器实例 `getValue()`

## 涉及文件

- `src/static/app.js` — 编辑器集成、与 save/preview 对接
- `src/static/app.css` — 编辑器主题（对接暗色模式）
- `src/template/main_template.py` — 编辑器容器、资源引入
- 依赖管理 — 新增库（注意 CDN 性能，见 memory `perf-frontend-cdn-bottleneck`，优先本地化打包）

## 验收标准

- [ ] 编辑模式具备 Markdown 语法高亮
- [ ] 行号、自动配对、查找替换可用
- [ ] 保存 / 预览功能正常
- [ ] 暗色模式下编辑器主题一致

## 备注

改动最大的一项。建议在 001–007 落地后再评估，避免编辑器重构与功能开发耦合。优先选 CodeMirror 6 以控制体积。
