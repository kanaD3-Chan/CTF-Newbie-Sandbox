#include <stdio.h>
#include <string.h>

int main() {
    char input[64];
    unsigned char enc[] = {
        0x33, 0x39, 0x34, 0x32, 0x2e, 0x22, 0x64, 0x3b,
        0x31, 0x65, 0x22, 0x60, 0x0a, 0x25, 0x30, 0x0a,
        0x33, 0x64, 0x39, 0x66, 0x0a, 0x27, 0x66, 0x23,
        0x66, 0x27, 0x26, 0x64, 0x3b, 0x32, 0x28,
    };

    printf("Enter the flag: ");
    fgets(input, 64, stdin);
    input[strcspn(input, "\n")] = 0;

    if (strlen(input) != 31) {
        printf("Wrong!\n");
        return 1;
    }

    for (int i = 0; i < 31; i++) {
        if ((input[i] ^ 0x55) != enc[i]) {
            printf("Wrong!\n");
            return 1;
        }
    }
    printf("Correct!\n");
    return 0;
}
