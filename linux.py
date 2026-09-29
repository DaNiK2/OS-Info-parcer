import os

VPN_TYPES = {
    "tun",          
    "tap",          
    "wireguard",    
    "vpn",          
    "ppp",          
    "ipip", "gre",  
}

def linux_processor():
    processor = os.path.join("/", "proc", "cpuinfo")
    core_num = 0
    model = ""
    with open(processor, "r", encoding="utf-8") as f:
        for l in f:
            if l.startswith("model name"): #can have problems on ARM architecture of processors
                model = l.split(":")[-1]
            elif l.startswith("processor"):
                core_num += 1
    
    return [model, core_num]
    
def linux_uptime():
    net = os.path.join("/", "proc", "uptime")

    with open(net, "r", encoding="utf-8") as f:
        uptime = f.readline().split(" ")[0]

    return uptime

def linux_memory():
    mem = os.path.join("/", "proc", "meminfo")
    Total_mem = 0
    Free_mem = 0
    Available_mem = 0
    with open(mem, "r", encoding="utf-8") as f:
        for l in f:
            if "Total" in l and Total_mem == 0:
                Total_mem = l.split(":")[1].strip()
            elif "Free" in l and Free_mem == 0:
                Free_mem = l.split(":")[1].strip()
            elif "Available" in l and Available_mem == 0:
                Available_mem = l.split(":")[1].strip()
    return [Total_mem, Free_mem, Available_mem]

def get_vpn():
    net = os.path.join("/", "proc", "net", "dev")
    with open(net, "r", encoding="utf-8") as f:
        for l in f:
            tables = l.split(" ")
            vpn = any(vpntype in tables[0] for vpntype in VPN_TYPES)
            if vpn == True: return True
    
            
get_vpn()

def data_collector():
    collected_data = {}
    Cpu_name, core_num = linux_processor()
    collected_data["Cpu_name"] = Cpu_name
    collected_data["Number_of_CPU_cores"] = core_num
    collected_data["Uptime"] = linux_uptime()
    Total_mem, Free_mem, Available_mem = linux_memory()
    collected_data["Total_memory"] = Total_mem
    collected_data["Free_memory"] = Free_mem
    collected_data["Available_memory"] = Available_mem
    collected_data["VPN_connections"] = get_vpn()
    return collected_data 
