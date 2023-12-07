import os
from aocd.models import Puzzle
from aocd import submit
from pprint import pprint 

os.environ['AOC_SESSION'] = '53616c7465645f5f5274298a1513bd33b311098204a4e371d2880a4590e8a95748ea42877f6b28b349045dcc1fee6d10f00932890ec53d2fdfe8a068bae08242'

year=2023
day=7

puzzle = Puzzle(year=year, day=day)
input = puzzle.input_data.splitlines()

scores={
    0: 0,
    1: 0,
    2: 1, #two of a kind
    3: 3, #three of a kind
    4: 5, #four of a kind
    5: 6  #five of a kind
}
# 2 pair = 1+1=2, full house = 3+1=5

card_values={
    "1":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "T":10,
    "J":11,
    "Q":12,
    "K":13,
    "A":14
}

class Hand:
    cards: str
    bid: int
    score1: int
    score2: int
    card_int1: int
    card_int2: int

    def __init__(self, cards: str, bid: str):
        self.cards=cards
        self.bid=int(bid)
        self.score1=0
        self.score2=0
        self.card_int1=0
        self.card_int2=0
        pass

    def get_score1(self):
        card_amounts = dict()
        for c in self.cards:
            try:
                card_amounts[c]+=1
            except:
                card_amounts[c]=1
        for c, count in card_amounts.items():
            self.score1+=scores[count]
        return
    
    def get_score2(self):
        card_amounts = dict()
        for c in self.cards:
            try:
                card_amounts[c]+=1
            except:
                card_amounts[c]=1
        jokers_left=card_amounts.pop("J", 0)
        for c, count in card_amounts.items():
            if count==max(card_amounts.values()):
                self.score2+=scores[count+jokers_left]
                jokers_left=0
            else:
                self.score2+=scores[count]
        self.score2+=scores[jokers_left]
        return
    
    def calc_card_int1(self):
        for i,c in enumerate(self.cards[::-1]):
            self.card_int1+=card_values[c]*15**i
        return
    
    def calc_card_int2(self):
        for i,c in enumerate(self.cards[::-1]):
            if c=="J":
                continue
            self.card_int2+=card_values[c]*15**i
        return

hands = []
for line in input:
    values = line.split(" ")
    hand = Hand(values[0], values[1])
    hand.get_score1()
    hand.get_score2()
    hand.calc_card_int1()
    hand.calc_card_int2()
    hands.append(hand)

hands.sort(key=lambda x: (15**5)*x.score1+ x.card_int1)
sol1=sum(i*hand.bid for i, hand in enumerate(hands, start=1))
submit(sol1, part=1, year=year, day=day)

hands.sort(key=lambda x: (15**5)*x.score2+ x.card_int2)
sol2=sum(i*hand.bid for i, hand in enumerate(hands, start=1))
submit(sol2, part=2, year=year, day=day)
