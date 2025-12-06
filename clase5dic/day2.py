import textwrap

def part1(input):
    result = 0
    for rang in input:
        start = int(rang.split("-")[0])
        end = int(rang.split("-")[1])

        for i in range(start, end+1):
            num_text = str(i)
            size = len(num_text)
            if size%2 == 0:
                if num_text[0:size//2] == num_text[size//2:]:
                    result += i
        

    return result

def part2(input):
    result = 0
    for rang in input:
        start = int(rang.split("-")[0])
        end = int(rang.split("-")[1])

        for i in range(start, end+1):
            num_text = str(i)
            size = len(num_text)
            parts = 1
            while parts <= size//2:
                if size%parts == 0:
                    num_in_parts = textwrap.wrap(num_text, parts)
                    if len(set(num_in_parts)) <= 1:
                        result += i
                        break
                parts += 1

    return result

input = list()
with open("clase5dic/input/day2.txt", "r") as f:
    input = f.read().split(",")

print(f"Part 1: {part1(input)}")
print(f"Part 2: {part2(input)}")