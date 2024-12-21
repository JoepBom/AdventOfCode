from aocd.models import Puzzle
from aocd import submit

year=2024
day=5
puzzle = Puzzle(year,day)

rules = puzzle.input_data.split("\n\n")[0].splitlines()
books = puzzle.input_data.split("\n\n")[1].splitlines()

def order_pages(pages):
    for rule in rules:
        first, second = rule.split("|")[0], rule.split("|")[1]
        if first in pages and second in pages:
            if pages.index(first) > pages.index(second):
                pages[pages.index(first)], pages[pages.index(second)] = pages[pages.index(second)], pages[pages.index(first)]
                return order_pages(pages)
    return pages   

answer1 = 0
answer2 = 0
for book in books:
    pages = book.split(",")
    good=True
    for rule in rules:
        if rule.split("|")[0] in pages and rule.split("|")[1] in pages:
            if pages.index(rule.split("|")[0]) > pages.index(rule.split("|")[1]):
                good=False
                pages = order_pages(pages)
                break
    if good:
        answer1+=int(pages[int(len(pages)/2)])
    if not good:
        answer2+=int(pages[int(len(pages)/2)])

submit(answer1, part="a", day=day, year=year)
submit(answer2, part="b", day=day, year=year)