#include <stdio.h>
#include <string.h>

int main() {
    char input[64];
    printf("Enter the flag: ");
    fgets(input, 64, stdin);
    input[strcspn(input, "\n")] = 0;

    const unsigned char password[] = {
        0x51, 0x5b, 0x56, 0x50, 0x4c, 0x44, 0x43, 0x03,
        0x43, 0x06, 0x54, 0x68, 0x03, 0x59, 0x03, 0x5b,
        0x4e, 0x44, 0x06, 0x44, 0x68, 0x06, 0x44, 0x68,
        0x04, 0x03, 0x02, 0x4e, 0x4a
    };

    if (strlen(input) != sizeof(password)) {
        printf("Wrong!\n");
        return 1;
    }

    for (int i = 0; i < sizeof(password); i++) {
        if ((input[i] ^ 0x37) != password[i]) {
            printf("Wrong!\n");
            return 1;
        }
    }

    printf("Correct! The flag is: %s\n", input);
    return 0;
}
