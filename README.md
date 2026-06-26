# My Star Feed ⭐

**更新于 2026-06-26 12:37**

<!-- FEED -->
- 📅 2026-06-26 10:26
- **[ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)** `b9803`
- 📝 更新内容：
  - 修复 OpenCL 在关闭时未刷新不完整性能分析批次的问题
  - 暂时禁用 macOS Apple Silicon 上启用 KleidiAI 的构建版本
  - 提供 macOS (arm64/x64) 和 iOS XCFramework 等多平台预编译二进制文件
- 🔗 [查看 Release](https://github.com/ggml-org/llama.cpp/releases/tag/b9803)

---

- 📅 2026-06-25 20:09
- **[anomalyco/opencode](https://github.com/anomalyco/opencode)** `v1.17.11`
- 📝 更新内容：
  - 核心：新增会话快照和回滚控制功能，支持将会话恢复到早期消息并还原文件变更
  - 核心：修复在浏览器流程无法打开时，MCP OAuth URL 不打印导致无法手动登录的问题
  - 桌面版：新增 Chrome 风格的标签页循环快捷键 (mod+1 至 mod+9)
  - 桌面版：支持标签页拖拽，并优化了无会话时的首页空状态和 v2 版最新跳转按钮样式
- 🔗 [查看 Release](https://github.com/anomalyco/opencode/releases/tag/v1.17.11)

---

- 📅 2026-06-25 06:20
- **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** `v1.1.1`
- 📝 更新内容：
  - 修复 1.0.0 引入的退化问题：重新让 CodeGraph 遵守 .gitignore 规则
  - 避免索引器遍历 gitignore 目录中的嵌套 git 仓库，解决图体积倍增和大型项目索引缓慢的问题
- 🔗 [查看 Release](https://github.com/colbymchenry/codegraph/releases/tag/v1.1.1)

---

- 📅 2026-06-25 22:31
- **[FufuLauncher/FufuLauncher](https://github.com/FufuLauncher/FufuLauncher)** `1.3.0.2`
- 📝 更新内容：
  - 修复插件消失、显存堆积、手柄热切换及帧数低下等多个功能异常问题
  - 重构多个界面，优化界面动画、字体以及部分插件功能的显示效果
  - 修复抽卡记录UP池异常、更新检查403、连点器无效及云游戏签到迁移等逻辑错误
- 🔗 [查看 Release](https://github.com/FufuLauncher/FufuLauncher/releases/tag/1.3.0.2)

---

- 📅 2026-06-24 11:06
- **[openclaw/openclaw](https://github.com/openclaw/openclaw)** `v2026.6.10`
- 📝 更新内容：
  - 新增自动快速对话模式：短对话自动启用快速模式，长文本回复自动切回常规模式并具兜底机制
  - 优化模型路由可靠性：Zai模型合成、GLM过载故障转移及原生推理级别选择现在更严格遵循活动模型目录
- 🔗 [查看 Release](https://github.com/openclaw/openclaw/releases/tag/v2026.6.10)

---

- 📅 2026-06-24 20:49
- **[microsoft/vscode](https://github.com/microsoft/vscode)** `1.126.0`
- 📝 更新内容：
  - 发布 v1.126.0 版本，具体更新详情请查看官方更新日志
  - 官方更新日志链接：https://code.visualstudio.com/updates/v1_126
- 🔗 [查看 Release](https://github.com/microsoft/vscode/releases/tag/1.126.0)

---

- 📅 2026-06-24 02:47
- **[Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)** `v0.26.0`
- 📝 更新内容：
  - 同步云端共享 API 契约至最新版本 00ef9cc
  - 合作伙伴节点更新：SoniloTextToMusic 节点价格减半
  - 新增 SDPoseDrawKeypoints 节点中禁用头部绘制的复选框
  - 修复使用 --base-directory 参数时启动消息中未记录基础目录日志的问题
- 🔗 [查看 Release](https://github.com/Comfy-Org/ComfyUI/releases/tag/v0.26.0)

---

- 📅 2026-06-24 10:38
- **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** `v4.8.3`
- 📝 更新内容：
  - 规则集现通过 SubagentStart 钩子注入子代理，确保生成的子代理也保持惰性策略
  - 文档新增韩语 README
  - 更新 README 中的 OpenCode npm 安装命令与徽章，移除过时的命令符号链接说明
- 🔗 [查看 Release](https://github.com/DietrichGebert/ponytail/releases/tag/v4.8.3)

---

- 📅 2026-06-23 00:16
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** `v4.13.0`
- 📝 更新内容：
  - 集成 Insane Search 模块，增强代理在开放网络中的信息检索能力
  - 提升应对恶劣环境的稳定性，修复网页被屏蔽、提供商波动、陈旧会话唤醒及平台打包边缘情况等问题
- 🔗 [查看 Release](https://github.com/code-yeongyu/oh-my-openagent/releases/tag/v4.13.0)

---

- 📅 2026-06-22 21:45
- **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** `v2.17.3`
- 📝 更新内容：
  - 修复自动捕获静默失败的问题
  - 迎来首位社区贡献者 @GraDea 参与修复
- 🔗 [查看 Release](https://github.com/tickernelz/opencode-mem/releases/tag/v2.17.3)

---

- 📅 2026-06-22 00:34
- **[Solsynth/Solian](https://github.com/Solsynth/Solian)** `3.9.0+233`
- 📝 更新内容：
  - 新增 CallKit 与 Siri 集成支持
  - 提示 GitHub Release 资产基于标签提交直接构建，可能缺少热修复，需访问特定站点获取完整版
- 🔗 [查看 Release](https://github.com/Solsynth/Solian/releases/tag/3.9.0%2B233)

---

- 📅 2026-06-20 12:45
- **[NapNeko/NapCatQQ](https://github.com/NapNeko/NapCatQQ)** `v4.18.7`
- 📝 更新内容：
  - 要求最低 NTQQ 版本为 40768，并提供 Windows 与 Linux (deb/rpm) 及 ARM64 架构的对应版本下载链接
  - 默认 WebUi 密钥改为随机密码，需在控制台查看
- 🔗 [查看 Release](https://github.com/NapNeko/NapCatQQ/releases/tag/v4.18.7)

---

- 📅 2026-06-20 03:39
- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** `v2026.6.19`
- 📝 更新内容：
  - 扩展触达渠道以支持 iMessage 等新对话入口
  - 深化与现有工具的集成并增强面向团队使用场景的支持
  - 包含约 1475 次提交、800 个合并 PR 及 245 名社区贡献者的大规模版本迭代
- 🔗 [查看 Release](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.6.19)
<!-- /FEED -->

---

*由 GitHub Actions 自动生成*
