with open("/Users/qassimiikhlas/Documents/GitHub/adventofcodesolution/Year2025/Day 6: Trash Compactor/data.txt", "r") as file:
    lines = file.read().splitlines()

width = max(len(line) for line in lines)
lines = [line.ljust(width) for line in lines]

blocks = []
in_block = False
start = 0

for c in range(width):
    has_char = any(line[c] != " " for line in lines)

    if has_char and not in_block:
        start = c
        in_block = True

    elif not has_char and in_block:
        blocks.append((start, c - 1))
        in_block = False

if in_block:
    blocks.append((start, width - 1))

grand_total = 0

for left, right in blocks:
    parts = []

    for line in lines:
        piece = line[left:right + 1].strip()

        if piece:
            parts.append(piece)

    if not parts:
        continue

    op = parts[-1]
    nums = list(map(int, parts[:-1]))

    if op == "+":
        value = sum(nums)

    elif op == "*":
        value = 1

        for n in nums:
            value *= n


    grand_total += value

print(grand_total)


def parse_worksheet(filename):
    with open(filename, "r") as f:
        lines = [line.rstrip("\n") for line in f]

    width = max(len(line) for line in lines)
    lines = [line.ljust(width) for line in lines]
    return lines


def solve_part_two(lines):
    rows = len(lines)
    cols = len(lines[0])
    total = 0

    col = cols - 1

    while col >= 0:
        # Skip blank separator columns
        while col >= 0 and all(lines[r][col] == " " for r in range(rows)):
            col -= 1

        if col < 0:
            break

        # Collect one full problem block: consecutive non-blank columns
        block_end = col
        while col >= 0 and not all(lines[r][col] == " " for r in range(rows)):
            col -= 1
        block_start = col + 1

        # Find the operator in the bottom row of this block
        operator = None
        for c in range(block_start, block_end + 1):
            if lines[rows - 1][c] in "+*":
                operator = lines[rows - 1][c]
                break

        if operator is None:
            raise ValueError(f"No operator found in block {block_start}-{block_end}")

        # Each column in the block is one number
        numbers = []
        for c in range(block_start, block_end + 1):
            digits = [lines[r][c] for r in range(rows - 1) if lines[r][c].isdigit()]
            if digits:
                numbers.append(int("".join(digits)))

        if operator == "+":
            result = sum(numbers)
        elif operator == "*":
            result = 1
            for n in numbers:
                result *= n
        else:
            raise ValueError(f"Unknown operator: {operator}")

        total += result

    return total


if __name__ == "__main__":
    lines = parse_worksheet("/Users/qassimiikhlas/Documents/GitHub/adventofcodesolution/Year2025/Day 6: Trash Compactor/data.txt")
    answer = solve_part_two(lines)
    print(answer)