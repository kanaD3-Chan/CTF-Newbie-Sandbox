# libc 在哪里

**出题人：** KanaDE
**难度：** Medium
**方向：** Pwn

---

开了 NX，没有 win() 函数。

但 libc 里有 system()。

先泄露 libc 基址，再 getshell。

---

**靶机：** `nc 172.16.173.140 [port]`
**附件：** `vuln`, `libc.so.6`
