#!/usr/bin/env python3
import os
import shutil

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

def reorder(dir_path, mapping):
    """mapping: list of (old_name, new_name). Use tmp prefix to avoid conflicts."""
    for old, new in mapping:
        old_path = os.path.join(dir_path, old)
        tmp_path = os.path.join(dir_path, "tmp-" + new)
        if os.path.exists(old_path):
            shutil.move(old_path, tmp_path)
    for _, new in mapping:
        tmp_path = os.path.join(dir_path, "tmp-" + new)
        final_path = os.path.join(dir_path, new)
        if os.path.exists(tmp_path):
            shutil.move(tmp_path, final_path)

def write_readme(dir_path, dir_name, challenges):
    checklist = "\n".join(
        f"- [ ] [{title}](./{folder}/README.md)"
        for folder, title in challenges
    )
    mkfile(os.path.join(dir_path, "README.md"),
           f"# {dir_name}\n\n## 待出题目\n\n{checklist}\n")

# ── Web安全 ──────────────────────────────────────────────
web_dir = os.path.join(BASE, "Web安全")

# Shift existing 01-09 → 04-12
reorder(web_dir, [
    ("09-access-control",   "12-access-control"),
    ("08-deserialization",  "11-deserialization"),
    ("07-xxe",              "10-xxe"),
    ("06-ssrf",             "09-ssrf"),
    ("05-file-inclusion",   "08-file-inclusion"),
    ("04-command-injection","07-command-injection"),
    ("03-xss",              "06-xss"),
    ("02-file-upload",      "05-file-upload"),
    ("01-sql-injection",    "04-sql-injection"),
])

# New beginner challenges
new_web = [
    ("01-view-source", "Ctrl+U", "Easy", """打开这个页面，按下 Ctrl+U。

就这样。

---

**靶机：** `http://172.16.173.140:[port]`"""),
    ("02-robots-txt", "爬虫不让去的地方", "Easy", """网站有一个文件叫 robots.txt，告诉搜索引擎哪些页面不要爬。

但它告诉了你。

---

**靶机：** `http://172.16.173.140:[port]`"""),
    ("03-http-header", "响应头里的秘密", "Easy", """有时候 flag 不在页面里，在 HTTP 响应头里。

打开开发者工具，看看 Network 面板。

---

**靶机：** `http://172.16.173.140:[port]`"""),
]

for folder, title, difficulty, desc in new_web:
    path = os.path.join(web_dir, folder, "README.md")
    mkfile(path, challenge_readme(title, "KanaDE", difficulty, "Web", desc))

write_readme(web_dir, "Web安全", [
    ("01-view-source",      "Ctrl+U"),
    ("02-robots-txt",       "爬虫不让去的地方"),
    ("03-http-header",      "响应头里的秘密"),
    ("04-sql-injection",    "你好，数据库"),
    ("05-file-upload",      "上传就完事了？"),
    ("06-xss",              "你的 Cookie 我收下了"),
    ("07-command-injection","ping 一下试试"),
    ("08-file-inclusion",   "include 进来看看"),
    ("09-ssrf",             "让服务器帮我访问"),
    ("10-xxe",              "XML 里藏着什么"),
    ("11-deserialization",  "反序列化的代价"),
    ("12-access-control",   "你没有权限——真的吗"),
])
print("Web安全 done")

# ── 逆向工程 ─────────────────────────────────────────────
# New order: static-analysis(1), script-reverse(2), asm-basics(3),
#            dynamic-debug(4), algorithm-recognition(5), pe-elf-format(6),
#            anti-obfuscation(7), android-reverse(8), windows-reverse(9)
rev_dir = os.path.join(BASE, "逆向工程")
reorder(rev_dir, [
    ("03-static-analysis",      "01-static-analysis"),
    ("07-script-reverse",       "02-script-reverse"),
    ("01-asm-basics",           "03-asm-basics"),
    ("04-dynamic-debug",        "04-dynamic-debug"),
    ("05-algorithm-recognition","05-algorithm-recognition"),
    ("02-pe-elf-format",        "06-pe-elf-format"),
    ("06-anti-obfuscation",     "07-anti-obfuscation"),
    ("08-android-reverse",      "08-android-reverse"),
    ("09-windows-reverse",      "09-windows-reverse"),
])
write_readme(rev_dir, "逆向工程", [
    ("01-static-analysis",      "IDA 第一课"),
    ("02-script-reverse",       "Python 也能逆"),
    ("03-asm-basics",           "汇编读不懂？先从这里开始"),
    ("04-dynamic-debug",        "断点打在哪里"),
    ("05-algorithm-recognition","这是什么加密"),
    ("06-pe-elf-format",        "文件头里的秘密"),
    ("07-anti-obfuscation",     "壳里面是什么"),
    ("08-android-reverse",      "APK 拆开看看"),
    ("09-windows-reverse",      "Windows 下的逆向"),
])
print("逆向工程 done")

