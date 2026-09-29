# OS-Info-parcer
In this repository you can find python code that takes info about system, where he was started, and parce it in .json

## ⚠️ Disclaimer

This repository is an **educational project** developed solely for academic, learning, and research purposes. 

- The software contains **no malicious code**, backdoors, or telemetry intended for unauthorized data harvesting.
- It operates strictly within user space to read public system metrics and hardware parameters available to standard processes.
- The project is distributed "as is", without warranties of any kind. Use it responsibly and in accordance with your organization's local security policies.

### Common Metrics (Linux & Windows)

These fields are collected across both operating systems:

- `OS`: Operating system family name (`Linux` or `Windows`).
- `Platform`: Detailed operating system platform and runtime string (e.g., glibc version on Linux or Service Pack build on Windows).
- `Release`: Operating system kernel or OS release version.
- `Core_Version`: Build revision of the underlying OS kernel.
- `Processor`: Processor architecture family or full processor identification string.
- `Architecture`: System bit depth and binary format (e.g., `["64bit", "ELF"]` or `["64bit", "WindowsPE"]`).
- `Username`: Username of the currently logged-in user running the script.
- `Machine_name`: Hostname of the target machine.

---

### Linux-Only Metrics

These fields are gathered exclusively in Linux environments:

- `Cpu_name`: Exact brand model name of the CPU (parsed from `/proc/cpuinfo` or `lscpu`).
- `Number_of_CPU_cores`: Total count of execution cores / logical threads.
- `Uptime`: System uptime in seconds elapsed since boot.
- `Total_memory`: Total installed physical RAM (in kB).
- `Free_memory`: Completely unused physical memory (in kB).
- `Available_memory`: Memory available for starting new applications without swapping (in kB).
- `VPN_connections`: Status indicator for active VPN interfaces/tunnels (or `null` if none detected).

---

### Windows-Only Metrics

These fields are gathered exclusively in Windows environments:

- `Disks`: Detailed breakdown of storage volumes (drive letter, total capacity in GB, used space in GB, and free space in GB).
- `MAC_address`: MAC address of the active physical network interface.
- `Network_info`: Primary local IPv4 address of the active connection.
- `Time`: Local system timestamp when the telemetry capture was executed (`YYYY-MM-DD HH:MM:SS`).
