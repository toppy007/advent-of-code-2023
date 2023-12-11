with open ('input.txt', 'r') as file:
    input = file.readlines()
    
clean = []
indexes = []

print('done 1')

for line in input:
    if line != '\n':
        clean.append(line.rstrip('\n'))
        
print('done 2')
    
for index, i in enumerate(clean):
    if i.find('#') < 0:
        indexes.append(index)
        
print('done 3')

count = 0       
for i in indexes:
    for z in range(1, 1000000):
        row = '.' * len(clean[0]) 
        clean.insert(i+count, row)
        count += 1

print('done 4')

column_length = 0
column_index = []
for i in range(len(clean[0])):
    for z in range(1, 1000000):
        column = []
        for x in clean:
            column.append(x[i])
        column_length = len(column)
        string = ''.join(column)
        if string.find('#') < 0:
            column_index.append(i)

print('done 5')

count = 0       
data = []
for i in clean:
    data.append(list(i))

print('done 6')

for i in column_index:
    col = '.'
    for x in data:
        x.insert(i+count, col)
    count += 1

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
    
for i in data_dict:
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
print(len(pairs))

location_data = []
total = 0

for pair in pairs:
    line1 = 0
    line2 = 0
    list1 = 0
    list2 = 0
    for index, p in enumerate(pair):
        dict = (next((item for item in data_dict if item["star"] == p), None))
        print(dict)
        if index == 0:
            line1 = dict.get('line1')
            list1 = dict.get('list1')
        elif index == 1:
            line2 = dict.get('line1')
            list2 = dict.get('list1')
    
    print('--------------')    
    print(line1, line2, list1, list2) 
    line_distance = abs(line1) - abs(line2)
    list_distance = abs(list1) - abs(list2)
    distance = abs(line_distance) + abs(list_distance)
    print(line_distance, list_distance, distance)
    
    total += abs(distance)
# for i in data:
#     print(i)
print(total)