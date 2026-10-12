import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from bad_code import Item, Student, add_numbers, find_item, process, total_price


def test_add_numbers() -> None:
    assert add_numbers(2, 3) == 5


def test_student_average() -> None:
    assert Student("Ivan", [5, 4, 3]).average() == 4.0


def test_student_average_empty() -> None:
    assert Student("Ivan", []).average() == 0.0


def test_find_item() -> None:
    items = [Item("pen", 1.5), Item("book", 10.0)]
    found = find_item(items, "pen")
    assert found is not None
    assert found.title == "pen"
    assert find_item(items, "missing") is None


def test_total_price() -> None:
    assert total_price([Item("a", 1.0), Item("b", 2.5)]) == 3.5


def test_process() -> None:
    assert process({"key": 5}) == 3
    assert process({}) == 0
