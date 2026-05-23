# 03 - 汇编读不懂？先从这里开始

"我不会汇编"——这大概是阻碍最多人入坑逆向的一句话。

实话说，你不需要精通汇编才能做逆向。CTF 里 90% 的逆向题，看懂这几条指令就够了：`mov`、`xor`、`cmp`、`jz`/`jnz`、`call`、`lea`。遇到不会的，现查。

## 题目的逻辑

`main` 函数干了这么几件事：

1. 读入字符串
2. 检查长度——必须是 30 字节
3. 循环 30 次，每个字节和 `0xcd` 异或，跟硬编码数组比较

翻译成 C 大概长这样：

```c
for (int i = 0; i < 30; i++) {
    if ((input[i] ^ 0xcd) != enc[i]) {
        printf("Wrong!\n");
        return 1;
    }
}
```

## 怎么玩

```
$ ./challenge
Enter the flag: test
Wrong!
```

拖进 IDA，找到 `main`，按 F5 看伪代码。或者直接 `objdump -d challenge | less` 硬读汇编——不丢人，很多人一开始就是这么干的。

> 看到 `xor` 和 `cmp` 头皮发麻的话，先打开 Google 搜 "x86 xor instruction" 花十分钟看一下，比硬扛有用得多。

## Flag

格式：`flag{...}`
