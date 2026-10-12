import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Final

MAX_SIZE: Final = 100
PASSING_GRADE: Final = 4.0


@dataclass
class Item:
    title: str
    price: float
    tags: list[str] = field(default_factory=list[str])


class Student:
    def __init__(self, name: str, grades: list[int]) -> None:
        self.name = name
        self.grades = grades
        self.total: int = 0

    def average(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def get_name(self) -> str:
        return self.name

    def find_grade(self, value: int) -> int | None:
        for grade in self.grades:
            if grade == value:
                return grade
        return None


class Graduate(Student):
    def label(self, extra: int) -> str:
        if self.average() + extra >= PASSING_GRADE:
            return "high"
        return "low"


def multiply_all(values: list[int], factor: int) -> list[int]:
    return [value * factor for value in values]


def add_numbers(a: int, b: int) -> int:
    return a + b


def add_strings(a: str, b: str) -> str:
    return a + b


def find_item(items: list[Item], title: str) -> Item | None:
    for item in items:
        if item.title == title:
            return item
    return None


def total_price(items: list[Item]) -> float:
    return sum(item.price for item in items)


def read_config(path: str) -> dict[str, str]:
    with Path(path).open(encoding="utf-8") as file:
        data: dict[str, str] = json.load(file)
    return data


def process(data: dict[str, int]) -> int:
    value = data.get("key")
    if value is None:
        return 0
    return value.bit_length()


def double(number: int) -> int:
    return number * 2


def main() -> None:
    student = Student("Ivan", [5, 4, 5])
    print(student.average())
    print(student.get_name().upper())

    grade = student.find_grade(5)
    if grade is not None:
        print(grade + 1)

    print(multiply_all([1, 2, 3], 2))
    print(add_numbers(1, 2))
    print(add_strings("1", "2"))

    items = [Item("pen", 1.5, ["a"]), Item("book", 10.0)]
    found = find_item(items, "pen")
    if found is not None:
        print(found.title.upper())
        found.tags.append("x")
    print(total_price(items))

    try:
        print(read_config("config.json"))
    except (OSError, json.JSONDecodeError):
        print("config not found")

    print(process({"key": 5}))
    print(double(3))

    graduate = Graduate("Petr", [4, 5])
    print(graduate.label(1))

    if student.name == "Ivan":
        print("match")


if __name__ == "__main__":
    main()
