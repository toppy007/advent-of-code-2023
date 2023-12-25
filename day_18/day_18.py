with open('input.txt', 'r') as file:
    input = file.readlines()

data = []
for index, line in enumerate(input):
    data_point = {}
    item = line.rstrip('\n').split(' ')
    data_point.update([('order', index)])
    data_point.update([('direction', item[0])])
    data_point.update([('amount', int(item[1]))])
    data_point.update([('colour', item[2])])
    data.append(data_point)
    
def generate_dig_area_coord(data):
    dig_area_coordinates = []

    x_coord = 0
    y_coord = 0

    for data_point in data:
        direction = data_point.get('direction')
        value = data_point.get('amount')
        colour = data_point.get('colour')
        
        if direction == 'R':
            for i in range(value):
                xy = {}
                x_coord += 1
                xy.update([('xy', [y_coord, x_coord])])
                xy.update([('colour', colour)])
                dig_area_coordinates.append(xy)
        elif direction == 'L':
            for i in range(value):
                xy = {}
                x_coord -= 1
                xy.update([('xy', [y_coord, x_coord])])
                xy.update([('colour', colour)])
                dig_area_coordinates.append(xy)
        elif direction == 'D':
            for i in range(value):
                xy = {}
                y_coord += 1
                xy.update([('xy', [y_coord, x_coord])])
                xy.update([('colour', colour)])
                dig_area_coordinates.append(xy)
        elif direction == 'U':
            for i in range(value):
                xy = {}
                y_coord -= 1
                xy.update([('xy', [y_coord, x_coord])])
                xy.update([('colour', colour)])
                dig_area_coordinates.append(xy)
    
    return dig_area_coordinates

def dig_area_calculator(xy):

    min_width, max_width = 0, 0
    min_height, max_height = 0, 0

    for data in xy:
        xy = data.get('xy')
        
        if xy[1] > max_width:
            max_width = xy[1]   
        elif xy[1] < min_width:
            min_width = xy[1]
                
        if xy[0] > max_height:
            max_height = xy[0]
        elif xy[0] < min_height:
            min_height = xy[0]
            
    return min_height, max_height, min_width, max_width

def build_dig_grid(min_height, max_height, min_width, max_width):
    max_height = abs(max_height) + abs(min_height)
    max_width = abs(max_width) + abs(min_width)
    area = []
    for i in range(max_height +1 ):
        area.append(['.'] * (max_width +1))
        
    return area

xy = generate_dig_area_coord(data)
min_height, max_height, min_width, max_width = dig_area_calculator(xy)
dig_gird = build_dig_grid(min_height, max_height, min_width, max_width)


for index, x in enumerate(xy):
    xy = x.get('xy')
    dig_gird[xy[0] + abs(min_height)][xy[1] + abs(min_width)] = '#'


dig_gird[int((xy[0] + abs(min_height)) / 2)][int((xy[1] + abs(min_width)) / 2)] = '1'

search_area = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

changed = True 

while changed:
    changed = False 

    for x in range(len(dig_gird)):
        for j in range(len(dig_gird[0])):
            if dig_gird[x][j] == '1':
                for k in search_area:
                    s = [a + b for a, b in zip([x, j], k)]
                    if 0 <= s[0] < len(dig_gird) and 0 <= s[1] < len(dig_gird[0]) and dig_gird[s[0]][s[1]] == '.':
                        dig_gird[s[0]][s[1]] = '1'
                        changed = True 


print(''.join(dig_gird[x]))

count = 0

for i in dig_gird:
    count += i.count('#')
    count += i.count('1')
    
print(count)
 
    

