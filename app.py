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
                case "switch":
                    temp = self.matrix
                    self.matrix = self.other
                    self.other = temp
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

    def check_tokens(self, tokens: list[str]):
        tokens.reverse()
        tok = tokens.pop()
        match tok:
            case "show":
                if len(tokens) > 1:
                    print("ERR: Too many flags with the < show > command.")
                else:
                    flag = tokens.pop()
                    if (flag == "m" or flag == "-m") and self.matrix is not None:
                        print(f"\nThe main matrix is\n{to_string(self.matrix)}\n")
                    elif (flag == "o" or flag == "-o") and self.other is not None:
                        print(f"\nThe main matrix is\n{to_string(self.other)}\n")
                    elif (flag == "b" or flag == "-b") and self.other is not None and self.matrix is not None:
                        print(f"\nThe main and the other matrix "
                              f"are\n{side_by_side_string(self.matrix, self.other)}")
                    else:
                        print("ERR: Wrong flags for < show > or no matrices initialized.")
            case _:
                print(f"The flag <{tok}> has no functionality."
                      f" Please try again")

    def main_loop(self):
        user_input = input("Matrix Calc > ")
        tokens = user_input.split()
        if len(tokens) == 1:
            self.check_action(user_input.lower())
        else:
            self.check_tokens(tokens)



