#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

char *chunks[16];
int count = 0;

void menu() {
    write(1, "1.alloc 2.delete 3.edit 4.view 5.exit\n", 39);
}

void alloc() {
    if (count >= 16) { write(1, "full\n", 5); return; }
    char buf[16];
    write(1, "size: ", 6);
    int n = read(0, buf, 8); buf[n - 1] = 0;
    int size = atoi(buf);
    chunks[count] = malloc(size);
    write(1, "data: ", 6);
    read(0, chunks[count], size);
    count++;
}

void delete() {
    char buf[16];
    write(1, "index: ", 7);
    int n = read(0, buf, 8); buf[n - 1] = 0;
    int idx = atoi(buf);
    if (idx < 0 || idx >= count || !chunks[idx]) {
        write(1, "invalid\n", 8);
        return;
    }
    free(chunks[idx]);
}

void edit() {
    char buf[16];
    write(1, "index: ", 7);
    int n = read(0, buf, 8); buf[n - 1] = 0;
    int idx = atoi(buf);
    if (idx < 0 || idx >= count || !chunks[idx]) {
        write(1, "invalid\n", 8);
        return;
    }
    write(1, "data: ", 6);
    read(0, chunks[idx], 0x60);
}

void view() {
    char buf[16];
    write(1, "index: ", 7);
    int n = read(0, buf, 8); buf[n - 1] = 0;
    int idx = atoi(buf);
    if (idx < 0 || idx >= count || !chunks[idx]) {
        write(1, "invalid\n", 8);
        return;
    }
    write(1, chunks[idx], 8);
}

int main() {
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    write(1, "=== SLsec Pwn: Heap Basics (Fastbin) ===\n", 41);
    while (1) {
        menu();
        char buf[16];
        int n = read(0, buf, 4); buf[n - 1] = 0;
        switch (atoi(buf)) {
            case 1: alloc(); break;
            case 2: delete(); break;
            case 3: edit(); break;
            case 4: view(); break;
            case 5: exit(0);
            default: write(1, "?\n", 2);
        }
    }
    return 0;
}
