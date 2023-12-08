from Matrix import Matrix
from utils.hooks import *
from Errors import *


class App:

    def __init__(self):
        self.MAXIMUM_MATRIX = 2
        self.last_error = False
        self.exit = False
        self.matrix: Matrix or None = None
        self.other: list[list[float]] or None = None

    def input_loop(self, init=True):
        matrix = []
        prev: list[float] or None = None
        user_input = input("Enter row (or 'done'): ")
        if user_input.lower() == "exit":
            self.exit = True
            user_input = "done"
        while user_input.lower() != "done":
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
            if user_input.lower() == "exit":
                self.exit = True
                user_input = "done"
        if init:
            self.matrix = Matrix(matrix)
        else:
            self.other = matrix
        print(f"Finished building matrix.")

    def check_action(self, inp: str):
        if self.other is None:
            match inp:
                case "det":
                    self.matrix.determinant()
                case "trans":
                    self.matrix.transpose()
                case "invert":
                    self.matrix.invert()
                case "add":
                    self.input_loop(False)
                case "exit":
                    self.exit = True
                case "restart":
                    print("Restart initialized")
                    self.input_loop()
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
                    self.exit = True
                case "restart":
                    print("Restart initialized")
                    self.other = None
                    self.input_loop()
                case "back":
                    self.other = None
                case _:
                    print(f"The input <{inp}> has no functionality."
                          f" Please try again")

    def main_loop(self):
        print("=======================================")
        print("What do you want to do?")
        print("\tDeterminant: 'det'\n\tTranspose: 'trans'\n\t"
              "Invert: 'invert'\n\tAdd other matrix: 'add'"
              "\n\tRestart: 'restart'"
              "\n\tExit: 'exit'") \
            if self.other is None else print("\n\t"
                                             "Back to main matrix: 'back'\n\t"
                                             "Addition: 'madd'\n\t"
                                             "Subtraction: 'sub'\n\t"
                                             "Dot product: 'dot'\n\t"
                                             "Cross product: 'cross'\n\t"
                                             "Exit: 'exit'\n\t"
                                             "Restart: 'restart'")
        print("=======================================")
        user_input = input("Matrix Calc > ")
        self.check_action(user_input.lower())



