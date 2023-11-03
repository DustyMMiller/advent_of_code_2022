def part_one(input):
    total = 0
    for line in input.split("\n"):
        ic = int(len(line)/2)
        c1 = line[:ic]
        c2 = line[ic:]
        match = ord(min(set(c1).intersection(c2)))
        if match > 97:
            match = match - 96
        else:
            match = match - 38
        total += match
    print(total)

def part_two(input):
    total = 0
    i = 0
    group = []
    for line in input.split("\n"):
        group.append(line)
        if len(group) == 3:
            e = ord(min(set.intersection(set(group[0]), set(group[1]), set(group[2]))))
            if e > 97:
                e = e - 96
            else:
                e = e - 38
            total += e
            group = []
    print(total)


def main():
    with open("input_3") as file:
        input = file.read()
    test_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
    part_one(input)
    part_two(input)



if __name__ == "__main__":
    main()