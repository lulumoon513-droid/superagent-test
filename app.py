def divide(a, b):
    return a / b


def average(values):
    total = 0
    for v in values:
        total += v
    return total / len(values)


if __name__ == "__main__":
    print(divide(10, 0))
