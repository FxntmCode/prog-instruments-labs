import requests
import re
import csv

r = requests.get("https://www.fish-ok.ru/catalog/kryuchki/kryuchki_cpinningiovye_flagman/", timeout=30)

with open("catalog.html", "w", encoding="utf-8") as file:
    file.write(r.text)

pattern = (r'<a\s+href="(/catalog/kryuchki/kryuchki_cpinningiovye_flagman/[0-9]+/)"'
    r'\s*>\s*<span>([^<]+)</span>\s*</a>'
    r'.*?<span\s+class="value">([^<]+)</span>')
hooks = re.findall(pattern, r.text, flags=re.DOTALL)

with open("hooks.csv", "w", encoding="utf-8-sig", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(["Название", "Ссылка", "Наличие"])

    for link, name, item_value in hooks:
        writer.writerow([
            name.strip(),
            "https://www.fish-ok.ru" + link,
            item_value.strip(),
        ])

for link, name, item_value in hooks:
    print(name.strip())
    print(link)
    print(item_value)
    print()