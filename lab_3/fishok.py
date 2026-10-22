import requests
import re

r = requests.get("https://www.fish-ok.ru/catalog/kryuchki/kryuchki_cpinningiovye_flagman/", timeout=30)

with open("catalog.html", "w", encoding="utf-8") as file:
    file.write(r.text)

pattern = (r'<a\s+href="(/catalog/kryuchki/kryuchki_cpinningiovye_flagman/[0-9]+/)"'
    r'\s*>\s*<span>([^<]+)</span>\s*</a>'
    r'.*?<span\s+class="value">([^<]+)</span>')
hooks = re.findall(pattern, r.text, flags=re.DOTALL)

for link, name, item_value in hooks:
    print(name.strip())
    print(link)
    print(item_value)
    print()