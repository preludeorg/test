# Can you excute SharpWMI on this host?

[SharpWMI](https://github.com/GhostPack/SharpWMI) is an open-source implementation of various functionality found in [Windows Management Instrumentation (WMI)](https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmi-start-page). WMI is a powerful Windows-native framework used for systems and data administration. The abuse of WMI functionality by adversaries is well-documented - WMI is listed in the [MITRE ATT&CK](https://attack.mitre.org/techniques/T1047/) framework with many references to it's [use by state-sponsored actors](https://www.cisa.gov/uscert/ncas/alerts/aa21-321a).

 SharpWMI enables a user to perform WMI actions without using native WMI tooling. By avoiding the use of built-in WMI tooling, signature and heuristic based detection content designed to catch suspicious usage of WMI may not detect SharpWMI, even though they work in functionally similar ways.  With SharpWMI, it's possible to perform WMI queries, execute code, enumerate systems and system information, and create processes.

 ## How

> Safety: the test does drop a known malicious to disk but executes it without any options.

This test will drop a pre-compiled SharpWMI executable to disk and attempt to execute it with no options as a saftey measure. Endpoint controls are expected to block execution.
