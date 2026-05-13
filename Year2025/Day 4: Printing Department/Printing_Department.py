matrix = []
def get_rolls(matrix):
    NumberOfRolls =0
    IndiceI = []
    IndiceJ = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "@":
                # all 8 neighboring positions
                directions = [
                    (-1, -1), (-1, 0), (-1, 1),
                    (0, -1),           (0, 1),
                    (1, -1),  (1, 0),  (1, 1)
                ]
                neighbors = 0
                for dx, dy in directions:
                    x = i + dx
                    y = j + dy
                    # stay inside matrix bounds
                    if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
                        # check neighbor
                        if matrix[x][y] == "@":
                            neighbors += 1
                if neighbors<4 :
                    print(f"@ at ({i},{j}) has {neighbors} neighboring @")
                    IndiceI.append(i)
                    IndiceJ.append(j)
                    NumberOfRolls = NumberOfRolls+1             
    print("NumberOfRolls : ",NumberOfRolls)
    for i in range(len(IndiceI)):
        matrix[IndiceI[i]][IndiceJ[i]] ='x'
    #print(matrix)
    return NumberOfRolls
def get_rolls2(matrix):
    TotalNumberOfRolls=0
    while (1) :
        print('starting ')
        NumberOfRolls=get_rolls(matrix)
        TotalNumberOfRolls=TotalNumberOfRolls+NumberOfRolls
        print (NumberOfRolls)
        if(NumberOfRolls==0) :
            break
    return TotalNumberOfRolls
with open("/Users/qassimiikhlas/Documents/GitHub/adventofcodesolution/Year2025/Day 4: Printing Department/data.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line:
            row = [ch for ch in line]
            matrix.append(row)

print(get_rolls2(matrix))
#print(matrix)