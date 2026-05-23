#include <stdio.h>
#include <string.h>

void decrypt(unsigned char *buf, int len, int key) {
    for (int i = 0; i < len; i++) {
        buf[i] ^= (unsigned char)key;
        key = (key * 7 + 11) & 0xff;
    }
}

int main() {
    char input[64];
    unsigned char flag[64];
    int seed;

    // 加密后的 flag，seed = (0xabcd + 0xef) & 0xff = 0xbc
    unsigned char enc[] = {
        0xda, 0x43, 0x35, 0x30, 0x17, 0x9b, 0x7d, 0x69,
        0x28, 0xa2, 0x85, 0x94, 0x93, 0xfb, 0x57, 0xa5,
        0x09, 0x59, 0x22, 0xde, 0x42, 0x78, 0x9b, 0x56,
        0xaf, 0x50, 0x04, 0x07, 0xfb, 0xec, 0x56, 0x7a
    };

    seed = (0xabcd + 0xef) & 0xff;
    memcpy(flag, enc, 32);
    decrypt(flag, 32, seed);
    flag[32] = 0;

    printf("Enter the flag: ");
    fgets(input, 64, stdin);
    input[strcspn(input, "\n")] = 0;

    if (strcmp(input, (char *)flag) == 0) {
        printf("Correct!\n");
    } else {
        printf("Wrong!\n");
    }

    return 0;
}
