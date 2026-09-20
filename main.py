import platform
import json
import subprocess
import linux


parametrs = {
    "OS" : platform.system(),
    "OS_Version" : platform.release(),
    "Core_Version" : platform.version(),
    "Machine" : platform.machine(),
    "Processor" : platform.processor(),
    "Network_name" : platform.node()
    }

if parametrs["OS"] == "Windows":
    parametrs["Processes"] = subprocess.check_output("tasklist", text = True)

elif parametrs["OS"] == "Linux":
    parametrs["Processes"] = subprocess.check_output("ps", text = True)
    Cpu_name, core_num = linux.linux_parser()
    parametrs["Cpu_name"] = Cpu_name
    parametrs["Number of CPU cores"] = core_num



with open("output.json", "w", encoding="utf-8") as file:
    json.dump(parametrs, file, ensure_ascii=False, indent=5)