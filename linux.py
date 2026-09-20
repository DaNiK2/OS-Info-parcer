import os

def linux_parser(): #this func return cpu_info in linux systems 
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
    