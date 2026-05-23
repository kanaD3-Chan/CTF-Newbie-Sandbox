# 06 - 文件头里的秘密

这个 ELF 文件看起来和普通程序没什么区别。但 flag 不在代码里——它藏在 ELF 文件的结构里。

## 你能学到什么

- ELF 文件的段（section）结构
- `.note` 段的用途
- 用 `readelf` 和 `objdump` 查看文件元数据

## 怎么玩

```
readelf -S flag_hider
```

看看有没有什么"多余"的段。找到之后：

```
readelf -p .note.flag flag_hider
```

flag 就在那里。

> 如果你看到 `__attribute__((section(".note.flag")))` 这个关键字就该明白了——C 语言可以把数据编译到指定的段里，不一定要写在代码路径上。有些恶意软件就用这个手法藏配置，只不过藏的是 C2 地址而不是 flag。

## Flag

格式：`flag{...}`
