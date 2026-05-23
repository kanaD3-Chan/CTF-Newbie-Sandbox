#include <stdio.h>
#include <string.h>
#include <stdint.h>

void tea_encrypt(uint32_t *v, uint32_t *k) {
    uint32_t v0 = v[0], v1 = v[1];
    uint32_t sum = 0;
    uint32_t delta = 0x9e3779b9;
    for (int i = 0; i < 32; i++) {
        sum += delta;
        v0 += ((v1 << 4) + k[0]) ^ (v1 + sum) ^ ((v1 >> 5) + k[1]);
        v1 += ((v0 << 4) + k[2]) ^ (v0 + sum) ^ ((v0 >> 5) + k[3]);
    }
    v[0] = v0; v[1] = v1;
}

int main() {
    char input[64];
    uint32_t key[4] = {0xdeadbeef, 0xcafebabe, 0x12345678, 0x87654321};

    // Pre-computed: tea_encrypt on "flag{4lg0r1thm_r3c0gn1t10n_1s_k3y}" (padded to 32 bytes)
    uint32_t expected[8] = {
        0xf75e7798, 0x04c7c4b2,
        0x84d60457, 0x22677440,
        0xc2022040, 0xb51746e6,
        0x7adffb54, 0xe5d17296,
    };
    uint32_t buf[8];

    printf("Enter the flag: ");
    fgets(input, 64, stdin);
    input[strcspn(input, "\n")] = 0;

    int len = strlen(input);
    if (len > 32) {
        printf("Wrong!\n");
        return 1;
    }

    memset(buf, 0, 32);
    memcpy(buf, input, len);

    for (int i = 0; i < 8; i += 2)
        tea_encrypt(&buf[i], key);

    if (memcmp(buf, expected, 32) == 0)
        printf("Correct!\n");
    else
        printf("Wrong!\n");

    return 0;
}
