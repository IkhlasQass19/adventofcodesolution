ranges = []

with open("/Users/qassimiikhlas/Documents/GitHub/adventofcodesolution/Year2025/Day 5: Cafeteria/data.txt", "r") as file:
    content = file.read()

ranges_text, ids_text = content.strip().split("\n\n")

for line in ranges_text.splitlines():
    a, b = map(int, line.split("-"))
    ranges.append((a, b))

count = 0

for line in ids_text.splitlines():
    x = int(line)

    fresh = any(a <= x <= b for a, b in ranges)

    if fresh:
        count += 1

print(count)
# Sort ranges by start
ranges.sort()
merged = []

for start, end in ranges:
    if not merged or start > merged[-1][1] + 1:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)

total_fresh = 0

for start, end in merged:
    total_fresh += end - start + 1

print(total_fresh)