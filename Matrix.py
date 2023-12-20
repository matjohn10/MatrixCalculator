import numpy as np
from utils.hooks import *


class Matrix:
    def __init__(self, matrix: list[list[float]]):
        self.matrix = matrix

    def to_string(self):
        if len(self.matrix) == 0:
            return "[]"
        final = f'[\n\t{self.matrix[0]}'
        for i in range(1, len(self.matrix)):
            final += f',\n\t{self.matrix[i]}'
        return final + ",\n]"

    def properties(self):
        if len(self.matrix) == 0:
            return "Empty"
        return f'{len(self.matrix)}x{len(self.matrix[0])}'

    def transpose(self):
        x = np.array(self.matrix)
        t = x.T
        print(
            f"\nThe transpose of\n{side_by_side_string(self.matrix, t, ' is')}")

    def determinant(self):
        if len(self.matrix) > 0 and len(self.matrix) == len(self.matrix[0]):
            x = np.array(self.matrix)
            d = np.linalg.det(x)
            print(f"\nThe determinant of\n{to_string(self.matrix)} "
                  f" is {round(d, 2)}")
        elif len(self.matrix) == 0:
            print("\nThe determinant cannot be"
                  " calculated as the matrix is empty.\n")
        else:
            print("\nThe matrix is not square.\n")

    def invert(self):
        if len(self.matrix) > 0 and len(self.matrix) == len(self.matrix[0]):
            x = np.array(self.matrix)
            try:
                i = np.linalg.inv(x)
                print(
                    f"\nThe inverse of\n{side_by_side_string(self.matrix, i, ' is the following: ')}")
            except np.linalg.LinAlgError:
                print(f"\nThe matrix\n{to_string(self.matrix)}\n"
                      " does not have an invert.\n")
        elif len(self.matrix) == 0:
            print(
                "\nThe inverse cannot be calculated as the matrix is empty.\n")
        else:
            print("\nThe matrix is not square.\n")

    def addition(self, other: list[list[float]]):
        if 0 < len(self.matrix) == len(other) > 0 and \
                len(self.matrix[0]) == len(other[0]):
            x = np.array(self.matrix)
            y = np.array(other)

            d = list(np.add(x, y))
            print(f"\nThe addition"
                  f" of\n{side_by_side_string(self.matrix, other, ' and ')}\n"
                  f"is the following:\n"
                  f"\n{to_string(d)}\n")

        elif len(self.matrix) == 0 or len(other) == 0:
            print("\nThe addition cannot be calculated with an empty matrix\n")
        else:
            print("\nAddition error\n")

    def subtraction(self, other: list[list[float]]):
        if 0 < len(self.matrix) == len(other) > 0 and \
                len(self.matrix[0]) == len(other[0]):
            x = np.array(self.matrix)
            y = np.array(other)

            d = list(np.subtract(x, y))
            print(f"\nThe subtraction of"
                  f"\n{side_by_side_string(self.matrix, other, ' and ')}\n"
                  f"is the following:\n"
                  f"\n{to_string(d)}\n")

        elif len(self.matrix) == 0 or len(other) == 0:
            print("\nThe subtraction cannot"
                  " be calculated with an empty matrix.\n")
        else:
            print("\nSubtraction error\n")

    def dot_product(self, other: list[list[float]]):
        x = np.array(self.matrix)
        y = np.array(other)
        try:
            d = list(np.dot(x, y))
            print(f"\nThe dot product of"
                  f"\n{side_by_side_string(self.matrix, other, ' and ')}\n"
                  f"is the following:\n"
                  f"\n{to_string(d)}\n")
        except ValueError:
            print(f"\nThe shape of matrix A ({self.properties()}) does "
                  f"not allow\na dot product with the shape of matrix B "
                  f"({len(other)}x{len(other[0])}).\n")

    def cross_product(self, other: list[list[float]]):
        x = np.array(self.matrix)
        y = np.array(other)
        try:
            d = list(np.cross(x, y))
            print(f"\nThe cross product of"
                  f"\n{side_by_side_string(self.matrix, other, ' and ')}\n"
                  f"is the following:\n"
                  f"\n{to_string(d)}\n")
        except ValueError:
            print(f"\nThe dimensions of the vectors do not allow cross product "
                  f"calculations.\n")


if __name__ == "__main__":
    c1 = [1, 2, 3, 4]
    c2 = [3, 6, 8, 0]
    c3 = [5, 3, 8, 4]
    m = Matrix([c1, c2, c3])
    print(m.to_string())
