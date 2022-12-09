def ass1():
    with open("input.txt", "r") as f:
        content = f.readlines()

    output = [[] for _ in range(17)]
    for i in range(7, -1, -1):
        for count, j in enumerate(range(1, len(content[0]) // 2)):
            output[count].append(content[i][2 * j - 1])
    output = list(filter(lambda x: x[0] != " ", output))
    new_list = [list(filter(lambda x: x != " ", stack)) for stack in output]
    for i in range(10, len(content)):
        splitted = content[i].strip().split(" ")
        amount = int(splitted[1])
        start = int(splitted[3]) - 1
        end = int(splitted[5]) - 1
        for _ in range(amount):
            value = new_list[start].pop()
            new_list[end].append(value)

    return "".join(row[-1] for row in new_list)


def ass2():
    with open("input.txt", "r") as f:
        content = f.readlines()

    output = [[] for _ in range(17)]
    for i in range(7, -1, -1):
        for count, j in enumerate(range(1, len(content[0]) // 2)):
            output[count].append(content[i][2 * j - 1])
    output = list(filter(lambda x: x[0] != " ", output))
    new_list = [list(filter(lambda x: x != " ", stack)) for stack in output]
    for i in range(10, len(content)):
        splitted = content[i].strip().split(" ")
        amount = int(splitted[1])
        start = int(splitted[3]) - 1
        end = int(splitted[5]) - 1

        to_be_stacked = [new_list[start].pop() for _ in range(amount)]
        to_be_stacked.reverse()
        new_list[end].extend(to_be_stacked)

    return "".join(row[-1] for row in new_list)

def main():
    print("Ass1", ass1(), sep=": ")
    print("Ass2", ass2(), sep=": ")


if __name__ == '__main__':
    main()
