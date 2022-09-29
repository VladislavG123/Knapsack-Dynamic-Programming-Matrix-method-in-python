input_str = input("Input sizes in this format (5,10,20,5): ")
sizes = [int(i) for i in input_str.split(',')]

input_str = input("Input values in this format (5,10,20,5): ")
values = [int(i) for i in input_str.split(',')]

capacity = int(input("Input capacity: "))

matrix = []


# 3,5,7,8,9
# 4,6,7,9,10
# 22

def validate():
    if len(sizes) != len(values):
        return False
    if capacity <= 0:
        return False
    return True


def main():
    if not validate():
        print('Validation problem')
        return
    for i in range(len(sizes) + 1):
        w_row = []
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                w_row.append(0)
                continue
            w_row.append(calculate_item(i, w))
        matrix.append(w_row)

    for c in matrix:
        for item in c:
            print(f"{'' if item >= 10 else ' '}{item}", end=' ')
        print()


def calculate_item(i, w):
    a = matrix[i - 1][w]

    row_index = w - sizes[i - 1]
    if row_index < 0:
        return a

    b = matrix[i - 1][row_index] + values[i - 1]

    if a == b:
        return a

    return a if a > b else b


if __name__ == "__main__":
    main()
