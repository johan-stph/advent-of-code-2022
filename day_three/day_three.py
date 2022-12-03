def ass1():
    with open("input.txt", "r") as f:
        output = []
        for line in f:
            line = line.strip()
            duplicate = set()
            for i in range(len(line)):
                if i < (len(line) / 2):
                    duplicate.add(line[i])
                    continue
                if line[i] in duplicate:
                    output.append(line[i])
                    break
        print(sum(map(get_point_of_char, output)))


def ass2():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        output = []
        for i in range(0, len(lines), 3):
            r1_set = {*(lines[i].strip())}
            r2_set = {*(lines[i + 2].strip())}
            for char in lines[i + 2].strip():
                if char in r1_set and char in r2_set:
                    output.append(char)
                    break
        print(sum(map(get_point_of_char, output)))


def get_point_of_char(c: str) -> int:
    return ord(c) - 38 if c.isupper() else ord(c) - 96


if __name__ == '__main__':
    ass2()
