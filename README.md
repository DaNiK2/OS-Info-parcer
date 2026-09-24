# OS-Info-parcer
In this repository you can find python code that takes info about system, where he was started, and parce it in .json

## ⚠️ Disclaimer

This repository is an **educational project** developed solely for academic, learning, and research purposes. 

- The software contains **no malicious code**, backdoors, or telemetry intended for unauthorized data harvesting.
- It operates strictly within user space to read public system metrics and hardware parameters available to standard processes.
- The project is distributed "as is", without warranties of any kind. Use it responsibly and in accordance with your organization's local security policies.

## 📊 Output Data Structure

### 🖥️ Operating System & Host Platform
- `OS` — Operating system family name.
- `OS_Version` — Operating system kernel release/version.
- `Core_Version` — Full kernel build information, including compiler details, build timestamp, and distribution specifics.
- `Machine` — Hardware platform architecture.
- `Processor` — CPU architecture family.
- `Machine_name` — Network hostname of the device.
- `Uptime` — System uptime elapsed since last boot (in seconds).

### ⚙️ CPU & Processes
- `Cpu_name` — Model name and brand string of the central processor.
- `Number_of_CPU_cores` — Total count of logical/physical CPU execution cores.
- `Processes` — Snapshot listing currently running processes.

### 🧠 Memory
- `Total_memory` — Total amount of installed physical RAM.
- `Free_memory` — Amount of completely unused physical memory.
- `Available_memory` — Estimated memory available for starting new applications without swapping.

### 🌐 Network
- `Network_name` — Identifier/SSID of the active network connection.
- `VPN_connections` — Boolean indicator signaling whether an active VPN interface or tunnel is detected.
