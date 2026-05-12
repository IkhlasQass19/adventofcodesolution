result = []
'''def get_password(arr, IntialPos):
    position = IntialPos
    countZero=0
    for direction, number in arr:
        #print(position)
        #print(direction, number)
         if(direction=='L') :
            position=(position-number)%100
        else :
            position=(position+number)%100
        if position==0 :
            countZero=countZero+1
    return countZero'''
def get_password(arr, IntialPos):
    position = IntialPos % 100
    countZero = 0
    for direction, number in arr:
        if direction == 'R':
            start = position + 1
            end = position + number
        else:
            start = position - number
            end = position - 1
        def count_multiples(a, b):
            return b // 100 - (a - 1) // 100
        countZero += count_multiples(start, end)
    return countZero

with open("/Users/qassimiikhlas/Documents/Improvment/Problem solving/data.txt", "r") as file:
    for line in file:
        line = line.strip()  # remove spaces/newlines
        if line:  # skip empty lines
            result.append((line[0], int(line[1:])))
print(get_password(result, 50))
