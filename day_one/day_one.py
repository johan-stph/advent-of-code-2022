def read_file(filepath: str) -> list[str]:
    with open(filepath, "r") as f:
        return f.readlines()


def assignment():
    output = []
    cal_count = 0
    for line in read_file("day_one_a1.txt"):
        if len(line) == 1:
            output.append(cal_count)
            cal_count = 0
            continue
        cal = int(line)
        cal_count += cal

    return output


def assignment_one():
    output = assignment()
    print(max(output))


def assignment_two():
    output = assignment()
    output.sort()
    print(output[-1] + output[-2] + output[-3])


def main():
    assignment_one()
    assignment_two()


if __name__ == '__main__':
    main()
