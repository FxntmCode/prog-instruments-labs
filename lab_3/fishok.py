import csv
import re
from urllib.parse import urljoin

import requests


BASE_URL = "https://www.fish-ok.ru"
CATALOG_URL = (
    f"{BASE_URL}/catalog/kryuchki/"
    "kryuchki_cpinningiovye_flagman/"
)

WOBBLERS_URL = f"{BASE_URL}/catalog/voblery/voblery_popery/"

HOOK_PATTERN = re.compile(
    r'<a\s+href="'
    r'(/catalog/kryuchki/kryuchki_cpinningiovye_flagman/[0-9]+/)"'
    r'\s*>\s*<span>([^<]+)</span>\s*</a>'
    r'.*?<span\s+class="value">([^<]+)</span>',
    flags=re.DOTALL,
)

def download_html(url: str, params: dict | None = None) -> str:
    """Скачивает HTML"""
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    return response.text


def save_html(html: str, filename: str) -> None:
    """Сохраняет HTML"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(html)


def parse_hooks(html: str) -> list[tuple[str, str, str]]:
    """Извлекает  название"""
    matches = HOOK_PATTERN.findall(html)

    return [
        (
            name.strip(),
            urljoin(BASE_URL, link),
            item_value.strip(),
        )
        for link, name, item_value in matches
    ]


def save_to_csv(
    hooks: list[tuple[str, str, str]],
    filename: str,
) -> None:
    """Сохраняет крючки в CSV"""
    with open(filename, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["Название", "Ссылка", "Наличие"])
        writer.writerows(hooks)


def main() -> None:
    html = download_html(CATALOG_URL)
    save_html(html, "catalog.html")

    hooks = parse_hooks(html)

    if not hooks:
        print("Товары не найдены. Проверьте сохранённый HTML.")
        return

    save_to_csv(hooks, "hooks.csv")

    for name, link, item_value in hooks:
        print(name)
        print(link)
        print(item_value)
        print()

    print(f"Сохранено товаров: {len(hooks)}")


if __name__ == "__main__":
    main()