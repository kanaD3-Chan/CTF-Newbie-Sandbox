#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

char target[] = "You need to change this";

void vuln() {
    char buf[0x100];
    read(0, buf, 0x100);
    printf(buf);

    if (target[0] == 'W' && target[1] == 'I' && target[2] == 'N') {
        system("cat /flag");
    }
}

int main() {
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    puts("=== SLsec Pwn: Format String ===");
    vuln();
    return 0;
}
