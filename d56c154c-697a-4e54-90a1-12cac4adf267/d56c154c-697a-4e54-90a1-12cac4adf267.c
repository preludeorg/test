/*
NAME: d56c154c-697a-4e54-90a1-12cac4adf267.c
QUESTION: Do I have root privileges?
CREATED: 2022-10-28 10:08:27.169993
*/
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#define BUFSIZE 100

void test(void)
{
    char user[BUFSIZE];
    char *envvar = "USER";

    if (!getenv(envvar))
    {
        exit(1);
    }

    if (snprintf(user, BUFSIZE, "%s", getenv(envvar)) >= BUFSIZE)
    {
        exit(1);
    }

    if (strcmp(user, "root") == 0)
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