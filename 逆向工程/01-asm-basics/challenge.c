#include <stdio.h>
#include <string.h>

int main() {
    char input[64];
    printf("Enter the flag: ");
    fgets(input, 64, stdin);
    input[strcspn(input, "\n")] = 0;

    if (strlen(input) != 30) {
        printf("Wrong!\n");
        return 1;
    }

    unsigned char enc[] = {
        0xab, 0xa1, 0xac, 0xaa, 0xb6, 0xf9, 0xbe, 0xa0,
        0x92, 0xfc, 0xbe, 0x92, 0xb9, 0xa5, 0xfe, 0x92,
        0xaf, 0xf9, 0xbe, 0xfc, 0xae, 0xbe, 0x92, 0xfd,
        0xab, 0x92, 0xbf, 0xfe, 0xbb, 0xb0
    };

    for (int i = 0; i < 30; i++) {
        if ((input[i] ^ 0xcd) != enc[i]) {
            printf("Wrong!\n");
            return 1;
        }
    }

    printf("Correct! The flag is: %s\n", input);
    return 0;
}
