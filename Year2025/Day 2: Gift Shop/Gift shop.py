def get_all_invalid_indices1(arr):
    all_invalid_indices= []
    for start, end in arr:
        for i in range(start, end + 1):
            s=str(i)
            mid = len(s) // 2
            first = s[:mid]
            second = s[mid:]
            if first==second :
                all_invalid_indices.append(i)
    total = sum(all_invalid_indices)
    return total

def get_all_invalid_indices2(arr):
    all_invalid_indices= []
    for start, end in arr:
        for i in range(start, end + 1):
            s=str(i)
            print(s)
            for j in range(1, len(s)):
                if len(s) % j == 0 and s == s[:j] * (len(s) // j):
                    print(s[:i])
                    all_invalid_indices.append(i)
                    break    
    total = sum(all_invalid_indices)
    return total

result = []

with open("/Users/qassimiikhlas/Documents/Improvment/Problem solving/Day 2: Gift Shop/data.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        parts = line.split(',')
        for part in parts:
            part = part.strip()
            if part:
                start, end = map(int, part.split('-'))
                result.append((start, end))

print(get_all_invalid_indices2(result))



