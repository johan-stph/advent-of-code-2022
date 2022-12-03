def read_file(filepath: str) -> list[str]:
    with open(filepath, "r") as f:
        return f.readlines()


def get_point_of_shape(shape: str) -> int:
    if shape == "X":
        return 1
    if shape == "Y":
        return 2

    if shape == "Z":
        return 3


def get_winner(opponent: str, plyer: str):
    if opponent == "A" and plyer == "X" or opponent == "B" and plyer == "Y" or opponent == "C" and plyer == "Z":
        return 3
    if opponent == "A":
        return 6 if plyer == "Y" else 0
    elif opponent == "B":
        return 6 if plyer == "Z" else 0
    elif opponent == "C":
        return 6 if plyer == "X" else 0


def assignment_one():
    lines = read_file("input.txt")
    score = 0
    for line in lines:
        split = line.split(" ")
        opp = split[0].strip()
        pl = split[1].strip()
        score += get_point_of_shape(pl) + get_winner(opp, pl)
    print(score)


def get_winner_v2(opp: str, output: str) -> int:
    if output == "Y":
        if opp == "A":
            we_play = "X"
        elif opp == "B":
            we_play = "Y"
        else:
            we_play = "Z"
        return 3 + get_point_of_shape(we_play)

    if output == "X":
        if opp == "A":
            we_play = "Z"
        elif opp == "B":
            we_play = "X"
        else:
            we_play = "Y"
        return get_point_of_shape(we_play)

    if output != "Z":
        raise KeyboardInterrupt()

    if opp == "A":
        we_play = "Y"
    elif opp == "B":
        we_play = "Z"
    else:
        we_play = "X"
    return 6 + get_point_of_shape(we_play)


def assignment_two():
    lines = read_file("input.txt")
    score = 0
    for line in lines:
        split = line.split(" ")
        opp = split[0].strip()
        result = split[1].strip()
        score += get_winner_v2(opp, result)
    print(score)


def main():
    assignment_one()
    assignment_two()


if __name__ == '__main__':
    main()
