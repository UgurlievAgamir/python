import re

pattern = r"^Рейс (\d+) (?:прибыл|отправился) (из|в) (\w+) в (\d{2}:\d{2}:\d{2})"

with open("data.txt", "r", encoding="utf-8") as data:
    with open("output.txt", "w", encoding="utf-8") as output:
        for line in data:
            res = re.search(pattern, line)
            if res:
                output.write(f"[{res.groups()[3]}] Поезд № {res.groups()[0]} {res.groups()[1]} {res.groups()[2]}\n")
