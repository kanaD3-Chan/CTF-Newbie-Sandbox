# tcache 投毒

**出题人：** KanaDE
**难度：** Hard
**方向：** Pwn

---

glibc 2.31，tcache 机制。

有一个 double free。

利用 tcache poisoning，把 malloc 的返回值指向任意地址，改掉 __free_hook。

---

**靶机：** `nc 172.16.173.140 [port]`
**附件：** `vuln`, `libc.so.6`
