#include <stdio.h>
#include <string.h>

__attribute__((noinline))
int validate(const char *input) {
    unsigned char enc[] = {
        0x8f, 0x80, 0x66, 0x65, 0x0e, 0x6c, 0x10, 0x51,
        0x73, 0x72, 0x5a, 0x7f, 0x3e, 0x84, 0x3f, 0x57,
        0x49, 0x12, 0x08, 0x3f, 0xb1, 0xeb, 0x87, 0xbd,
        0xd3, 0xd9,
    };
    int len = strlen(input);
    if (len != 26) return 0;

    for (int i = 0; i < 26; i++) {
        // opaque predicate: always true
        int x = (i * i + i) % 2;  // always 0 for consecutive integers
        if (x) return 0;  // dead code

        // convoluted key derivation with dead code
        int k = i + 0xab;
        k = (k * 7 + 11) & 0xff;
        k ^= 0x55;
        k = (k + 0x37) & 0xff;
        k ^= 0xcd;

        // actual check
        if ((input[i] ^ k) != enc[i])
            return 0;
    }
    return 1;
}

int main() {
    char input[64];
    printf("Enter the flag: ");
    fgets(input, 64, stdin);
    input[strcspn(input, "\n")] = 0;
    if (validate(input))
        printf("Correct!\n");
    else
        printf("Wrong!\n");
    return 0;
}
