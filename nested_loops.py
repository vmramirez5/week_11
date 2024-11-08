# nested lopp = A loop within another loop (outer, inner)
#                   outer loop:
#                       inner loop:

# for x in range(1,10):
#     print(x, end=" ")  # numbers on the same line

# for x in range(3):
#     for y in range(1,10):
#         print(y, end=" ") 
#     print()

rows = int(input("enter the number of rows: "))
colums = int(input("enter the number of colums: "))
symbol = input("enter a symbol to use: ")

for x in range(rows):
    for y in range(colums):
        print(symbol, end=" ") 
    print()