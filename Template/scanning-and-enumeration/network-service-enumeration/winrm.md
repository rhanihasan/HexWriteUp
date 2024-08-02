---
description: >-
  WinRM uses the WS-Management protocol to communicate between machines. It can
  be configured for both HTTP and HTTPS transports
---

# WinRM

Windows Remote Management (WinRM) is a Microsoft protocol that allows administrators to:&#x20;

* Run commands
* Access management information
* Run scripts
* Connect to remote Windows servers
* Run PowerShell commands on remote computers
* port number 5985 for http & 5986 for https



### evil-winrm

* Guest Session using evil-winrm

```bash
evil-winrm -i #Target-IP -u #Username -p #Password
>> Tab Tab Twice to see the option its offer.
```
