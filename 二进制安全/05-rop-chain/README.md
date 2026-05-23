# ROP 链拼图

**出题人：** KanaDE
**难度：** Hard
**方向：** Pwn

---

开了 NX，没有 shellcode 可用。

但程序里有足够的 gadget。

拼一条 ROP 链，调用 execve("/bin/sh")。

---

**靶机：** `nc 172.16.173.140 [port]`
**附件：** `vuln`
