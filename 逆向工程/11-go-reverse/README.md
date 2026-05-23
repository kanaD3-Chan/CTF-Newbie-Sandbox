# 11 - Go 逆向

Go 编译出的二进制又是一种画风——静态链接、巨大的体积、字符串以 `(ptr, len)` 对的形式传递。最明显的特征是反编译后你会看到很多以 `go_` 开头的内部函数。

## 你能学到什么

- 识别 Go 编译的二进制（`runtime.*` 符号、goroutine 启动、Go build ID）
- Go 的 string 结构体（`type string struct { data *byte; len int }`）
- 静态链接带来的大量库代码

## 对比特征

| 特征 | Go | C |
|------|-----|-----|
| 链接方式 | 默认静态链接 | 默认动态链接 |
| 文件大小 | 1.5MB+ 起步 | 16KB |
| 符号表 | `runtime.main`、`go.shape.*` | `main`、`printf` |
| 字符串 | `(ptr, len)` 结构体 | null-terminated `char*` |

> Go 逆向有个很让人头疼的地方：因为静态链接，二进制里塞了整个 runtime 和标准库。你看到的代码 80% 是 Go 的内部实现。不过换个角度想——Go 的 `main` 函数永远是真正的入口，找到它，然后顺着看它调了什么。

## Flag

格式：`flag{...}`
