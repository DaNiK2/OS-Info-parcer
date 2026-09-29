import datetime
import socket
import uuid
import shutil


def get_network_info():
    try:
        ip_local = socket.gethostbyname(socket.gethostname())
    except socket.gaierror:
        ip_local = "unknown"

    return ip_local

def get_mac_address():
    mac_int = uuid.getnode()
    mac_hex = ':'.join(['{:02x}'.format((mac_int >> i) & 0xff)
                        for i in range(0, 48, 8)][::-1])
    return mac_hex

def get_disks_windows():
    import string
    disks = []
    for letter in string.ascii_uppercase:
        path = f"{letter}:\\"
        try:
            usage = shutil.disk_usage(path)
            disks.append({
                "letter": path,
                "total_gb": round(usage.total / (1024 ** 3), 1),
                "used_gb": round(usage.used / (1024 ** 3), 1),
                "free_gb": round(usage.free / (1024 ** 3), 1)
            })
        except (FileNotFoundError, PermissionError, OSError):
            continue
    return disks

def get_win_inf():
    parametrs_win = {
        "Disks": get_disks_windows(),
        "MAC_address": get_mac_address(),
        "Network_info": get_network_info(),
        "Time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    }
    return parametrs_win
