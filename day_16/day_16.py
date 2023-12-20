# note that '\\' has changed to '?'

import time

with open ('input.txt', 'r') as file:
    input = file.readlines() 

layout = []

bondry = ((len(input[0])-1) * '@')
input.insert(0, bondry)
input.append(bondry)

for line in input:
    line = line.rstrip('\n').replace('\\', 'x')
    layout.append(list("@" + line + "@"))

start_pionts = []

top = [1, 0]
bottom = [-1, 0]
left = [0, 1]
right = [0, -1]

for j in range(0, len(layout)-1):

    current = [1, j]
    last = [0, j]
    
    current_res = [x + y for x, y in zip([0, 1], current)]
    last_res = [x + y for x, y in zip([0, 1], last)]
    start_pionts.append([last_res, current_res])
    
    current = [len(layout)-2, j]
    last = [len(layout)-1, j]
    
    current_res = [x + y for x, y in zip([0, 1], current)]
    last_res = [x + y for x, y in zip([0, 1], last)]
    start_pionts.append([last_res, current_res])
    
    current = [j, len(layout)-2]
    last = [j, len(layout)-1]
    
    current_res = [x + y for x, y in zip([0, 0], current)]
    last_res = [x + y for x, y in zip([0, 0], last)]
    start_pionts.append([last_res, current_res])

    current = [j, 1]
    last = [j, 0]
    
    current_res = [x + y for x, y in zip([0, 0], current)]
    last_res = [x + y for x, y in zip([0, 0], last)]
    start_pionts.append([last_res, current_res])

def find_direction(positions):

    up = [-1, 0]
    down = [1, 0]
    right = [0, 1]
    left = [0, -1]

    for i in range(1, len(positions)):
        direction = [x - y for x, y in zip(positions[i], positions[0])]
    if direction == up:
        return up 
    elif direction == down:
        return down
    elif direction == right:
        return right
    elif direction == left:
        return left

def next_move(direction, currentt_position, sym):
    if sym == '.':
        if direction == [-1, 0]:
            return [sum(x) for x in zip(currentt_position, [-1, 0])]
        elif direction == [1, 0]:
            return [sum(x) for x in zip(currentt_position, [1, 0])]
        elif direction == [0, 1]:
            return [sum(x) for x in zip(currentt_position, [0, 1])]
        elif direction == [0, -1]:
            return [sum(x) for x in zip(currentt_position, [0, -1])]
    
    elif sym == '|':
        if direction == [-1, 0]:
            return [sum(x) for x in zip(currentt_position, [-1, 0])], None
        elif direction == [1, 0]:
            return [sum(x) for x in zip(currentt_position, [1, 0])], None
        elif direction == [0, 1]:
            return [sum(x) for x in zip(currentt_position, [1, 0])], [sum(x) for x in zip(currentt_position, [-1, 0])]
        elif direction == [0, -1]:
            return [sum(x) for x in zip(currentt_position, [1, 0])], [sum(x) for x in zip(currentt_position, [-1, 0])]

    elif sym == '-':
        if direction == [-1, 0]:
            return [sum(x) for x in zip(currentt_position, [0, 1])], [sum(x) for x in zip(currentt_position, [0, -1])]
        elif direction == [1, 0]:
            return [sum(x) for x in zip(currentt_position, [0, 1])], [sum(x) for x in zip(currentt_position, [0, -1])]
        elif direction == [0, 1]:
            return [sum(x) for x in zip(currentt_position, [0, 1])], None
        elif direction == [0, -1]:
            return [sum(x) for x in zip(currentt_position, [0, -1])], None
        
    elif sym == '/':
        if direction == [-1, 0]:
            return [sum(x) for x in zip(currentt_position, [0, 1])]
        elif direction == [1, 0]:
            return [sum(x) for x in zip(currentt_position, [0, -1])]
        elif direction == [0, 1]:
            return [sum(x) for x in zip(currentt_position, [-1, 0])]
        elif direction == [0, -1]:
            return [sum(x) for x in zip(currentt_position, [1, 0])]
    
    elif sym == 'x':
        if direction == [-1, 0]:
            return [sum(x) for x in zip(currentt_position, [0, -1])]
        elif direction == [1, 0]:
            return [sum(x) for x in zip(currentt_position, [0, 1])]
        elif direction == [0, 1]:
            return [sum(x) for x in zip(currentt_position, [1, 0])]
        elif direction == [0, -1]:
            return [sum(x) for x in zip(currentt_position, [-1, 0])]
        
def remove_duplicate_sublists(duplicate_coordinates):
    seen = set()
    result = [coordinates for coordinates in duplicate_coordinates if tuple(map(tuple, coordinates)) not in seen and not seen.add(tuple(map(tuple, coordinates)))]
    return result

ans = 0
count = 0
for current in start_pionts:
    print(count)

    current_answer = 0
    calculate_ans = []
    current_beams = []
    final = []
    beams_record = []
    
    current_beams.append(current)
    for x in range(600):
        collection_moves = []
        counter = 0
        for index, i in enumerate(current_beams):
            beams_record.append(i[1])

            new_moves = []
            sym = layout[i[1][0]][i[1][1]]
            direction = find_direction(i)
            
            if sym == '@':
                del i

            if sym == '|':
                next1, next2 = next_move(direction, i[1], sym)
                new_moves += [i[1], next1]
                collection_moves.append(new_moves)
                new_moves = []
                if next2 != None:
                    new_moves += [i[1], next2]
                    collection_moves.append(new_moves)

            elif sym == '-':
                next1, next2 = next_move(direction, i[1], sym)
                new_moves += [i[1], next1]
                collection_moves.append(new_moves)
                new_moves = []
                if next2 != None:
                    new_moves += [i[1], next2]
                    collection_moves.append(new_moves)

            elif sym == '/':
                next = next_move(direction, i[1], sym)
                new_moves += [i[1], next]
                collection_moves.append(new_moves)

            elif sym == 'x':
                next = next_move(direction, i[1], sym)
                new_moves += [i[1], next]
                collection_moves.append(new_moves)

            elif sym == '.':
                next = next_move(direction, i[1], sym)
                new_moves += [i[1], next]
                collection_moves.append(new_moves)
                 
        current_beams = collection_moves
        current_beams = remove_duplicate_sublists(current_beams)
    
    layout_copy = [row[:] for row in layout]

    for i in beams_record:
        layout_copy[i[0]][i[1]] = '#'

    final = layout_copy[1:-1]
    
    for i in final:
        calculate_ans.append(i[1:-1])
    
    for i in calculate_ans:
        current_answer += i.count('#')
        if current_answer > ans:
            ans = current_answer
            # print("".join(i))
    
    count += 1 
          
print(ans)
    
    