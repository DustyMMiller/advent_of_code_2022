

def main():
    with open("input_1") as file:
        input = file.read()
    elves = []
    l = 0
    for i in input.split("\n"):
        if not elves:
            elves.append(0)
        try:
            elves[l] = elves[l] + int(i)
        except:
            l += 1
            elves.append(0)
    elves.sort()
    print(elves[-1])
    print(sum(elves[-3:])) 

if __name__ == "__main__":
    main()