# 堆的第一课

**出题人：** KanaDE
**难度：** Hard
**方向：** Pwn

---

一个菜单题。申请、释放、查看。

glibc 2.23，没有 tcache，fastbin 是主角。

有一个 UAF 漏洞——释放之后指针没清零。利用它伪造 fastbin chunk，把 malloc 的返回值打到 `__malloc_hook`。

---

**靶机：** `nc 172.16.173.140 [port]`
**附件：** `vuln`, `libc-2.23.so`
