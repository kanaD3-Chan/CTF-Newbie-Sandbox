#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

void win() {
    system("cat /flag");
}

void vuln() {
    char buf[0x20];
    read(0, buf, 0x40);
    printf(buf);
    read(0, buf, 0x100);
}

int main() {
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    puts("=== SLsec Pwn: Canary + PIE Bypass ===");
    vuln();
    return 0;
}
