# My Star Feed ⭐

**更新于 2026-06-25 21:36**

<!-- FEED -->
- 📅 2026-06-12 00:44
- **[sglwsjxh/GenshinMacro](https://github.com/sglwsjxh/GenshinMacro)** `v1.1.1`
- 📝 更新内容：
  - 修复双玛头时间差问题，补齐迁移时丢失的100ms延迟以恢复原始输入节奏
  - 从Python全面迁移至C# .NET 10 WPF并采用MVVM架构
  - 输入引擎改用Win32 SendInput原生API替代pydirectinput
  - 新增启动自动提权与xUnit单元测试覆盖
- 🔗 [查看 Release](https://github.com/sglwsjxh/GenshinMacro/releases/tag/v1.1.1)

---

- 📅 2026-06-12 13:16
- **[sglwsjxh/rag-mcp](https://github.com/sglwsjxh/rag-mcp)** `v1.0.2`
- 📝 更新内容：
  - 新增搜索结果低置信度标注功能，基于CONFIDENCE_THRESHOLD配置标记高/低/未知
  - 实现文件MD5哈希去重，同知识库内重复内容自动跳过入库
  - 全库搜索支持按知识库分组返回结果，单库搜索维持扁平列表
  - 新增pytest测试框架及25个核心场景的smoke test
- 🔗 [查看 Release](https://github.com/sglwsjxh/rag-mcp/releases/tag/v1.0.2)

---

- 📅 2026-06-08 01:48
- **[sglwsjxh/ffix](https://github.com/sglwsjxh/ffix)** `v1.1.3`
- 📝 更新内容：
  - 所有LLM API调用强制使用response_format: json_object确保结构化输出
  - 引入Zod schema替代手动JSON解析，简化验证逻辑
  - 新增Schema验证失败自动重试机制，附带错误提示降低无修复错误率
- 🔗 [查看 Release](https://github.com/sglwsjxh/ffix/releases/tag/v1.1.3)

---

- 📅 2026-06-08 01:27
- **[lingfengQAQ/webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer)** `v6.2.0`
- 📝 更新内容：
  - 优化命令结束后的结果报告可读性，统一展示已完成、部分完成与未完成状态
  - 写章失败后支持断点恢复，重试时自动检查已完成步骤并从失败处继续
  - 精简上下文读取提示词，减少无关参考资料占用以保持长流程重点
  - 最小写章模式增加明确的跳过审查记录，不再伪装审查已通过
- 🔗 [查看 Release](https://github.com/lingfengQAQ/webnovel-writer/releases/tag/v6.2.0)

---

- 📅 2026-06-05 00:33
- **[microsoft/vcpkg](https://github.com/microsoft/vcpkg)** `2026.06.01`
- 📝 更新内容：
  - 总端口数达到2832个
  - x64-linux可用端口数达2754个，x64-windows达2735个
  - 提供各架构triplet的可用端口详细计数统计
- 🔗 [查看 Release](https://github.com/microsoft/vcpkg/releases/tag/2026.06.01)
<!-- /FEED -->

---

*由 GitHub Actions 自动生成*
