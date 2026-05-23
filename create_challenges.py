#!/usr/bin/env python3
import os

BASE = "/home/sunsi/育人资助项目/CTF出题库"

def mkfile(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def challenge_readme(title, author, difficulty, direction, description):
    return f"""# {title}

**出题人：** {author}
**难度：** {difficulty}
**方向：** {direction}

---

{description}
"""

WEB = [
    ("01-sql-injection", "你好，数据库", "Easy", """登录框。用户名，密码，提交。

这道题就这么多。

但你有没有想过，后端在拿到你输入的内容之后，直接拼进了 SQL 语句里？

试试看。

---

**靶机：** `http://172.16.173.140:[port]`"""),
    ("02-file-upload", "上传就完事了？", "Easy", """一个文件上传页面。

它说只允许上传图片。

你信吗？

---

**靶机：** `http://172.16.173.140:[port]`"""),
    ("03-xss", "你的 Cookie 我收下了", "Medium", """这是一个留言板。你可以在上面留言，管理员会定期查看。

管理员的 Cookie 里有 flag。

你懂我的意思吧？

---

**靶机：** `http://172.16.173.140:[port]`"""),
    ("04-command-injection", "ping 一下试试", "Medium", """一个网络工具页面，输入 IP 地址，它会帮你 ping 一下。

很方便。

但如果你输入的不只是 IP 地址呢？

---

**靶机：** `http://172.16.173.140:[port]`"""),
    ("05-file-inclusion", "include 进来看看", "Medium", """PHP 的 include 函数很好用——可以把任意文件的内容包含进来。

这道题的后端用了 include，而且参数是你控制的。

flag 在 /flag 里。

---

**靶机：** `http://172.16.173.140:[port]`"""),
    ("06-ssrf", "让服务器帮我访问", "Medium", """这个网站有一个功能：输入一个 URL，它会帮你抓取页面内容。

很贴心。

但它能访问的，不只是公网。内网里有什么？

---

**靶机：** `http://172.16.173.140:[port]`"""),
    ("07-xxe", "XML 里藏着什么", "Medium", """这个接口接受 XML 格式的数据。

XML 有一个功能叫外部实体——可以读取服务器上的文件。

你知道怎么用吗？

---

**靶机：** `http://172.16.173.140:[port]`"""),
    ("08-deserialization", "反序列化的代价", "Hard", """后端用 PHP 的 unserialize() 处理了你传入的数据。

这个函数有点危险。

flag 在 /flag 里。

---

**靶机：** `http://172.16.173.140:[port]`"""),
    ("09-access-control", "你没有权限——真的吗", "Medium", """普通用户看不到 flag，只有管理员能看。

但这个权限校验，真的靠谱吗？

试着改改请求，看看会发生什么。

---

**靶机：** `http://172.16.173.140:[port]`"""),
]

REVERSE = [
    ("01-asm-basics", "汇编读不懂？先从这里开始", "Easy", """一个简单的 ELF 程序，输入正确的字符串就能拿到 flag。

没有加密，没有混淆，就是纯粹的汇编逻辑。

用 IDA 或者 Ghidra 打开，找到比较的地方，读懂它。

---

**附件：** `challenge`"""),
    ("02-pe-elf-format", "文件头里的秘密", "Easy", """这个文件看起来是个普通的 ELF，但它的某些字段被动过手脚。

flag 就藏在文件结构里——不是在代码里，是在格式里。

用 010 Editor 或者 readelf 仔细看看。

---

**附件：** `mystery`"""),
    ("03-static-analysis", "IDA 第一课", "Easy", """一个 C 程序，输入密码，验证通过就输出 flag。

密码是硬编码在程序里的。

用 IDA 或 Ghidra 打开，找到验证逻辑，逆出密码。

---

**附件：** `crackme`"""),
    ("04-dynamic-debug", "断点打在哪里", "Medium", """这个程序的验证逻辑有点绕，静态分析看不太清楚。

试试动态调试——在关键位置下断点，看看运行时的值。

GDB 或者 x64dbg，选一个你顺手的。

---

**附件：** `debugme`"""),
    ("05-algorithm-recognition", "这是什么加密", "Medium", """程序对输入做了某种变换，然后和一个硬编码的值比较。

变换的逻辑看起来很眼熟——你见过这个算法吗？

识别它，逆向它，拿到 flag。

---

**附件：** `encrypted`"""),
    ("06-anti-obfuscation", "壳里面是什么", "Medium", """这个程序加了壳。

直接分析什么都看不到。

先脱壳，再逆向。

---

**附件：** `packed`"""),
    ("07-script-reverse", "Python 也能逆", "Easy", """一个 .pyc 文件。

Python 字节码，反编译一下就能看到源码。

然后逆出 flag。

---

**附件：** `verify.pyc`"""),
    ("08-android-reverse", "APK 拆开看看", "Medium", """一个 Android APK。

用 jadx 反编译，找到验证逻辑，逆出正确的输入。

---

**附件：** `app-release.apk`"""),
    ("09-windows-reverse", "Windows 下的逆向", "Medium", """一个 Windows PE 程序。

输入正确的序列号就能拿到 flag。

用 x64dbg 或者 IDA 分析。

---

**附件：** `keygen.exe`"""),
]

PWN = [
    ("01-stack-overflow", "溢出第一步", "Easy", """一个没有任何保护的 32 位程序。

有一个 gets() 调用，有一个 win() 函数。

你知道该怎么做。

---

**靶机：** `nc 172.16.173.140 [port]`
**附件：** `vuln`"""),
    ("02-ret2libc", "libc 在哪里", "Medium", """开了 NX，没有 win() 函数。

但 libc 里有 system()。

先泄露 libc 基址，再 getshell。

---

**靶机：** `nc 172.16.173.140 [port]`
**附件：** `vuln`, `libc.so.6`"""),
    ("03-format-string", "格式化字符串的秘密", "Medium", """`printf(buf)` ——就这一行，没有格式化字符串。

你能读出栈上的内容吗？能改掉某个变量的值吗？

flag 就在某个全局变量里。

---

**靶机：** `nc 172.16.173.140 [port]`
**附件：** `vuln`"""),
    ("04-canary-pie", "绕过保护机制", "Hard", """开了 Canary 和 PIE。

但程序还有一个格式化字符串漏洞。

先泄露，再溢出。

---

**靶机：** `nc 172.16.173.140 [port]`
**附件：** `vuln`"""),
    ("05-shellcode", "写一段 shellcode", "Medium", """程序会读取你的输入，然后直接执行它。

写一段 shellcode，拿到 shell。

注意：有字符过滤。

---

**靶机：** `nc 172.16.173.140 [port]`
**附件：** `vuln`"""),
    ("06-rop-chain", "ROP 链拼图", "Hard", """开了 NX，没有 shellcode 可用。

但程序里有足够的 gadget。

拼一条 ROP 链，调用 execve("/bin/sh")。

---

**靶机：** `nc 172.16.173.140 [port]`
**附件：** `vuln`"""),
    ("07-heap-basics", "堆的第一课", "Hard", """一个菜单题。申请、释放、查看。

有一个 UAF 漏洞。

你能控制程序流吗？

---

**靶机：** `nc 172.16.173.140 [port]`
**附件：** `vuln`, `libc.so.6`"""),
    ("08-heap-advanced", "tcache 投毒", "Hard", """glibc 2.31，tcache 机制。

有一个 double free。

利用 tcache poisoning，把 malloc 的返回值指向任意地址，改掉 __free_hook。

---

**靶机：** `nc 172.16.173.140 [port]`
**附件：** `vuln`, `libc.so.6`"""),
]

CRYPTO = [
    ("01-classical-cipher", "凯撒大帝的密信", "Easy", """一段密文。看起来像英文，但每个字母都错位了。

凯撒大帝用的就是这个——他以为没人能破解。

---

**密文：**
```
Wkh iodjv lv: iodj{fdhvdu_flskhu_lv_ixq}
```"""),
    ("02-rsa-attacks", "RSA 不是铁板一块", "Easy", """给你 n、e、c。

n 很小，可以直接分解。

分解之后，求出 d，解密，拿到 flag。

---

**附件：** `params.txt`"""),
    ("03-aes-attacks", "AES 的弱点", "Medium", """AES-ECB 模式加密。

相同的明文块，加密出相同的密文块。

这道题利用的就是这个性质——构造特定的输入，推断出 flag。

---

**靶机：** `nc 172.16.173.140 [port]`"""),
    ("04-hash-attacks", "哈希碰撞", "Easy", """后端用 MD5 验证密码，但用的是 PHP 的弱类型比较（==）。

你知道 0e 开头的 MD5 值有什么特殊性质吗？

---

**靶机：** `http://172.16.173.140:[port]`"""),
    ("05-stream-cipher", "流密码的秘密", "Medium", """两段密文，用的是同一个密钥流加密的。

已知其中一段的明文。

你能解出另一段吗？

---

**附件：** `ciphertexts.txt`"""),
    ("06-number-theory", "数论基础", "Hard", """一道 RSA 变体题。

e 和 phi(n) 不互素，普通的求逆元方法不管用。

需要用到一些数论知识——Rabin 密码体制，或者 AMM 算法。

---

**附件：** `params.txt`"""),
    ("07-ecc", "椭圆曲线上的秘密", "Hard", """椭圆曲线密码学。

曲线参数有问题——阶太小，可以暴力破解离散对数。

用 SageMath 算一下。

---

**附件：** `params.txt`"""),
    ("08-diffie-hellman", "密钥交换的漏洞", "Hard", """一个 Diffie-Hellman 密钥交换协议的实现。

但参数选得很糟糕——g 的阶太小，离散对数可以暴力求解。

---

**附件：** `transcript.txt`"""),
    ("09-misc-crypto", "奇怪的编码", "Easy", """一段看起来乱七八糟的字符串。

不是 Base64，不是 Hex，不是 ASCII。

但它确实是某种编码。识别它，解码它，拿到 flag。

---

**附件：** `encoded.txt`"""),
]

MISC = [
    ("01-encoding-tricks", "这是什么编码", "Easy", """一段字符串，套了好几层编码。

Base64、Hex、摩斯电码……一层一层剥开，最里面是 flag。

---

**附件：** `encoded.txt`"""),
    ("02-steganography", "图片里藏着什么", "Easy", """一张普通的 PNG 图片。

用 LSB 隐写藏了一段数据。

工具很多，选一个用就行。

---

**附件：** `image.png`"""),
    ("03-image-forensics", "图片取证", "Easy", """这张图片的宽高被改过了，导致显示不完整。

修复文件头，看看完整的图片里藏着什么。

---

**附件：** `broken.png`"""),
    ("04-qrcode", "二维码修复", "Medium", """一个损坏的二维码。部分模块被涂黑了。

二维码有纠错机制——修复它，扫描它，拿到 flag。

---

**附件：** `damaged_qr.png`"""),
    ("05-traffic-analysis", "流量里的秘密", "Easy", """一个 pcap 文件。

里面有一段 HTTP 流量，flag 就在某个请求或响应里。

用 Wireshark 过滤，找到它。

---

**附件：** `capture.pcap`"""),
    ("06-disk-forensics", "磁盘取证", "Medium", """一个磁盘镜像文件。

有文件被删除了，但删除不等于消失。

用取证工具恢复，找到 flag。

---

**附件：** `disk.img`"""),
    ("07-incident-response", "应急响应", "Medium", """一台被入侵的 Linux 系统的内存镜像。

攻击者留下了什么？

用 Volatility 分析，找到攻击者的痕迹——flag 就在里面。

---

**附件：** `memory.raw`"""),
    ("08-osint", "开源情报", "Medium", """一张照片。

照片里有一些细节——建筑、路牌、植被。

根据这些信息，确定拍摄地点，拿到 flag。

---

**附件：** `photo.jpg`"""),
    ("09-blockchain", "区块链上的秘密", "Hard", """一个部署在测试链上的智能合约。

合约里有一个 flag，但只有满足某个条件才能取出来。

读懂合约逻辑，构造正确的调用。

---

**合约地址：** `[address]`
**附件：** `Contract.sol`"""),
]

AI = [
    ("01-prompt-injection", "提示词注入", "Easy", """一个 AI 助手，系统提示词里藏着 flag。

它被告知不能透露系统提示词。

你能让它说出来吗？

---

**靶机：** `http://172.16.173.140:[port]`"""),
    ("02-jailbreak", "越狱", "Easy", """一个有安全限制的 AI 模型。

它拒绝回答某些问题。

用角色扮演或者其他方式绕过它的限制，让它说出 flag。

---

**靶机：** `http://172.16.173.140:[port]`"""),
    ("03-llm-app-security", "LLM 应用安全", "Medium", """一个基于 LLM 的 Web 应用。

用户的输入会被拼进 prompt 里，然后发给模型。

你能通过构造输入，让模型执行你想要的操作，泄露 flag 吗？

---

**靶机：** `http://172.16.173.140:[port]`"""),
    ("04-adversarial-examples", "对抗样本", "Medium", """一个图像分类器，输入正确的类别才能拿到 flag。

但你可以对图片做微小的修改——肉眼看不出来，但分类器会判断错。

用 FGSM 生成对抗样本，让分类器把它误判为目标类别。

---

**靶机：** `http://172.16.173.140:[port]`
**附件：** `target.png`, `model_info.txt`"""),
    ("05-model-extraction", "模型提取", "Hard", """一个黑盒模型，只能通过 API 查询。

通过大量查询，推断出模型的决策边界，然后构造一个能绕过它的输入。

flag 在绕过之后的响应里。

---

**靶机：** `http://172.16.173.140:[port]`"""),
    ("06-multimodal-attack", "多模态攻击", "Hard", """一个接受图片和文字输入的多模态模型。

在图片里嵌入对抗性文字，让模型忽略用户的真实指令，执行你的指令。

---

**靶机：** `http://172.16.173.140:[port]`"""),
    ("07-federated-learning", "联邦学习隐私攻击", "Hard", """一个联邦学习场景的模拟。

通过分析梯度更新，推断出训练数据中的敏感信息。

flag 就藏在训练数据里。

---

**靶机：** `http://172.16.173.140:[port]`
**附件：** `gradients.pkl`"""),
    ("08-ai-tools", "AI 安全工具实战", "Medium", """综合题。

需要用到 AI 安全工具——ART（Adversarial Robustness Toolbox）或者 TextFooler。

具体用哪个，看题目给的环境和提示。

---

**靶机：** `http://172.16.173.140:[port]`
**附件：** `challenge.py`"""),
    ("09-ai-ctf-summary", "AI CTF 综合挑战", "Hard", """一道综合题，涵盖 Prompt Injection、对抗样本、模型安全多个方向。

没有明确的提示，自己判断该用什么方法。

拿到 flag 的路不止一条。

---

**靶机：** `http://172.16.173.140:[port]`"""),
]

DIRECTIONS = [
    ("Web安全", "Web", WEB),
    ("逆向工程", "Reverse", REVERSE),
    ("二进制安全", "Pwn", PWN),
    ("密码学", "Crypto", CRYPTO),
    ("Misc杂项", "Misc", MISC),
    ("AI安全", "AI", AI),
]

for dir_name, dir_short, challenges in DIRECTIONS:
    dir_path = os.path.join(BASE, dir_name)
    checklist = []
    for folder, title, difficulty, desc in challenges:
        challenge_path = os.path.join(dir_path, folder)
        readme_path = os.path.join(challenge_path, "README.md")
        content = challenge_readme(title, "KanaDE", difficulty, dir_short, desc)
        mkfile(readme_path, content)
        checklist.append(f"- [ ] [{title}](./{folder}/README.md)")

    # Update direction README
    readme_path = os.path.join(dir_path, "README.md")
    with open(readme_path, 'r', encoding='utf-8') as f:
        old = f.read()

    # Replace old checklist section
    checklist_str = "\n".join(checklist)
    new_content = f"""# {dir_name}

## 待出题目

{checklist_str}
"""
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"Done: {dir_name} ({len(challenges)} challenges)")

print("All done!")
