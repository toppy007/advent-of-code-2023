with open('input.txt', 'r') as file:
    input = file.readlines()

data = []

for index, line in enumerate(input):
    data_point = {}
    item = line.rstrip('\n').split(' ')
    data_point.update([('order', index)])
        
    direction_mapping = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}
    cleaned_direction = item[2].strip('()#')
    direction = cleaned_direction[-1]
    if direction in direction_mapping:
        data_point['direction'] = direction_mapping[direction]
    
    cleaned_hex = item[2].strip('()#')
    modified_hex = cleaned_hex[:-1]
    data_point.update([('distance', int(modified_hex, 16))])

    data.append(data_point)

# for index, line in enumerate(input):
#     data_point = {}
#     item = line.rstrip('\n').split(' ')
#     data_point.update([('order', index)])
#     data_point.update([('direction', item[0])])
#     data_point.update([('distance', int(item[1]))])
#     data_point.update([('colour', item[2])])
#     data.append(data_point)

start_x_coord, start_y_coord = 0, 0
end_x_coord, end_y_coord = 0, 0

start_r = True

direction_map = {'DL': 1, 'RD': 1, 'LD': 0, 'DR': 0, 'LU': 1, 'UR': 1, 'RU': 0, 'UL': 0}

for j in range(len(data)):
    
    corner = data[j-1]['direction']
    corner1 = data[j]['direction']
    if j == len(data) - 1:
        corner2 = data[0]['direction']
    else:
        corner2 = data[j+1]['direction']
    
    concatenated_direction1 = corner + corner1
    concatenated_direction2 = corner1 + corner2
    if concatenated_direction1 in direction_map:
        matching_value1 = direction_map[concatenated_direction1]
    if concatenated_direction2 in direction_map:
        matching_value2 = direction_map[concatenated_direction2]
    
    distance = data[j]['distance']
    distance = (distance - 1) + matching_value1 + matching_value2
    data[j]['distance'] = distance

for data_point in data:

    direction = data_point.get('direction')
    distance = data_point.get('distance')
    if direction == 'R':
        data_point.update([('start', (start_x_coord, start_y_coord))])
        end_y_coord = start_y_coord
        end_x_coord += distance
        data_point.update([('end', (end_x_coord, end_y_coord))])
        start_x_coord, start_y_coord = end_x_coord, end_y_coord
    elif direction == 'L':
        data_point.update([('start', (start_x_coord, start_y_coord))])
        end_y_coord = start_y_coord
        end_x_coord -= distance
        data_point.update([('end', (end_x_coord, end_y_coord))])
        start_x_coord, start_y_coord = end_x_coord, end_y_coord
    elif direction == 'D':
        data_point.update([('start', (start_x_coord, start_y_coord))])
        end_y_coord += distance
        end_x_coord = start_x_coord
        data_point.update([('end', (end_x_coord, end_y_coord))])
        start_x_coord, start_y_coord = end_x_coord, end_y_coord
    elif direction == 'U':
        data_point.update([('start', (start_x_coord, start_y_coord))])
        end_y_coord -= distance
        end_x_coord = start_x_coord
        data_point.update([('end', (end_x_coord, end_y_coord))])
        start_x_coord, start_y_coord = end_x_coord, end_y_coord
        
    print(data_point)
        
x_coord = []
y_coord = []

for i in data:
    x, y = i['start']
    y_coord.append(y)
    x_coord.append(x)
    
x_reverse = x_coord[1:] 
y_reverse = y_coord[1:] 

x_coord_res = x_reverse[::-1]
y_coord_res = y_reverse[::-1]

x_coord[1:] = x_coord_res
y_coord[1:] = y_coord_res

x_coord.append(0)
y_coord.append(0)

shoelace_up = []
shoelace_down = []

for x in range(len(x_coord)-1):
    shoelace_up.append(x_coord[x] * y_coord[x + 1])
    shoelace_down.append(y_coord[x] * x_coord[x + 1])

print(sum(shoelace_up))
print(sum(shoelace_down))

print(abs(sum(shoelace_up) - sum(shoelace_down)) / 2)
    

