import json
import re
with open('failed_password.json') as file:
    data = json.load(file)
count = len(data)
print("Количество инцидентов:", count)