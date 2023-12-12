with open ('input.txt', 'r') as file:
    input = file.readlines()

end =[]    
size = [1]

for j in size:
    clean = []
    indexes = []

    print('done 1')

    for line in input:
        if line != '\n':
            clean.append(line.rstrip('\n'))
            
    print('done 2')

    indexes = [index for index, row in enumerate(clean) if '#' not in row]

    print('done 3')
    
    print 

    # row_length = len(clean[0])
    # block_of_rows = ['.' * row_length for _ in range(j)]
    # for index in reversed(indexes):
    #     clean[index + 1:index + 1] = [row[:] for row in block_of_rows]


    print('done 4')

    column_index = [i for i in range(len(clean[0])) if '#' not in ''.join(clean[j][i] for j in range(len(clean)))]

    print('done 5')

    data = [list(row) for row in clean]

    print('done 6')

    block_of_columns = ['.'] * (j)

    # for index in reversed(column_index):
    #     for row in data:
    #         row[index + 1:index + 1] = block_of_columns.copy()
        
    print(column_index, indexes)
    
    print('done 7')

    count = 1
    data_dict = []

    for index, line in enumerate(data):
        for i, x in enumerate(line):
            if x[0] == '#':
                location = {}
                line[i] = str(count) + x[1:]
                location['star'] = count
                location['list1'] = i
                location['line1'] = index
                count += 1
                data_dict.append(location)
        stars = count
        
    for i in data:
        print(i)

    print('done 8')

    stars_list = []
    for i in range(1, stars):
        stars_list.append(i)

    print('done 9')

    pairs = []
    for i in range(len(stars_list)):
        for j in range(i + 1, len(stars_list)):
            pairs.append([stars_list[i], stars_list[j]])

    print('done 10')

    location_data = []
    total = 0

    for pair in pairs:
        line1 = 0
        line2 = 0
        list1 = 0
        list2 = 0
        for index, p in enumerate(pair):
            dict = (next((item for item in data_dict if item["star"] == p), None))
            if index == 0:
                line1 = dict.get('line1')
                list1 = dict.get('list1')
            elif index == 1:
                line2 = dict.get('line1')
                list2 = dict.get('list1')
        
        inside_row = 0
        for i in indexes:
            abs_values = sorted([abs(line1), abs(line2)])
            if i > abs_values[0] and i < abs_values[1]:
                inside_row += 1
        
        line_distance = abs(line1) - abs(line2)
        
        inside_col = 0
        for i in column_index:
            abs_values = sorted([abs(list1), abs(list2)])
            if i > abs_values[0] and i < abs_values[1]:
                inside_col += 1
        
        added_lines = (inside_col + inside_row) * 999999
        
        list_distance = abs(list1) - abs(list2)
        distance = abs(line_distance) + abs(list_distance) + added_lines
        
        total += abs(distance)
    end.append(total)

print(end)
