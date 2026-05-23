# 02 - Python 也能逆

谁说逆向一定要看汇编？有时候附件就是个 `.pyc` 文件。

Python 的字节码（bytecode）本质上是一套栈式虚拟机的指令集，跟你平时写的 Python 代码是一一对应的。区别只是——它更啰嗦，而且变量名全丢了。

## 你能学到什么

- 用 `uncompyle6` 或 `pycdc` 把 `.pyc` 反编译回 `.py`
- 如果反编译工具失效（比如 Python 版本太新），直接读字节码
- Python 字节码常见指令：`LOAD_CONST`、`LOAD_FAST`、`BINARY_OP`、`COMPARE_OP`

## 怎么玩

附件是一个 `verify.pyc`。两种玩法：

```bash
# 方法一：反编译工具
pycdc verify.pyc

# 方法二：直接读字节码
python3 -c "import dis; import marshal; f=open('verify.pyc','rb'); f.read(16); dis.dis(marshal.load(f))"
```

> 反编译出来的代码有时候跑不了，这很正常。照着字节码手写一个等效的解密脚本就行，反正逻辑很简单——找到 enc 数组和 key，XOR 回去。

## Flag

格式：`flag{...}`
