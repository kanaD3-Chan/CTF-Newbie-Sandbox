#include <stdio.h>
#include <unistd.h>

void vuln() {
    char buf[0x100];
    read(0, buf, 0x100);
    ((void (*)())buf)();
}

int main() {
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    puts("=== SLsec Pwn: Shellcode Injection ===");
    vuln();
    return 0;
}
