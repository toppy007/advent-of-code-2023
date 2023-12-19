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

current = [[1, 0], [1, 1]]

calculate_ans = []
ans = 0
current_beams = []
beams_record = []

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
        
current_beams.append(current)

for x in range(600):
    collection_moves = []
    
    for index, i in enumerate(current_beams):
        beams_record.append(i[1])
        
        new_moves = []
        direction = find_direction(i)
        sym = layout[i[1][0]][i[1][1]]
        
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

for i in beams_record:
    layout[i[0]][i[1]] = '#'

final = layout[1:-1]

for i in final:
    calculate_ans.append(i[1:-1])

for i in calculate_ans:
    ans += i.count('#')
    print("".join(i))
        
print(ans)

6840