# My Star Feed ⭐

**更新于 2026-06-30 12:22**

<!-- FEED -->
- 📅 2026-06-30 10:08
- **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** `v1.1.5`
- 📝 更新内容：
  - 修复 C++ 类解析问题，带 export 或 visibility 宏（如 XXX_API、*_EXPORT、*_ABI）的类/结构体现在能被正确索引为真实类
  - 解决了宏导致解析器将整个声明误读为函数的问题，适用范围覆盖 Unreal Engine、Qt、Boost 及 LLVM 等库
- 🔗 [查看 Release](https://github.com/colbymchenry/codegraph/releases/tag/v1.1.5)

---

- 📅 2026-06-30 09:17
- **[ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)** `b9843`
- 📝 更新内容：
  - 回退了先前关于 split compute 期间减少同步的调度重构 (#20793)
  - 禁用了 macOS Apple Silicon (arm64) 上的 KleidiAI 支持
- 🔗 [查看 Release](https://github.com/ggml-org/llama.cpp/releases/tag/b9843)

---

- 📅 2026-06-29 22:52
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** `v4.14.0`
- 📝 更新内容：
  - /frontend 强制采用设计系统工作流，引用转为 DESIGN.md 契约，组件需追溯到 token 和状态，并验证渲染表面
  - Designpowers 功能内置于前端，统一 persona、无障碍约束、设计审查、设计债与移交等规则集，减少 UI 开发的临时性
  - 引入合成用户测试反馈至前端规则集
- 🔗 [查看 Release](https://github.com/code-yeongyu/oh-my-openagent/releases/tag/v4.14.0)

---

- 📅 2026-06-29 13:26
- **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** `v4.8.4`
- 📝 更新内容：
  - 新增作为原生 Hermes Agent 插件运行的支持，提供常驻上下文、内嵌技能和斜杠命令
  - 新增作为 Devin CLI 插件的分发支持
  - 技能触发机制优化，现在可响应任何编码任务而非仅限关键字提示，编码任务召回率由 2/6 提升至 6/6
- 🔗 [查看 Release](https://github.com/DietrichGebert/ponytail/releases/tag/v4.8.4)

---

- 📅 2026-06-28 11:27
- **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** `v2.17.4`
- 📝 更新内容：
  - 修复 Windows 构建及测试套件的兼容性问题
  - 修复 Web 端内存类型徽章的转义问题
- 🔗 [查看 Release](https://github.com/tickernelz/opencode-mem/releases/tag/v2.17.4)

---

- 📅 2026-06-27 06:24
- **[microsoft/vcpkg](https://github.com/microsoft/vcpkg)** `2026.06.24`
- 📝 更新内容：
  - 总端口数量达到 2849
  - x64-linux 可用端口数最多达 2780，arm-neon-android 可用端口数最少为 2208
- 🔗 [查看 Release](https://github.com/microsoft/vcpkg/releases/tag/2026.06.24)

---

- 📅 2026-06-25 22:31
- **[FufuLauncher/FufuLauncher](https://github.com/FufuLauncher/FufuLauncher)** `1.3.0.2`
- 📝 更新内容：
  - 修复插件消失、显存堆积、插件手柄热切换、插件帧数低下及连点器无效等问题
  - 重构多个界面，修复抽卡记录 UP 池异常、更新检查 403、云游戏签到迁移及浅色模式图鉴背景异常
- 🔗 [查看 Release](https://github.com/FufuLauncher/FufuLauncher/releases/tag/1.3.0.2)

---

- 📅 2026-06-25 20:09
- **[anomalyco/opencode](https://github.com/anomalyco/opencode)** `v1.17.11`
- 📝 更新内容：
  - Core 新增会话快照与还原控制，支持将会话回滚至早期消息及对应文件变更状态
  - Core 修复在浏览器流程打开时 MCP OAuth URL 未打印导致的手动登录问题
  - Desktop 新增 Chrome 风格的标签页循环快捷键（mod+1 至 mod+9）与可拖拽标签页
- 🔗 [查看 Release](https://github.com/anomalyco/opencode/releases/tag/v1.17.11)

---

- 📅 2026-06-24 20:49
- **[microsoft/vscode](https://github.com/microsoft/vscode)** `1.126.0`
- 📝 更新内容：
  - 发布 1.126.0 版本更新
  - 详细更新日志请参考 code.visualstudio.com/updates/v1_126
- 🔗 [查看 Release](https://github.com/microsoft/vscode/releases/tag/1.126.0)

---

- 📅 2026-06-24 11:06
- **[openclaw/openclaw](https://github.com/openclaw/openclaw)** `v2026.6.10`
- 📝 更新内容：
  - 引入自动快速模式（/fast auto），短对话快速启动，长任务或降级任务无损转至正常模式
  - 提升 Provider 路由、通道进度、会话身份及信任工具策略的可靠性
  - 优化了 Provider 设置、诊断及转录工具等细节功能
- 🔗 [查看 Release](https://github.com/openclaw/openclaw/releases/tag/v2026.6.10)

---

- 📅 2026-06-24 02:47
- **[Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)** `v0.26.0`
- 📝 更新内容：
  - 同步云端 OpenAPI 合约至最新版本
  - SoniloTextToMusic 合作节点价格减半
  - SDPoseDrawKeypoints 节点新增禁用头部绘制的复选框
  - 修复使用 --base-directory 时未将基础目录记录到启动日志的问题
- 🔗 [查看 Release](https://github.com/Comfy-Org/ComfyUI/releases/tag/v0.26.0)
<!-- /FEED -->

---

*由 GitHub Actions 自动生成*
