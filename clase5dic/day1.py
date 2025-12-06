'''
cargar un archivo
[0..99]
resultado = 0
para cada linea del archivo
    si dial acaba en 0
        resultado + 1

devolver resultado

'''

def part1(input):
    result = 0
    dial = 50

    for line in input:
        rotation = line[0] 
        number = int(line[1:]) #
        if rotation == "R":
            dial = (dial+number)%100
        else:
            dial = (dial-number)%100
        
        if dial == 0:
            result += 1


    return result

def part2(input):
    result = 0
    dial = 50

    for line in input:
        rotation = line[0] 
        number = int(line[1:]) 
        if rotation == "R":
            dial += number
            if dial > 99:
                result += dial//100
                dial %= 100
        else:
            if dial == 0:
                result -= 1
            dial -= number
            if dial <= 0:
                result += (dial//-100)+1
                dial %= 100


    return result

input = list()
with open("clase5dic/input/day1.txt", "r") as f:
    input = f.readlines()

print(f"Part 1: {part1(input)}")
print(f"Part 2: {part2(input)}")