# ── 密码学 ───────────────────────────────────────────────
# New order: classical-cipher(1), misc-crypto(2), hash-attacks(3),
#            rsa-attacks(4), aes-attacks(5), stream-cipher(6),
#            diffie-hellman(7), number-theory(8), ecc(9)
crypto_dir = os.path.join(BASE, "密码学")
reorder(crypto_dir, [
    ("01-classical-cipher", "01-classical-cipher"),
    ("09-misc-crypto",      "02-misc-crypto"),
    ("04-hash-attacks",     "03-hash-attacks"),
    ("02-rsa-attacks",      "04-rsa-attacks"),
    ("03-aes-attacks",      "05-aes-attacks"),
    ("05-stream-cipher",    "06-stream-cipher"),
    ("08-diffie-hellman",   "07-diffie-hellman"),
    ("06-number-theory",    "08-number-theory"),
    ("07-ecc",              "09-ecc"),
])
write_readme(crypto_dir, "密码学", [
    ("01-classical-cipher", "凯撒大帝的密信"),
    ("02-misc-crypto",      "奇怪的编码"),
    ("03-hash-attacks",     "哈希碰撞"),
    ("04-rsa-attacks",      "RSA 不是铁板一块"),
    ("05-aes-attacks",      "AES 的弱点"),
    ("06-stream-cipher",    "流密码的秘密"),
    ("07-diffie-hellman",   "密钥交换的漏洞"),
    ("08-number-theory",    "数论基础"),
    ("09-ecc",              "椭圆曲线上的秘密"),
])
print("密码学 done")

# ── Misc杂项 ─────────────────────────────────────────────
# New order: encoding-tricks(1), image-forensics(2), steganography(3),
#            qrcode(4), traffic-analysis(5), disk-forensics(6),
#            incident-response(7), osint(8), blockchain(9)
misc_dir = os.path.join(BASE, "Misc杂项")
reorder(misc_dir, [
    ("01-encoding-tricks",  "01-encoding-tricks"),
    ("03-image-forensics",  "02-image-forensics"),
    ("02-steganography",    "03-steganography"),
    ("04-qrcode",           "04-qrcode"),
    ("05-traffic-analysis", "05-traffic-analysis"),
    ("06-disk-forensics",   "06-disk-forensics"),
    ("07-incident-response","07-incident-response"),
    ("08-osint",            "08-osint"),
    ("09-blockchain",       "09-blockchain"),
])
write_readme(misc_dir, "Misc杂项", [
    ("01-encoding-tricks",  "这是什么编码"),
    ("02-image-forensics",  "图片取证"),
    ("03-steganography",    "图片里藏着什么"),
    ("04-qrcode",           "二维码修复"),
    ("05-traffic-analysis", "流量里的秘密"),
    ("06-disk-forensics",   "磁盘取证"),
    ("07-incident-response","应急响应"),
    ("08-osint",            "开源情报"),
    ("09-blockchain",       "区块链上的秘密"),
])
print("Misc杂项 done")

# ── AI安全 ───────────────────────────────────────────────
# New order: prompt-injection(1), jailbreak(2), llm-app-security(3),
#            adversarial-examples(4), ai-tools(5), model-extraction(6),
#            multimodal-attack(7), federated-learning(8), ai-ctf-summary(9)
ai_dir = os.path.join(BASE, "AI安全")
reorder(ai_dir, [
    ("01-prompt-injection",     "01-prompt-injection"),
    ("02-jailbreak",            "02-jailbreak"),
    ("03-llm-app-security",     "03-llm-app-security"),
    ("04-adversarial-examples", "04-adversarial-examples"),
    ("08-ai-tools",             "05-ai-tools"),
    ("05-model-extraction",     "06-model-extraction"),
    ("06-multimodal-attack",    "07-multimodal-attack"),
    ("07-federated-learning",   "08-federated-learning"),
    ("09-ai-ctf-summary",       "09-ai-ctf-summary"),
])
write_readme(ai_dir, "AI安全", [
    ("01-prompt-injection",     "提示词注入"),
    ("02-jailbreak",            "越狱"),
    ("03-llm-app-security",     "LLM 应用安全"),
    ("04-adversarial-examples", "对抗样本"),
    ("05-ai-tools",             "AI 安全工具实战"),
    ("06-model-extraction",     "模型提取"),
    ("07-multimodal-attack",    "多模态攻击"),
    ("08-federated-learning",   "联邦学习隐私攻击"),
    ("09-ai-ctf-summary",       "AI CTF 综合挑战"),
])
print("AI安全 done")

print("\nAll done!")
