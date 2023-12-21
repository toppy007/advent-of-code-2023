with open ('input.txt', 'r') as file:
    input = file.readlines() 

layout = []

for line in input:
    line = line.rstrip('\n').replace('\\', 'x')
    layout.append(list(line))
    
s = [0, 0]

left_edge = 0
top_edge = 0
right_edge = len(layout[0])
bottom_edge = len(layout)

def valid_move(paths, next_node):

    result = [a + b for a, b in zip(paths[-1], next_node)]
    valid = sum(result)
    print(valid, result)
    
    if valid < 0:
        return None
    elif result[1] > right_edge:
        return None
    elif result[0] > bottom_edge:
        return None
    elif result[0] == -1 or result[1] == -1:
        return None
    elif len(paths) >= 2:
        if paths[-2] == result:
            return None
        elif len(paths) > 3:
            last_three_paths = paths[-4:]
            last_three_paths.append(result)
            
            first_digits = [path[0] for path in last_three_paths]
            second_digits = [path[1] for path in last_three_paths]

            same_vertical = all(element == first_digits[0] for element in first_digits)
            same_horizontal = all(element == second_digits[0] for element in second_digits)
            
            if same_horizontal == True or same_vertical == True:
                return False
            else:
                return True
        else:
            return True
    else:
        return True
    
def build_snake(paths, next_node):
    snake = []
    result = [a + b for a, b in zip(paths[-1], next_node)]
    for j in paths:
        snake.append(j)
    snake.append(result)
    
    return snake
    
steps = [[1, 0], [-1, 0], [0, 1], [0, -1]]
paths  = [[[0, 0]]]

found = False

# while found == False:
for i in range(16):
    new_snakes = [] 
    print(paths[0])
    for i in range(len(paths)):
        for x in steps:
            new_snake = valid_move(paths[i], x)
            if new_snake == True:
                snake_value = 0
                snake = build_snake(paths[i], x)
                
                for s in snake:
                    snake_value += int(layout[s[0]][s[1]])
                
                if snake[-1] == [7, 7]:
                    found = True
                
                new_snakes.append(snake)   
            
    paths.clear()
    paths += new_snakes
        
    layout_copy = [row[:] for row in layout]

    for x in paths[0]:
        # for x in i:
        layout_copy[x[0]][x[1]] = '#'
    print(paths[0])

    for i in layout_copy:
        print("".join(i)) 
        