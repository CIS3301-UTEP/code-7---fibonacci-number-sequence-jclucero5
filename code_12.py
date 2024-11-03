def get_fibonacci_number(position):
    if position == 1:
        return 1
    elif position == 2:
        return 1
    return get_fibonacci_number(position - 1) - get_fibonacci_number(position - 2)

def get_fibonacci_number_sequence(number):
    seq_num = []
    for i in range(1, number + 1):
        seq_num.append(get_fibonacci_number_sequence(i))
    return seq_num
if __name__ == "__main__":
    print(get_fibonacci_number(3))
    print(get_fibonacci_number_sequence(9))