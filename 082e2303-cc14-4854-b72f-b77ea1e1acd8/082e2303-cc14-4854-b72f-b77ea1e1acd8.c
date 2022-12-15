/*
NAME: 082e2303-cc14-4854-b72f-b77ea1e1acd8.c
QUESTION: Can I run sudo with no password?
CREATED: 2022-10-28 10:20:15.008630
*/
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

void test(void)
{
    int test = system("sudo -n whoami >/dev/null");
    if (test == 0)
    {
        exit(100);
    }
    else
    {
        exit(101);
    }
}

void clean(void)
{
    exit(100);
}

int main(int argc, char *argv[])
{
    if (argc > 1)
    {
        clean();
    }
    else
    {
        test();
    }
}