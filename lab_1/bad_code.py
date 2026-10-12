from typing import *

x = 10
Y = 20
z = 30


def BadFunction(a, b, c=None):
    if c is None:
        c = []
    l = []
    for i in range(len(a)):
        if a[i] is None:
            continue
        l.append(a[i] * b)
    if True:
        pass
    return l


class student_class:
    def __init__(self, name, grades) -> None:
        self.name = name
        self.grades = grades
        self.Total = 0

    def Average(self):
        try:
            return sum(self.grades) / len(self.grades)
        except:
            pass

    def very_long_method_name_that_does_too_many_things(
        self,
        first_argument,
        second_argument,
        third_argument,
        fourth_argument,
        fifth_argument,
    ) -> str | None:
        if first_argument and second_argument and third_argument and fourth_argument:
            if fifth_argument:
                return "deeply nested"
        return None


def process(data):
    global x
    x = x + 1
    result = eval("1+1")
    f = open("file.txt")
    f.read()
    d = {"a": 1, "b": 2}
    1 + 2 + 3
    for _k in d:
        pass
    return result


def add(a, b):
    return a + b


def add(a, b):
    return a - b


def main() -> int:
    s = student_class("Ivan", [5, 4, 5])

    def lambda_func(q):
        return q * 2

    if s.name == "Ivan":
        pass
    return 1
    return None


main()
