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
            dial = (dial+number)%100
        else:
            dial = (dial-number)%100
        
        if dial == 0:
            result += 1


    return result

input = list()
with open("clase5dic/day1.txt", "r") as f:
    input = f.readlines()

print(f"Part 1: {part1(input)}")