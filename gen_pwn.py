#!/usr/bin/env python3
import os

BASE = "/home/sunsi/育人资助项目/CTF出题库/二进制安全"

FLAG_PLACEHOLDER = "flag{placeholder_local_test}"

# ── 01: ret2text ────────────────────────────────────────
stack_src = r"""#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

void win() {
    system("cat /flag");
}

void vuln() {
    char buf[0x20];
    read(0, buf, 0x100);
}

int main() {
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    vuln();
    return 0;
}
"""

stack_df = r"""FROM ubuntu:22.04 AS builder
RUN apt-get update && apt-get install -y gcc
COPY vuln.c .
RUN gcc -no-pie -fno-stack-protector -o vuln vuln.c

FROM ubuntu:22.04
RUN apt-get update && apt-get install -y socat && useradd -m ctf
COPY --from=builder vuln /home/ctf/vuln
COPY flag /flag
RUN chmod +x /home/ctf/vuln
EXPOSE 13371
CMD socat TCP-LISTEN:13371,reuseaddr,fork EXEC:/home/ctf/vuln
"""

# ── 02: shellcode ───────────────────────────────────────
shellcode_src = r"""#include <stdio.h>
#include <unistd.h>

void vuln() {
    char buf[0x100];
    read(0, buf, 0x100);
    ((void (*)())buf)();
}

int main() {
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    vuln();
    return 0;
}
"""

shellcode_df = r"""FROM ubuntu:22.04 AS builder
RUN apt-get update && apt-get install -y gcc
COPY vuln.c .
RUN gcc -no-pie -fno-stack-protector -z execstack -o vuln vuln.c

FROM ubuntu:22.04
RUN apt-get update && apt-get install -y socat && useradd -m ctf
COPY --from=builder vuln /home/ctf/vuln
COPY flag /flag
RUN chmod +x /home/ctf/vuln
EXPOSE 13372
CMD socat TCP-LISTEN:13372,reuseaddr,fork EXEC:/home/ctf/vuln
"""

# ── 03: format-string ───────────────────────────────────
fmt_src = r"""#include <stdio.h>
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
    vuln();
    return 0;
}
"""

fmt_df = r"""FROM ubuntu:22.04 AS builder
RUN apt-get update && apt-get install -y gcc
COPY vuln.c .
RUN gcc -no-pie -fno-stack-protector -o vuln vuln.c

FROM ubuntu:22.04
RUN apt-get update && apt-get install -y socat && useradd -m ctf
COPY --from=builder vuln /home/ctf/vuln
COPY flag /flag
RUN chmod +x /home/ctf/vuln
EXPOSE 13373
CMD socat TCP-LISTEN:13373,reuseaddr,fork EXEC:/home/ctf/vuln
"""

# ── 04: canary + PIE ────────────────────────────────────
canary_src = r"""#include <stdio.h>
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
    vuln();
    return 0;
}
"""

canary_df = r"""FROM ubuntu:22.04 AS builder
RUN apt-get update && apt-get install -y gcc
COPY vuln.c .
RUN gcc -pie -fstack-protector -o vuln vuln.c

FROM ubuntu:22.04
RUN apt-get update && apt-get install -y socat && useradd -m ctf
COPY --from=builder vuln /home/ctf/vuln
COPY flag /flag
RUN chmod +x /home/ctf/vuln
EXPOSE 13374
CMD socat TCP-LISTEN:13374,reuseaddr,fork EXEC:/home/ctf/vuln
"""

# ── 05: ROP chain ───────────────────────────────────────
rop_src = r"""#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

const char *binsh = "/bin/sh";

void vuln() {
    char buf[0x20];
    read(0, buf, 0x100);
}

int main() {
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    vuln();
    return 0;
}
"""

rop_df = r"""FROM ubuntu:22.04 AS builder
RUN apt-get update && apt-get install -y gcc
COPY vuln.c .
RUN gcc -no-pie -fno-stack-protector -o vuln vuln.c

FROM ubuntu:22.04
RUN apt-get update && apt-get install -y socat && useradd -m ctf
COPY --from=builder vuln /home/ctf/vuln
COPY flag /flag
RUN chmod +x /home/ctf/vuln
EXPOSE 13375
CMD socat TCP-LISTEN:13375,reuseaddr,fork EXEC:/home/ctf/vuln
"""

# ── 06: ret2libc ────────────────────────────────────────
ret2libc_src = r"""#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

void vuln() {
    char buf[0x20];
    read(0, buf, 0x100);
    puts("Bye");
    read(0, buf, 0x100);
}

int main() {
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    puts("Hello");
    vuln();
    return 0;
}
"""

ret2libc_df = r"""FROM ubuntu:22.04 AS builder
RUN apt-get update && apt-get install -y gcc
COPY vuln.c .
RUN gcc -no-pie -fno-stack-protector -o vuln vuln.c

FROM ubuntu:22.04
RUN apt-get update && apt-get install -y socat && useradd -m ctf
COPY --from=builder vuln /home/ctf/vuln
COPY flag /flag
RUN chmod +x /home/ctf/vuln
EXPOSE 13376
CMD socat TCP-LISTEN:13376,reuseaddr,fork EXEC:/home/ctf/vuln
"""

# ── 07: heap (glibc 2.23) ──────────────────────────────
heap_src = r"""#include <stdio.h>
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
"""

heap_df = r"""FROM ubuntu:16.04 AS builder
RUN apt-get update && apt-get install -y gcc
COPY vuln.c .
RUN gcc -no-pie -fno-stack-protector -o vuln vuln.c

FROM ubuntu:16.04
RUN apt-get update && apt-get install -y socat && useradd -m ctf
COPY --from=builder vuln /home/ctf/vuln
COPY flag /flag
RUN chmod +x /home/ctf/vuln
EXPOSE 13377
CMD socat TCP-LISTEN:13377,reuseaddr,fork EXEC:/home/ctf/vuln
"""

# Write all files
challenges = [
    ("01-stack-overflow",  stack_src,      stack_df),
    ("02-shellcode",       shellcode_src,  shellcode_df),
    ("03-format-string",   fmt_src,        fmt_df),
    ("04-canary-pie",      canary_src,     canary_df),
    ("05-rop-chain",       rop_src,        rop_df),
    ("06-ret2libc",        ret2libc_src,   ret2libc_df),
    ("07-heap-basics",     heap_src,       heap_df),
]

for folder, src, df in challenges:
    path = os.path.join(BASE, folder)
    with open(os.path.join(path, "vuln.c"), "w") as f:
        f.write(src)
    with open(os.path.join(path, "Dockerfile"), "w") as f:
        f.write(df)
    with open(os.path.join(path, "flag"), "w") as f:
        f.write(FLAG_PLACEHOLDER + "\n")
    print(f"Created: {folder}")

print("Done!")
