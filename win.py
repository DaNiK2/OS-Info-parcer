import platform
import json
import subprocess
import linux
import getpass
from win import get_win_inf

parametrs = {
        "OS": platform.system(),
        "Platform": platform.platform(),
        "Release": platform.release(),
        "Core_Version": platform.version(),
        "Processor": platform.processor(),
        "Architecture": platform.architecture(),
        "Username": getpass.getuser(),
        "Network_name": platform.node(),
    }

if parametrs["OS"] == "Windows":
    parametrs.update(get_win_inf())


elif parametrs["OS"] == "Linux":
    parametrs["Processes"] = subprocess.check_output("ps", text = True)
    Cpu_name, core_num = linux.linux_processor()
    parametrs["Cpu_name"] = Cpu_name
    parametrs["Number of CPU cores"] = core_num
    parametrs["Uptime"] = linux.linux_uptime()
    Total_mem, Free_mem, Available_mem = linux.linux_memory()
    parametrs["Total memory"] = Total_mem
    parametrs["Free memory"] = Free_mem
    parametrs["Available memory"] = Available_mem




with open("output.json", "w", encoding="utf-8") as file:
    json.dump(parametrs, file, ensure_ascii=False, indent=5)
