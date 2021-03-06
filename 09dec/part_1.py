puzzle_input = [int(line.replace("\n", "")) for line in open('puzzle_input.txt').readlines()]

PREAMBLE_SIZE = 25

def all_duos(lst):
    duos = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            duos.append((lst[i], lst[j]))
    
    return duos

for idx, num in enumerate(puzzle_input):
    if idx < PREAMBLE_SIZE:
        continue

    section = puzzle_input[max(0, idx-PREAMBLE_SIZE):][:min(PREAMBLE_SIZE, idx)]

    found_pair = False
    for duo in all_duos(section):
        if sum(duo) == num:
            print(f"{duo[0]} + {duo[1]} = {num}")
            found_pair = True
            break
    
    if not found_pair:
        print("No pair num:", num)
        break
