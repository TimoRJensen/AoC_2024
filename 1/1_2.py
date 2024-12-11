from pathlib import Path

file = Path("1/input")
lefts = []
rights = []
for line in file.open():
    strings = line.split()
    left = int(strings[0])
    lefts.append(left)
    right = int(strings[1])
    rights.append(right)

    def find_in_right(left) -> int:
        cnt = 0
        for right in rights:
            if left == right:
                cnt += 1
        return cnt


similarities = []
for e in lefts:
    similarities.append(e * find_in_right(e))

# print(f"{similarities=}")
print(f"{sum(similarities)=}")
