FROM ubuntu:22.04 AS builder
RUN apt-get update && apt-get install -y gcc
COPY vuln.c .
RUN gcc -no-pie -fno-stack-protector -o vuln vuln.c

FROM ubuntu:22.04
RUN apt-get update && apt-get install -y socat && useradd -m ctf
COPY --from=builder vuln /home/ctf/vuln
RUN chmod +x /home/ctf/vuln
EXPOSE 13373
CMD sh -c 'echo "$FLAG" > /flag && exec socat TCP-LISTEN:13373,reuseaddr,fork EXEC:/home/ctf/vuln'
