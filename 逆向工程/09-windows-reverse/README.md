# 09 - Windows 下的逆向

说到逆向，大家默认都是 Linux ELF。但现实世界里 Windows 的 PE 文件才是主流——恶意软件、桌面软件、游戏，大部分都是 PE。

## 你能学到什么

- PE 文件格式的基本结构（DOS 头、NT 头、节区表）
- 用 `file` 命令识别交叉编译的 PE 文件
- 用 IDA / x64dbg 分析 Windows 程序

## 玩法

```
$ file win_crackme.exe
win_crackme.exe: PE32+ executable for MS Windows 5.02 (console), x86-64
```

这个程序是用 MinGW 交叉编译的，逻辑和前面几道题一样简单——XOR 比较。

> 如果你没有 Windows 环境，直接用 IDA 打开也能分析。PE 和 ELF 在函数级别的逆向上没有本质区别，入口点换成 `main` 之后的事情都差不多。

## Flag

格式：`flag{...}`
