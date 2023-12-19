with open('input.txt', 'r') as file:
    file_input = file.readlines()

result = []
current_sublist = []

for line in file_input:
    item = line.rstrip('\n')
    if not item.strip():
        result.append(current_sublist)
        current_sublist = []
    else:
        current_sublist.append(list(item))

if current_sublist:
    result.append(current_sublist)

repeated = {}
total = []

for data_list in result:
    change = 1
    c = 0

    for x in range(600):
        if change <= 2:
            transposed = [list(row) for row in zip(*data_list)]
            change += 1
        else:
            transposed = [list(reversed(row)) for row in zip(*data_list)]
            change += 1
            if change == 3:
                change += 1

        turns = []

        for line in transposed:
            split_lists = []
            current_split = []

            for index, char in enumerate(line):
                if char == '#':
                    if current_split:
                        split_lists.append(current_split)
                        current_split = []
                    split_lists.append([char])
                else:
                    current_split.append(char)

            if current_split:
                split_lists.append(current_split)

            for sublist in split_lists:
                i, j = 0, 0
                while j < len(sublist):
                    if sublist[j] == 'O':
                        sublist[i], sublist[j] = sublist[j], sublist[i]
                        i += 1
                    j += 1

            joined_list = [item for sublist in split_lists for item in sublist]
            turns.append(joined_list)

        data_list = turns

        added = 0
        for index, i in enumerate(data_list):
            count_of_10 = i.count('O')
            tot = count_of_10 * (index+1)
            added += tot
        
        total.append(added)
        print(total)
        
        print(x)
        
        if x > 35:
            state_hash = str(total[-35:])
            if state_hash in repeated:
                start = repeated[state_hash]
                length = x - start
                break
            repeated[state_hash] = x    

target = 1_000_000_000
offset = (target - start) % length - 1

print(total[start + offset])

106390