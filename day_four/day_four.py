def ass1():
    overlap = 0
    with open("input.txt", "r") as f:
        for line in f:
            first_pair = tuple(map(lambda x: int(x), line.split(",")[0].strip().split("-")))
            second_pair = tuple(map(lambda x: int(x), line.split(",")[1].strip().split("-")))

            if first_pair[0] <= second_pair[0] and first_pair[1] >= second_pair[1]:
                overlap += 1
                continue

            if second_pair[0] <= first_pair[0] and second_pair[1] >= first_pair[1]:
                overlap += 1
    return overlap


def ass2():
    overlap = 0
    with open("input.txt", "r") as f:
        for line in f:
            first_pair = tuple(map(lambda x: int(x), line.split(",")[0].strip().split("-")))
            second_pair = tuple(map(lambda x: int(x), line.split(",")[1].strip().split("-")))
            first_range = set(range(first_pair[0], first_pair[1] + 1))
            for i in range(second_pair[0], second_pair[1] + 1):
                if i in first_range:
                    overlap += 1
                    break

    return overlap


def main():
    print(ass1())
    print(ass2())


if __name__ == '__main__':
    main()
