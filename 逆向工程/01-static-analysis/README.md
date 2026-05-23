# 01 - IDA 第一课

说实话，大部分人在逆向一道题的时候，第一反应就是"拖进 IDA 看看"。

IDA 就像逆向工程的记事本——你不会用它写诗，但少了它你连购物清单都写不利索。这道题就是让你习惯这个流程的。

## 你能学到什么

- 把 ELF 文件丢进 IDA（或 Ghidra）看看长什么样
- 找到 `main` 函数，看反编译出的伪代码
- 识别 XOR 加密的特征（`xor` 指令 + 硬编码的字节数组）
- 用 Python 写个循环就跑出 flag

## 玩法

```
$ file crackme
crackme: ELF 64-bit LSB executable, x86-64, not stripped

$ ./crackme
Enter the flag: test
Wrong!
```

不拖 IDA 的话，直接用 `strings` 也能看到加密后的字节数组。XOR 的 key 是 `0x37`，藏得不算深。

> 这道题编译的时候没开 PIE，函数地址是固定的，反编译直接就能看到 `main`。

## Flag

格式：`flag{...}`

**记住**：你的第一个逆向分析工具不是 AI，是你的眼睛。
