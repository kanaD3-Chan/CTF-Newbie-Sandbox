# 04 - 断点打在哪里

静态分析不是万能的。有些程序会在运行时才解密关键数据，你翻遍二进制也找不到 flag 的明文。

这时候就需要上调试器了。GDB 是你最忠实的伙伴。

## 关键思路

这道题的 flag 在编译时是加密存放的，`main` 函数会先调用 `decrypt` 原地解密，然后再跟你的输入比较。

所以正确的做法是：等 `decrypt` 执行完，在 `strcmp` 之前停下来。

```
gdb ./debugme
break *main+197
run
x/s $rbp-0x50
```

> 具体断点的偏移取决于你的编译结果，不一定正好是 +197。自己算一下 main 里哪条指令是 strcmp 的参数准备。

当然，你也可以选择不碰调试器，直接把解密算法用 Python 重写一遍。两种方法都能出答案。

## 解密算法

```c
void decrypt(unsigned char *buf, int len, int key) {
    for (int i = 0; i < len; i++) {
        buf[i] ^= (unsigned char)key;
        key = (key * 7 + 11) & 0xff;
    }
}
```

seed 是 `(0xabcd + 0xef) & 0xff`。

> 大部分人这道题都会卡在 GDB 命令上。记不住 `x/s` 什么的很正常——GDB 本来就不是给人设计的交互工具。不过调试器在手的时候，那些"这个 flag 到底在哪"的困惑感会少很多。

## Flag

格式：`flag{...}`
