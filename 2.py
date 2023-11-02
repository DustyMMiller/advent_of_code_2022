score = {
    "X": 1,
    "Y": 2,
    "Z": 3, 
}

rps = {
    "A": {"Y": 6, "X": 3, "Z": 0},
    "B": {"Z": 6, "Y": 3, "X": 0},
    "C": {"X": 6, "Z": 3, "Y": 0}
}

def part_one(input):
    total = 0
    for row in input.split("\n"):
        row_score = rps[row[0]][row[2]] + score[row[2]]
        total += row_score
    print(f"Part one total: {total}")

def part_two(input):
    total = 0
    for row in input.split("\n"):
        match row[2]:
            case "X":
                for game in rps[row[0]]:
                    if rps[row[0]][game] == 0:
                        total += score[game]
            case "Y":
                for game in rps[row[0]]:
                    if rps[row[0]][game] == 3:
                        total += score[game] + 3
            case "Z":
                for game in rps[row[0]]:
                    if rps[row[0]][game] == 6:
                        total += score[game] + 6
    print(f"Part two total: {total}")
    

def main():
    with open("input_2") as file:
        input = file.read()
    part_one(input)
    part_two(input)



if __name__ == "__main__":
    main()