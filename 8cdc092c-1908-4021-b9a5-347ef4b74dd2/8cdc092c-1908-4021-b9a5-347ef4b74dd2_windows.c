/*
NAME: 8cdc092c-1908-4021-b9a5-347ef4b74dd2_windows.c
QUESTION: Are there macro enabled Office documents on this host?
CREATED: 2022-11-05
*/
#include <windows.h>
#include <stdio.h>


int endsWith(const char *str, const char *suffix)
{
    size_t str_len = strlen(str);
    size_t suffix_len = strlen(suffix);
    return (str_len >= suffix_len) && (!memcmp(str + str_len - suffix_len, suffix, suffix_len));
}

int test_file_extension(char *filename)
{
    char file_extensions[7][10] = {".docm", ".dotm", ".xlsm", ".xltm", ".pptm", ".potm", ".ppsm"};
    for (size_t i = 0; i < sizeof(file_extensions) / sizeof(file_extensions[0]); i++) {
        if (endsWith(filename, file_extensions[i])) {
            return 1;
        }
    }
    return 0;
}

int find_macro_file(const char *folder, char *fullpath)
{
    char wildcard[MAX_PATH];
    char path[MAX_PATH];
    sprintf(wildcard, "%s\\*", folder);
    WIN32_FIND_DATA fd;
    HANDLE handle = FindFirstFile(wildcard, &fd);
    if (handle == INVALID_HANDLE_VALUE) return 0;

    do
    {
        if (strcmp(fd.cFileName, ".") == 0 || strcmp(fd.cFileName, "..") == 0) continue;

        sprintf(path, "%s\\%s", folder, fd.cFileName);
        if (test_file_extension(path)) {
            strcpy(fullpath, path);
        } else if (fd.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) {
            find_macro_file(path, fullpath);
        }

        if(strlen(fullpath)) break;
    } while (FindNextFile(handle, &fd));

    FindClose(handle);
    return strlen(fullpath);
}

void test(void)
{
    CHAR *tmpDir = getenv("HOMEPATH");
    char fullpath[MAX_PATH];
    if (find_macro_file(tmpDir, fullpath)) {
        printf("Found: %s\n", fullpath);
        exit(100);
    }
    exit(101);
}

void clean(void)
{
    exit(100);
}

int main(int argc, char *argv[]) {
    if (argc > 1) {
        clean();
    } else {
        test();
    }
}