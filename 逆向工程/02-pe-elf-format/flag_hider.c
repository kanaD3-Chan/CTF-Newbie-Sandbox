#include <stdio.h>
#include <string.h>

__attribute__((section(".note.flag")))
const unsigned char hidden_flag[] = "flag{3lf_s3ct10n_h3ad3r5_0r_d1rty}";

int main() {
    char input[64];
    printf("Enter the flag: ");
    fgets(input, 64, stdin);
    input[strcspn(input, "\n")] = 0;
    if (strcmp(input, (char *)hidden_flag) == 0)
        printf("Correct!\n");
    else
        printf("Wrong!\n");
    return 0;
}
