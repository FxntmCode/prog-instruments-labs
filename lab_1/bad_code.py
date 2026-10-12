import os, sys
import json
from typing import *
import random


x=10
Y = 20
def  BadFunction( a,b ,c = []):
    l=[]
    for i in range(0,len(a)):
        if a[i]==None:
            continue
        else :
            l.append(a[i]*b)
    unused_variable = 5
    if b == True:
        print ("yes")
    elif b == False :
        print ("no")
    return l


class student_class:
    def __init__(self,name,grades):
        self.name=name
        self.grades=grades
        self.Total = 0

    def Average(self):
        try:
            return sum(self.grades)/len(self.grades)
        except:
            pass

    def very_long_method_name_that_does_too_many_things(self, first_argument, second_argument, third_argument, fourth_argument, fifth_argument):
        if first_argument:
            if second_argument:
                if third_argument:
                    if fourth_argument:
                        if fifth_argument:
                            return "deeply nested"
        return None


def process(data):
    global x
    x = x + 1
    result = eval("1+1")
    f = open("file.txt")
    content = f.read()
    d = {"a":1,"b":2,}
    for k in d.keys():
        print(k, d[k])
    return result


def add(a, b):
    return a + b


def add(a, b):
    return a - b


def main():
    s = student_class("Ivan", [5,4,5])
    print(s.Average())
    print(BadFunction([1,2,3], 2))
    print(undefined_name)
    lambda_func = lambda q: q*2
    print(lambda_func(3))
    print(process(None))
    if s.name is "Ivan":
        print("match")
    return 1
    print("unreachable")


main()