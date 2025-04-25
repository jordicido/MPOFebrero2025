dimension = int(input("Introduce un número positivo impar que indique la dimensión del cuadrado:\n"))

for i in range(dimension):
    for j in range(dimension):
        if i == 0 or i == dimension-1:
            print("x"*dimension,end="")
            break
        if j == 0 or j == dimension-1 or j == i or j == dimension-i-1:
            print("x",end="")
        else:
            print(" ",end="")
    print()
        

'''
dimension = 5
xxxxx
xx xx
x x x
xx xx
xxxxx

dimension = 7
xxxxxxx
xx   xx
x x x x
x  x  x
x x x x
xx   xx
xxxxxxx


'''