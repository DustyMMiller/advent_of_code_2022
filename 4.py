def part_one(input):
    pairs = 0
    for line in input.split("\n"):
        elves = line.split(",")
        if ((int(elves[0].split("-")[0]) >= int(elves[1].split("-")[0]) and
            int(elves[0].split("-")[1]) <= int(elves[1].split("-")[1])) or
            (int(elves[0].split("-")[0]) <= int(elves[1].split("-")[0]) and
            int(elves[0].split("-")[1]) >= int(elves[1].split("-")[1]))):
            pairs += 1
    print(pairs)

def part_two(input):
    pairs = 0
    for line in input.split("\n"):
        elves = line.split(",")
        if ((int(elves[0].split("-")[0]) <= int(elves[1].split("-")[0]) and
            int(elves[0].split("-")[1]) >= int(elves[1].split("-")[0])) or
            (int(elves[0].split("-")[0]) >= int(elves[1].split("-")[0]) and
            int(elves[0].split("-")[0]) <= int(elves[1].split("-")[1]))):
            pairs += 1
    print(pairs)


def main():
    with open("input_4") as file:
        input = file.read()
    test_input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
    part_one(input)
    part_two(input)



if __name__ == "__main__":
    main()