# 08 - APK 拆开看看

逆向不只有 ELF，还有 APK（Android 应用包）。Android 应用跑在 Java 虚拟机上，字节码比 x86 汇编好读得多——这意味着你需要的不是汇编基础，而是反编译工具。

## 你能学到什么

- 用 `jadx` 或 `CFR` 反编译 `.class` / `.dex` 文件
- 读 Java 字节码
- 理解 Java 的 `charAt()`、字符串比较等常见模式

## 怎么玩

```
# 直接反编译 .class 文件
javap -c FlagChecker.class
```

> `javap` 是 JDK 自带的工具，输出的是 JVM 字节码而不是 Java 源码，可读性稍差。如果你想要源码级别的输出，用 `jadx` 或 `CFR`。

这道题就是一个纯粹的 XOR 校验，没有任何花招。反编译出来看到 enc 数组和 XOR key（0x22），直接写脚本解密。

## Flag

格式：`flag{...}`
