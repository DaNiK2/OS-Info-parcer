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
        "Machine_name": platform.node(),
    }

if parametrs["OS"] == "Windows":
    parametrs.update(get_win_inf())


elif parametrs["OS"] == "Linux":
    parametrs.update(linux.data_collector())




with open("output.json", "w", encoding="utf-8") as file:
    json.dump(parametrs, file, ensure_ascii=False, indent=5)
