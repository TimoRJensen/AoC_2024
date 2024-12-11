from pathlib import Path


file = Path("1/input")
lefts = []
rights = []
for line in file.open():
    strings = line.split()
    left = strings[0]
    right = strings[1]
    lefts.append(int(left))
    rights.append(int(right))

left_sorted = sorted(lefts)
right_sorted = sorted(rights)

combined = zip(left_sorted, right_sorted)
distances = []
for pair in combined:
    distances.append(abs(pair[0] - pair[1]))

print(f"Sum of distances: {sum(distances)}")
