# 006 - 图片灯箱（Lightbox）查看

| 字段 | 值 |
|---|---|
| 编号 | 006 |
| 状态 | 🔴 未开始 |
| 优先级 | 🥈 P1（体验提升明显） |
| 类型 | 改进 |
| 涉及端 | 纯前端 |

## 背景与痛点

当前点击图片只是简单 `scale(2)` 放大（`setupImageHandlers`），体验粗糙：会溢出容器、无法拖动平移、无法在多图间切换。

## 功能描述

将图片点击放大升级为全屏灯箱，支持缩放、平移、翻图、键盘操作。

## 实现方案

- 新增灯箱浮层（fixed 全屏 + 半透明遮罩）
- 点击文档内图片 → 打开灯箱显示该图
- 功能：
  - 滚轮 / 按钮 缩放
  - 拖拽平移
  - 左右键 / 箭头 在当前文档的所有图片间切换
  - ESC / 点击遮罩 关闭
  - 双击复位缩放
- 替换现有 `setupImageHandlers` 中的 `scale(2)` 逻辑

## 涉及文件

- `src/static/app.js` — 灯箱组件、手势与键盘绑定（替换 `setupImageHandlers` 的 onclick）
- `src/static/app.css` — 灯箱与遮罩样式
- `src/translations.py` — 若有按钮 tooltip

## 验收标准

- [ ] 点击图片打开全屏灯箱
- [ ] 支持缩放、平移
- [ ] 支持左右翻看当前文档其他图片
- [ ] ESC / 点遮罩可关闭
- [ ] 原有图片加载错误的提示（onerror 红框）仍保留

## 备注

可考虑引入轻量库（如 GLightbox / Lity）或纯手写；手写更可控且无新 CDN 依赖（契合项目「CDN 是性能瓶颈」的现状，见 memory `perf-frontend-cdn-bottleneck`）。
