from aocd.models import Puzzle
from aocd import submit
from pprint import pprint
from typing import List, Tuple, Dict, Any

def get_input(year=2024, day=1, example=False):
    puzzle = Puzzle(year,day)
    if example:
        return puzzle.examples[0].input_data
    return puzzle.input_data

def int_to_bin_list(A_int):
    A_bin = list()
    count = 1
    while True:
        if A_int == 0:
            break
        if A_int%(2*count) == 0:
            A_bin.append(0)
        else:
            A_bin.append(1)
            A_int -= count
        count *= 2
    return A_bin

def bin_list_to_int(A_bin):
    A_int = 0
    for i, bit in enumerate(A_bin):
        A_int += bit*(2**i)
    return A_int

class Gate():
    type: str
    inputs: tuple
    input_values: list
    next_id: str
    output_value: bool


    def __init__(self, inputstring: str) -> None:
        tmp = inputstring.split(" ")
        self.inputs = (tmp[0], tmp[2])
        self.input_values = [None, None]
        self.type = tmp[1]
        self.next_id = tmp[-1]
        self.output_value = None
        pass

    def get_output(self):
        if self.input_values[0] is None or self.input_values[1] is None:
            self.output_value = None
            return None
        if self.type == "AND":
            self.output_value = self.input_values[0] and self.input_values[1]
        if self.type == "OR":
            self.output_value = self.input_values[0] or self.input_values[1]
        if self.type == "XOR":
            self.output_value = not self.input_values[0] == self.input_values[1]
        return self.output_value


def parse_input(input):
    start_signals, gates = tuple(j for j in input.split("\n\n"))
    start_signals = {i.split(": ")[0]: bool(int(i.split(": ")[1])) for i in start_signals.split("\n")}
    gates = [Gate(i) for i in gates.split("\n")]
    return start_signals, gates

def number_to_signals(prefix: str, number: int, min_length: int):
    bin_list = int_to_bin_list(number)
    while len(bin_list) < min_length:
        bin_list.append(0)
    signals = dict()
    for i, bit in enumerate(bin_list):
        signals[prefix+("0"+ str(i) if i<= 9 else str(i))] = bool(bit)
    return signals

def signal_first_bits(prefix: str, bit_nr: int):
    bin_list = []
    while len(bin_list) < bit_nr:
        bin_list.append(0)
    signals = dict()
    for i, bit in enumerate(bin_list):
        signals[prefix+("0"+ str(i) if i<= 9 else str(i))] = bool(bit)
    return signals

def signals_to_number(signals: dict):
    bit_list = []
    counter = 0
    while True:
        try:
            bit_list.append(signals["z"+("0"+ str(counter) if counter<= 9 else str(counter))])
            counter += 1
        except:
            break
    return bin_list_to_int(bit_list)

def update_gates(gates: List[Gate], signals: dict):
    for gate in gates:
        if gate.output_value is not None:
            continue
        if gate.inputs[0] in signals:
            gate.input_values[0] = signals[gate.inputs[0]]
        if gate.inputs[1] in signals:
            gate.input_values[1] = signals[gate.inputs[1]]
        res = gate.get_output()
        if res is not None:
            signals[gate.next_id] = res
    return gates, signals

def evaluate_signals(signals: dict, gates: List[Gate]):
    prev_signal_length = 0
    while prev_signal_length != len(signals):
        prev_signal_length = len(signals)
        gates, signals = update_gates(gates, signals)
    return signals

if __name__ == "__main__":
    year = 2024
    day = 24

    input = get_input(year=year, day=day, example=False)
    signals, gates = parse_input(input)
    signals = evaluate_signals(signals, gates)

    answer1 = signals_to_number(signals)
    submit(answer1, part="a", day=day, year=year)


    signals, gates = parse_input(input)
    for i in range(len(signals)//2):
        signals = signal_first_bits("x", i) | signal_first_bits("y", i)
        pprint(signals)
        quit()
        signals = evaluate_signals(signals, gates)
        if signals_to_number(signals) != 2**i+1:
            print(signals_to_number(signals), 2**i+1)
            # pprint("wrong")
        # else:
            # pprint("right")

    # distances = get_distances(walls, start, end)

    # cheat_dists = get_cheats(distances, 2)
    # answer1 = sum(amount for dist, amount in cheat_dists.items() if dist >= 100)


    # cheat_dists = get_cheats(distances, 20)
    # answer2 = sum(amount for dist, amount in cheat_dists.items() if dist >= 100)
    # submit(answer2, part="b", day=day, year=year)

