from Matrix import Matrix
from utils.hooks import *
from Errors import *
import os


class App:

    def __init__(self):
        self.MAXIMUM_MATRIX = 2
        self.last_error = False
        self.matrix: Matrix or None = None
        self.other: list[list[float]] or None = None

    def input_loop(self, init=True):
        help_setup()
        matrix = []
        prev: list[float] or None = None

        user_input = input("Enter row (or 'done'): ")
        while user_input.lower() != "done":
            if user_input.lower() == "exit":
                exit(1)
            try:
                row = list_from_string(user_input)
                if isinstance(prev, list):
                    if len(prev) != len(row):
                        raise LengthError
                matrix.append(row)
                prev = row
            except LengthError:
                print("The length of the row does "
                      "not match the previous row(s). Try again")
            except ValueError:
                print("One of the elements of the row was not an integer."
                      " Try again")
                self.last_error = "ValueError"
            user_input = input("Enter row (or 'done'): ")

        if init:
            self.matrix = Matrix(matrix)
        else:
            self.other = matrix
        print(f"Finished building matrix.")

    def check_action(self, inp: str):
        if self.other is None:
            match inp:
                case "create":
                    self.input_loop()
                case "det":
                    self.matrix.determinant()
                case "trans":
                    self.matrix.transpose()
                case "invert":
                    self.matrix.invert()
                case "add":
                    if self.matrix is None:
                        print("Initialise the main matrix first using "
                              "< create > command.")
                    else:
                        self.input_loop(False)
                case "exit":
                    exit(1)
                case "clear":
                    if os.name == "nt":
                        os.system('cls')
                    else:
                        os.system('clear')
                case "restart":
                    print("Restart initialized")
                    self.input_loop()
                case "help":
                    cmd_help(self.other)
                case _:
                    print(f"The input <{inp}> has no functionality in "
                          f"the current state."
                          f" Please try again")
        else:
            match inp:
                case "madd":
                    self.matrix.addition(self.other)
                case "sub":
                    self.matrix.subtraction(self.other)
                case "dot":
                    self.matrix.dot_product(self.other)
                case "cross":
                    self.matrix.cross_product(self.other)
                case "exit":
                    exit(1)
                case "restart":
                    print("Restart initialized")
                    self.other = None
                    self.input_loop()
                case "back":
                    self.other = None
                case "help":
                    cmd_help(self.other)
                case "clear":
                    if os.name == "nt":
                        os.system('cls')
                    else:
                        os.system('clear')
                case _:
                    print(f"The input <{inp}> has no functionality."
                          f" Please try again")

    def main_loop(self):
        user_input = input("Matrix Calc > ")
        self.check_action(user_input.lower())



