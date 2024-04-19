import json
import re
ports=[]
count=0
with open("auth.log") as file:
    logs = file.readlines()
for log in logs:
    result = re.findall(r"port \d+", log)
    if result:
        if result not in ports:
            count +=1
            ports.append(result)
print("Количество инцидентов:",(count))