import numpy as np
import re
from pprint import pprint

# f = open("C:/Users/joep_/Documents/AdventOfCode/2022/10/input_small.txt", "r")
f = open("C:/Users/joep_/Documents/AdventOfCode/2022/10/input.txt", "r")
input = f.read().splitlines()

class Monkey:
    items: list
    divisible: function

    def __init__(self, items, operation, divisible_test, if_true, if_false):
        self.items = items
        self.operation = operation
        def test(number):
            if number % divisible_test == 0:
                return if_true
            else:
                return if_false
        self.divisible = test
        pass

def op0():
    

monkeys = [Monkey([54, 61, 97, 63, 74], )]
Monkey 0:
  Starting items: 
  Operation: new = old * 7
  Test: divisible by 17
    If true: throw to monkey 5
    If false: throw to monkey 3

Monkey 1:
  Starting items: 61, 70, 97, 64, 99, 83, 52, 87
  Operation: new = old + 8
  Test: divisible by 2
    If true: throw to monkey 7
    If false: throw to monkey 6

Monkey 2:
  Starting items: 60, 67, 80, 65
  Operation: new = old * 13
  Test: divisible by 5
    If true: throw to monkey 1
    If false: throw to monkey 6

Monkey 3:
  Starting items: 61, 70, 76, 69, 82, 56
  Operation: new = old + 7
  Test: divisible by 3
    If true: throw to monkey 5
    If false: throw to monkey 2

Monkey 4:
  Starting items: 79, 98
  Operation: new = old + 2
  Test: divisible by 7
    If true: throw to monkey 0
    If false: throw to monkey 3

Monkey 5:
  Starting items: 72, 79, 55
  Operation: new = old + 1
  Test: divisible by 13
    If true: throw to monkey 2
    If false: throw to monkey 1

Monkey 6:
  Starting items: 63
  Operation: new = old + 4
  Test: divisible by 19
    If true: throw to monkey 7
    If false: throw to monkey 4

Monkey 7:
  Starting items: 72, 51, 93, 63, 80, 86, 81
  Operation: new = old * old
  Test: divisible by 11
    If true: throw to monkey 0
    If false: throw to monkey 4


        
