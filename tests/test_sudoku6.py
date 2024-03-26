import os
import subprocess
import sys
import unittest
import json

INSTANCES = "./instances/txt"
SOLUTIONS = "./solutions/q04"


def parse_answers(text):
    is_model = False
    answers = []
    answer = []
    for line in text.strip().splitlines():
        if line == "":
            continue
        if is_model and len(answer) < 9:
            answer.append(line)
        if is_model and len(answer) >= 9:
            answers.append(tuple(answer))
            is_model = False
        if line.startswith("Answer:"):
            is_model = True
            answer = []
    return set(answers)


def get_answer(command_line, sorted=True):
    return parse_answers(subprocess.check_output(command_line).decode("utf-8"))


def get_solutions(file_name):
    with open(f"{SOLUTIONS}/{file_name}.txt") as f:
        solutions = parse_answers(f.read())
    return solutions


class TestSudoku(unittest.TestCase):
    def test_sudoku(self):
        for file in os.listdir(INSTANCES):
            file_name = os.path.splitext(os.path.basename(file))[0]
            output = get_answer([sys.executable, "-u", "sudoku6.py", f"{INSTANCES}/{file}"])
            solutions = get_solutions(file_name)
            self.assertEqual(len(output), 1, file_name)
            for answer in output:
                self.assertIn(answer, solutions, file_name)
