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
    "Machine_name" : platform.node()
    }

if parametrs["OS"] == "Windows":
    parametrs["Processes"] = subprocess.check_output("tasklist", text = True)

elif parametrs["OS"] == "Linux":
    parametrs.update(linux.data_collector())




with open("output.json", "w", encoding="utf-8") as file:
    json.dump(parametrs, file, ensure_ascii=False, indent=5)