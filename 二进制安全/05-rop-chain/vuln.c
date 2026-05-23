#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

const char *binsh = "/bin/sh";

/* embedded gadget: pop rdi; ret */
__asm__(".text\n"
        ".global my_gadget\n"
        "my_gadget:\n"
        "  pop %rdi\n"
        "  ret\n");

void vuln() {
    char buf[0x20];
    read(0, buf, 0x100);
}

int main() {
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    puts("ok");
    /* force system into PLT (dead branch kept by volatile) */
    volatile int x = 0;
    if (x) system("/bin/sh");
    vuln();
    return 0;
}
