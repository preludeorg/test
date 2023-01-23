# Can you excute Seatbelt on this host?

[Seatbelt](https://github.com/GhostPack/Seatbelt) Seatbelt is a C# project that conducts a variety of host-survey "safety checks" that are significant from both an offensive and defensive security standpoint. These include enumeration for providers registered for [AMSI](https://learn.microsoft.com/en-us/windows/win32/amsi/antimalware-scan-interface-portal), the current user's saved credentials using CredEnumerate(), and DNS cache entries (via [WMI](https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmi-start-page)).

 ## How

> Safety: the test does drop a known malicious to disk but executes it without any options.

This test will drop a pre-compiled Seatbelt executable to disk and attempt to execute it with no options as a saftey measure. Endpoint controls are expected to block execution.
