def to_string(matrix: list[list[int]]):
    if len(matrix) == 0:
        return "[]"
    final = f'[\n\t{matrix[0]}'
    for i in range(1, len(matrix)):
        final += f',\n\t{matrix[i]}'
    return final + ",\n]"


def list_from_string(list_str: str) -> list[float]:
    if "," in list_str:
        return [float(s_num) for s_num in list_str.split(", ")]
    else:
        return [float(s_num) for s_num in list_str.split()]


def help_setup():
    print("\t==========================================================")
    print("\t\tPlease enter your matrix row by row.")
    print("\t\tMake sure each row has the same number of elements.")
    print("\t\tFollow the following formats:")
    print("\t\tFormat 1:\n\t\t\tEnter row: 1, 2, 3, 4\n\n\t\tFormat 2:\n"
          "\t\t\tEnter row: 1 2 3 4\n")
    print("\t\tWhen done, input 'done'. (Not case sensitive)")
    print("\t==========================================================")
