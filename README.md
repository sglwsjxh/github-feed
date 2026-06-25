# My Star Feed ⭐

**更新于 2026-06-25 21:16**

<!-- FEED -->
- 📅 2026-06-25 21:16
- **[sglwsjxh/github-feed](https://github.com/sglwsjxh/github-feed)**
- 📝 更新内容：
  - 优化 Star 仓库动态抓取逻辑，支持解析包含新 Release tag 的推送事件
  - 修复当 starred 仓库大批量更新时的 API 限流导致的推送遗漏问题
- 🔗 [查看 Release](https://github.com/sglwsjxh/github-feed)

---

- 📅 2026-06-25 21:10
- **[microsoft/vscode](https://github.com/microsoft/vscode)** `1.126.0`
- 📝 更新内容：
  - 引入多光标协作编辑模式，支持在同一文件内由不同用户驱动独立光标
  - 重构内置终端渲染引擎，大幅降低高频繁输出场景下的 CPU 占用
  - 优化 Copilot 上下文注入策略，减少代码补全时的内存峰值消耗
- 🔗 [查看 Release](https://github.com/microsoft/vscode)

---

- 📅 2026-06-25 21:02
- **[ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)** `b9789`
- 📝 更新内容：
  - 新增对 Qualcomm NPU 的原生算子支持，端侧推理速度提升 60%
  - 修复在多卡张量并行分割时特定层分配不均导致的 NaN 梯度问题
  - 优化 KV Cache 量化策略，百亿参数模型上下文窗口内存占用降低 30%
- 🔗 [查看 Release](https://github.com/ggml-org/llama.cpp)

---

- 📅 2026-06-25 21:00
- **[anomalyco/opencode](https://github.com/anomalyco/opencode)** `v1.17.11`
- 📝 更新内容：
  - 新增 Agent 工作流 DAG 可视化面板，直观审查多步代码生成与审查依赖
  - 修复语义检索在超大型代码库中上下文截断导致补全不完整的问题
  - 优化文件监控服务，显著降低在 node_modules 等巨型目录变更时的 CPU 唤醒频率
- 🔗 [查看 Release](https://github.com/anomalyco/opencode)

---

- 📅 2026-06-25 19:41
- **[lfnovo/open-notebook](https://github.com/lfnovo/open-notebook)** `v1.10.0`
- 📝 更新内容：
  - 新增多模态音频摘要生成，支持自动从播客录音提取关键论点时间戳
  - 引入实时协作文档编辑，支持多人同时在同一 Notebook 条目中修改
  - 修复 PDF 文献解析在双栏排版下的段落交错合并错误
- 🔗 [查看 Release](https://github.com/lfnovo/open-notebook)

---

- 📅 2026-06-25 18:41
- **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** `v2026.6.19`
- 📝 更新内容：
  - 全新实现基于反思链的自动调试工具，支持代码报错后自主修正并验证
  - 优化长上下文窗口的策略路由，减少无关工具调用带来的 Token 损耗
  - 修复在沙箱环境中并发文件写入导致的死锁问题
- 🔗 [查看 Release](https://github.com/NousResearch/hermes-agent)

---

- 📅 2026-06-25 18:01
- **[code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)** `v4.13.0`
- 📝 更新内容：
  - 引入自适应 Token 预算分配器，在代码生成与测试环节智能动态分配算力
  - 新增 OpenCode 底座支持，无缝对接 Codex 与本地推理后端
  - 修复复杂仓库结构下依赖解析循环导致的 Agent 假死现象
- 🔗 [查看 Release](https://github.com/code-yeongyu/oh-my-openagent)

---

- 📅 2026-06-25 18:04
- **[Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)** `v0.26.0`
- 📝 更新内容：
  - 重构核心调度器，支持工作流节点的动态子图并行执行
  - 新增对 Flux 变分自编码器的原生加载支持，显存峰值占用缩减 25%
  - 修复在 Chrome 较新版本中 WebGPU 后端初始化偶发的 GPU 上下文丢失错误
- 🔗 [查看 Release](https://github.com/Comfy-Org/ComfyUI)

---

- 📅 2026-06-25 08:03
- **[microsoft/vcpkg](https://github.com/microsoft/vcpkg)** `2026.06.01`
- 📝 更新内容：
  - 更新基础端口库至 3200+，新增 Intel oneAPI DPC++ 编译器工具链适配
  - 修复在 ARM64 macOS 平台上交叉编译时 CMake 系统链接路径推导错误
  - 优化二进制缓存命中策略，避免因微小版本号差异导致的全局重编译
- 🔗 [查看 Release](https://github.com/microsoft/vcpkg)

---

- 📅 2026-06-25 06:20
- **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** `v1.1.1`
- 📝 更新内容：
  - 新增实时文件监听与增量索引同步，代码变更后图谱刷新延迟降至 500ms 内
  - 优化 LLM 查询时的子图裁剪算法，将 Codex 上下文污染率降低 40%
  - 修复解析 TypeScript 类型别名时存在的死循环导致 OOM 崩溃问题
- 🔗 [查看 Release](https://github.com/colbymchenry/codegraph)

---

- 📅 2026-06-25 01:55
- **[rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk)** `v0.10.0`
- 📝 更新内容：
  - 新增对 Cursor 及 Windsurf 编码进度的实时动作捕捉与桌面宠物反馈
  - 优化宠物渲染引擎帧率，在低配设备上降低 50% GPU 占用
  - 修复多显示器切换时宠物窗口定位漂移无法正常拖拽的问题
- 🔗 [查看 Release](https://github.com/rullerzhou-afk/clawd-on-desk)

---

- 📅 2026-06-25 20:07
- **[FufuLauncher/FufuLauncher](https://github.com/FufuLauncher/FufuLauncher)** `1.3.0.1`
- 📝 更新内容：
  - 新增游戏内覆盖面板，支持实时显示帧率与网络延迟
  - 修复在特定 Windows 11 更新下注入模块被安全中心误杀拦截的问题
  - 优化自动签到服务的定时器调度，修复长时间挂机失效及重复请求
- 🔗 [查看 Release](https://github.com/FufuLauncher/FufuLauncher)

---

- 📅 2026-06-25 20:04
- **[Solsynth/Solian](https://github.com/Solsynth/Solian)** `3.9.0+233`
- 📝 更新内容：
  - 全新重写 Solar Network 即时通讯模块，消息投递延迟降低至 50ms
  - 新增动态分享卡片生成并导出至本地功能
  - 修复在大屏 Android 设备上边栏导航手势与页面滑动冲突的问题
- 🔗 [查看 Release](https://github.com/Solsynth/Solian)

---

- 📅 2026-06-25 20:46
- **[openclaw/openclaw](https://github.com/openclaw/openclaw)** `v2026.6.10`
- 📝 更新内容：
  - 引入跨设备工作状态无缝热迁移，切换环境无需重载上下文
  - 新增对离线 TTS 语音缓存复用与播放控制的支持
  - 修复 Wayland 环境下全局快捷键注册失效导致语音唤醒无响应的问题
- 🔗 [查看 Release](https://github.com/openclaw/openclaw)

---

- 📅 2026-06-25 19:05
- **[cli/cli](https://github.com/cli/cli)** `v2.95.0`
- 📝 更新内容：
  - 新增 gh repo insights 命令，支持命令行直接查看仓库社区健康度与依赖图
  - 优化 OAuth 设备流程刷新机制，解决长时间挂机操作过期导致的鉴权失败
  - 修复在签出包含 Git LFS 大文件的 PR 时因指针锁引发的合并冲突误报
- 🔗 [查看 Release](https://github.com/cli/cli)

---

- 📅 2026-06-24 21:37
- **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** `v4.8.3`
- 📝 更新内容：
  - 优化惰性函数生成逻辑，自动识别并剔除无副作用的无用代码分支
  - 新增对复杂异步并发场景下的状态机折叠与化简策略
  - 修复代码生成器处理模板字符串时因类型推导失败导致的循环依赖
- 🔗 [查看 Release](https://github.com/DietrichGebert/ponytail)

---

- 📅 2026-06-24 20:10
- **[ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev)**
- 📝 更新内容：
  - 新增 Vercel Edge Config 与 Supabase Vector 免费额度说明条目
  - 更新 AWS Free Tier 中 S3 请求配额与过期策略说明
  - 修正 Cloudflare Workers 免费计划每日调用次数限制描述
- 🔗 [查看 Release](https://github.com/ripienaar/free-for-dev)

---

- 📅 2026-06-24 15:38
- **[NapNeko/NapCatQQ](https://github.com/NapNeko/NapCatQQ)** `v4.18.7`
- 📝 更新内容：
  - 适配 NTQQ 最新核心协议底层变动，修复频繁掉线与 45 报错问题
  - 优化高并发消息下发的事件分发队列，大幅降低群消息风暴时延迟
  - 修复处理特殊 CQ 码图片节点反序列化时触发的内存越界异常
- 🔗 [查看 Release](https://github.com/NapNeko/NapCatQQ)

---

- 📅 2026-06-23 04:32
- **[tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem)** `v2.17.3`
- 📝 更新内容：
  - 引入本地 SQLite 向量数据库作为持久化存储后端，重启会话不丢失记忆
  - 优化高频长上下文写入时的去重检查算法，内存占用峰值降低约 40%
  - 修复语义检索时在阈值为 0 的边界条件引发的全文档无效扫全表问题
- 🔗 [查看 Release](https://github.com/tickernelz/opencode-mem)

---

- 📅 2026-06-23 15:54
- **[cheahjs/free-llm-api-resources](https://github.com/cheahjs/free-llm-api-resources)**
- 📝 更新内容：
  - 新增 DeepSeek V4 API 公测免费轮次与 Chutes AI 使能信息
  - 更新 OpenAI 免费计划速率限制，细化不同终端的 RPM 限额
  - 修正 Gemini Flash 模型最新定价策略与免费层上下文窗口说明
- 🔗 [查看 Release](https://github.com/cheahjs/free-llm-api-resources)

---

- 📅 2026-06-23 12:53
- **[sglwsjxh/BetterNTE](https://github.com/sglwsjxh/BetterNTE)** `v1.1.0`
- 📝 更新内容：
  - 新增自定义 SD 建模分辨率接入与视角切换预设
  - 修复异环游戏更新后内存特征基址偏移导致辅助读取失败的问题
  - 优化全局帧率平滑逻辑，减少高速移动场景下的渲染卡顿
- 🔗 [查看 Release](https://github.com/sglwsjxh/BetterNTE)

---

- 📅 2026-06-22 20:50
- **[mrexodia/ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp)** `1.4.0`
- 📝 更新内容：
  - 新增 Claude 与 GPT-4o 多模型切换支持，提供逆向指令集专用提示词模板
  - 优化反编译结果注入 IDB 时的类型推导推断，减少手动修复类型次数
  - 修复 IDA 批量分析模式干预下 MCP 服务端异步请求超时断连问题
- 🔗 [查看 Release](https://github.com/mrexodia/ida-pro-mcp)

---

- 📅 2026-06-22 11:01
- **[opendatalab/MinerU](https://github.com/opendatalab/MinerU)** `mineru-3.4.0-released`
- 📝 更新内容：
  - 全新集成基于布局感知的表格识别引擎，复杂嵌套表格结构与合并单元格解析准确率提升 35%
  - 新增原生 .docx 格式直接解析与转换，无需依赖 LibreOffice 转换中转
  - 修复处理超大 PDF（>1000页）时内存溢出导致应用崩溃的问题
- 🔗 [查看 Release](https://github.com/opendatalab/MinerU)

---

- 📅 2026-06-22 12:21
- **[XSRQMiracle/Miracle-Dashboard](https://github.com/XSRQMiracle/Miracle-Dashboard)**
- 📝 更新内容：
  - 新增 GPU 显存占用与 CUDA 核心利用率独立监控面板
  - 优化 Rust 采集守护进程的数据传输结构体，降低开关高频采集时 20% CPU 损耗
  - 修复在 Wayland 环境下 WebUI 自动刷新 WebSocket 连接断开崩溃的问题
- 🔗 [查看 Release](https://github.com/XSRQMiracle/Miracle-Dashboard)

---

- 📅 2026-06-22 20:00
- **[babalae/better-genshin-impact](https://github.com/babalae/better-genshin-impact)** `0.61.2`
- 📝 更新内容：
  - 适配 5.0 版本全新尘歌壶地图场景与交互物件识别
  - 修复自动钓鱼 AI 在新鱼类抛竿判定时间缩短导致抛竿失败的问题
  - 优化全自动七圣召唤卡牌流派识别算法，降低策略选择延迟
- 🔗 [查看 Release](https://github.com/babalae/better-genshin-impact)

---

- 📅 2026-06-19 18:11
- **[slkiser/opencode-quota](https://github.com/slkiser/opencode-quota)** `v3.10.1`
- 📝 更新内容：
  - 新增 Kimi Code 与 Alibaba Coding Plan 配额追踪与自动限流
  - 修复 OpenAI Plus 配额统计在高并发流式响应时 Token 扣减计算延迟不准的问题
  - 优化注入式拦截显式输出，确保零上下文窗口污染交互体验
- 🔗 [查看 Release](https://github.com/slkiser/opencode-quota)

---

- 📅 2026-06-19 02:30
- **[icebear0828/codex-proxy](https://github.com/icebear0828/codex-proxy)** `v2.0.83`
- 📝 更新内容：
  - 全面适配 OpenAI 最新 Responses API 代理协议格式
  - 新增自动 OAuth 令牌池管理，过期 Token 无感刷新并重试排队
  - 修复高并发流式请求代理时，偶发缓冲区截断导致的 JSON 解析报错
- 🔗 [查看 Release](https://github.com/icebear0828/codex-proxy)

---

- 📅 2026-06-20 10:26
- **[zyf2007/ChatAPI](https://github.com/zyf2007/ChatAPI)**
- 📝 更新内容：
  - 新增基于 OpenAI Responses API 规范的 Assistant 回调注入与模拟接口
  - 优化对话状态机调度逻辑，修复复杂交互分支状态覆盖 Bug
  - 修复流式响应在特定网络 MTU 下分包导致的 Token 输出乱序问题
- 🔗 [查看 Release](https://github.com/zyf2007/ChatAPI)
<!-- /FEED -->

---

*由 GitHub Actions 自动生成*
