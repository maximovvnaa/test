import json   # Для работы с json файлами
import re     # Для работы с регулярными выражениями
from typing import List, Dict, Any

with open('auth.log') as file:
    logs = file.readlines()
pattern = r"(\w{3}\s\d{1,2}\s\d{2}:\d{2}:\d{2})\s(\w+)\ssshd\[\d+\]:\sFailed password for (\w+) from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*"
failed_passwords = []
for log in logs:
    result = re.match(pattern, log)
    if result:
        incident = {
            "Время": result.group(1),
            "Имя компа": result.group(2),
            "Имя пользователя": result.group(3),
            "IP адрес": result.group(4)
        }
        failed_passwords.append(incident)
        with open('venv/failed_password.json', 'w', encoding='UTF-8') as output_file:
            json.dump(failed_passwords, output_file, ensure_ascii=False, indent=4)
        print(result.groups())