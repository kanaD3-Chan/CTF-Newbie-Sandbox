#include <stdio.h>
#include <unistd.h>

__asm__(".text\n"
        ".global my_gadget\n"
        "my_gadget:\n"
        "  pop %rdi\n"
        "  ret\n");

void vuln() {
    char buf[0x20];
    read(0, buf, 0x100);
    puts("Bye");
}

int main() {
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    puts("Hello");
    vuln();
    return 0;
}
