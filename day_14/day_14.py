with open ('input.txt', 'r') as file:
    input = file.readlines()

result = []
current_sublist = []

for line in input:
    item = line.rstrip('\n')
    if not item.strip():
        result.append(current_sublist)
        current_sublist = []
    else:
        current_sublist.append(list(item))

if current_sublist:
    result.append(current_sublist)
 
space = False
   
for data_list in result:
    data_list = [list(s.rstrip('\n')) for s in input]
    new_row = ['0'] * len(data_list[0])
    data_list.insert(0, new_row)

    for i in range(len(data_list[0])):
        if data_list[0][i][0] == 'O':
            data_list[0][i] = str(len(data_list)) + data_list[0][i][1:]
            
        elif data_list[0][i][0] == '#':
            data_list[0][i] = '0' + data_list[0][i][1:]

    while space == False:
        concatenated_start = ''.join([''.join(sublist) for sublist in data_list])
        print(concatenated_start)
        
        for i in range(1, len(data_list)):
            for x in range(0, (len(data_list[0]))):

                if str(data_list[i][x])[0] == 'O' and str(data_list[i-1][x])[0] == '.':
                    data_list[i-1][x] = 'O'
                    data_list[i][x] = '.'
                
                elif str(data_list[i][x])[0] == 'O' and str(data_list[i-1][x])[0] != '.':
                    data_list[i][x] = '10'
                
                elif str(data_list[i][x])[0] == '#':
                    data_list[i][x] = '0'
                
        print('------------------')   

        concatenated_string = ''.join([''.join(sublist) for sublist in data_list])

        if concatenated_string == concatenated_start:
            space = True

total = 0
       
for index, i in enumerate(data_list):
    count_of_10 = i.count('10')
    tot = count_of_10 * (len(data_list) - index)
    total += tot
print(total)
            