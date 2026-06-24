# Markdown Reader 需求跟踪总览

> 本目录记录 Markdown Reader 的新功能与改进需求。每个需求一个 `.md` 文件，本文件为总览与状态跟踪。

## 状态图例

| 图例 | 含义 |
|---|---|
| 🔴 未开始 | 尚未开工 |
| 🟡 进行中 | 正在开发 |
| 🟢 已完成 | 已实现并验收 |
| ⚪ 暂缓 | 暂不推进（可选） |
| ❌ 取消 | 决定不做 |

## 优先级图例

- 🥇 **P0**：高价值 / 低成本，优先推进
- 🥈 **P1**：体验提升明显
- 🥉 **P2**：锦上添花 / 架构演进

---

## 需求清单

### 🥇 第一梯队 — 高频刚需

| 编号 | 需求 | 优先级 | 状态 | 文件 |
|---|---|---|---|---|
| 001 | 全文搜索（跨文件搜索） | 🥇 P0 | 🔴 未开始 | [001-full-text-search.md](001-full-text-search.md) |
| 002 | 文档大纲（TOC 侧边面板） | 🥇 P0 | 🟢 已完成 | [002-document-outline-toc.md](002-document-outline-toc.md) |
| 003 | 阅读位置记忆 + 阅读进度 | 🥇 P0 | 🔴 未开始 | [003-reading-position-memory.md](003-reading-position-memory.md) |

### 🥈 第二梯队 — 体验提升

| 编号 | 需求 | 优先级 | 状态 | 文件 |
|---|---|---|---|---|
| 004 | 文件收藏 / 书签 | 🥈 P1 | 🔴 未开始 | [004-file-bookmarks.md](004-file-bookmarks.md) |
| 005 | 最近打开（Recent） | 🥈 P1 | 🔴 未开始 | [005-recent-files.md](005-recent-files.md) |
| 006 | 图片灯箱（Lightbox）查看 | 🥈 P1 | 🔴 未开始 | [006-image-lightbox.md](006-image-lightbox.md) |
| 007 | 导出 PDF / 打印优化 | 🥈 P1 | 🔴 未开始 | [007-export-pdf-print.md](007-export-pdf-print.md) |

### 🥉 第三梯队 — 锦上添花 / 架构演进

| 编号 | 需求 | 优先级 | 状态 | 文件 |
|---|---|---|---|---|
| 008 | 富文本代码编辑器（CodeMirror/Monaco） | 🥉 P2 | 🔴 未开始 | [008-rich-code-editor.md](008-rich-code-editor.md) |
| 009 | 文档元信息 / 阅读统计 | 🥉 P2 | 🔴 未开始 | [009-document-metadata-stats.md](009-document-metadata-stats.md) |
| 010 | 高级搜索（正则/大小写/历史） | 🥉 P2 | 🔴 未开始 | [010-advanced-search.md](010-advanced-search.md) |
| 011 | 安全演进：多用户 / 密码环境变量化 | 🥉 P2 | 🔴 未开始 | [011-security-multi-user-env-password.md](011-security-multi-user-env-password.md) |

---

## 维护说明

- 开工时：将对应行的状态改为 🟡 进行中
- 完成并验收后：改为 🟢 已完成，勾选该需求文件中的验收标准
- 暂缓 / 取消：改为 ⚪ / ❌ 并在文件中说明原因
- 新增需求：使用下一个递增编号，并在本表追加一行
