# 10 - Rust 逆向

Rust 编译出来的二进制和 C 有很大的区别——长长的符号名（符号修饰）、运行时的一些安全检查、LLVM 风格的代码生成。第一次见到会觉得很陌生。

## 你能学到什么

- 识别 Rust 编译的二进制（`.rdata` 段里的 panic 消息、`core::*` 符号）
- 从 mangled symbol 中恢复函数名（`rustfilt` 或 `llvm-cxxfilt`）
- 理解 Rust 的 fat pointer 和 `&str` 表示方式

## 对比特征

| 特征 | Rust | C |
|------|------|----|
| 符号名 | `_ZN3std...` 长长的修饰名 | 短名或简单修饰 |
| 字符串 | 带长度信息的 fat pointer | null-terminated |
| 运行时 | 有整数溢出检查、panic 处理 | 裸奔 |

> Rust 逆向最让人头疼的就是符号修饰。好在 IDA Pro 最近的版本已经能自动 demangle Rust 符号了。如果你用的是 Ghidra，装一个 Rust 插件就好。

这道题逻辑上就是个 XOR，和前面的题没有本质区别。关键是通过这道题认识 Rust 二进制长什么样——以后遇到恶意软件、区块链合约之类的 Rust 逆向，至少心里有底。

## Flag

格式：`flag{...}`
