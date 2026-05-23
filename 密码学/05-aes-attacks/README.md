# AES 的弱点

**出题人：** KanaDE
**难度：** Medium
**方向：** Crypto

---

AES-ECB 模式加密。

相同的明文块，加密出相同的密文块。

这道题利用的就是这个性质——构造特定的输入，推断出 flag。

你有一个 `aes_oracle.py`，其中 `oracle(plaintext)` 函数会加密 `plaintext + flag`。

通过选择不同的 `plaintext`，你可以逐字节推断出 flag 的内容。

---

**附件：** `aes_oracle.py`
