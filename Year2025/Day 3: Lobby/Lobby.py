def build_number(arr):
    maxFirstValue = 0
    maxSecondValue = 0
    maxIndex = 0
    for i in range(len(arr) - 1):
        if maxFirstValue < arr[i]:
            maxFirstValue = arr[i]
            maxIndex = i + 1

    print('the first max value is :', maxFirstValue, 'with indice :', maxIndex - 1)

    for j in range(maxIndex, len(arr)):

        if maxSecondValue < arr[j]:
            maxSecondValue = arr[j]
            print('the second max value is :', maxSecondValue, 'with indice :', j)

    result = str(maxFirstValue) + str(maxSecondValue)

    print('result', result)

    return int(result)


def build_number2(arr, k=12):
    stack = []
    remove = len(arr) - k  # how many digits we can remove

    for digit in arr:

        # remove smaller previous digits if possible
        while stack and remove > 0 and stack[-1] < digit:
            stack.pop()
            remove -= 1

        stack.append(digit)

    # keep exactly k digits
    stack = stack[:k]

    return int("".join(map(str, stack)))

def get_max_joltage(result):
    final = []

    for row in result:
        final.append(build_number(row))

    return final

def get_max_joltage2(array):
    final = []

    for row in array:
        final.append(build_number2(row))
    result =sum(final)
    return result



result = []

with open("/Users/qassimiikhlas/Documents/Improvment/Problem solving/Day 3: Lobby/data.txt", "r") as file:
    for line in file:
        line = line.strip()

        if line:
            digits = [int(ch) for ch in line]
            result.append(digits)

total = get_max_joltage2(result)

print(total)