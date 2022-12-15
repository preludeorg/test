/*
NAME: 39de298a-911d-4a3b-aed4-1e8281010a9a.c
QUESTION: Health check
CREATED: 2022-11-17 14:11:16.510563
*/
#include <stdlib.h>

void test(void)
{
    exit(100);
}

void clean(void)
{
    exit(100);
}

int main(int argc, char *argv[])
{
    if (argc > 1) {
        clean();
    } else {
        test();
    }
}