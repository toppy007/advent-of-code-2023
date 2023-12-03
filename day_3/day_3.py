with open ('input.txt', 'r') as file:
    input = file.readlines()
    
def prepend_boarder(input):
    char = '.'
    empty_line = char * 141
    
    input.insert(0, empty_line)
    input.insert((len(input)), empty_line)
    
    result = []
    
    for line in input:
        result.append(char + str(line))
    return result
    
def create_part_data(line):
    list = []
    data = {}
    number = []
    indexgroup = []        

    for index, char in enumerate(line):
        if char.isdigit():
            number += [char]
            indexgroup += [index]          
        else:
            if len(number) != 0:
                data.update([('part', ''.join(number))])
                data.update([('index', indexgroup)])
                indexgroup = []
                number = []
                list.append(data)
                data = {}
    return(list)

res = prepend_boarder(input)

for index, line in enumerate(res):
    data = create_part_data(line)
    print(line)
    for dict in data:
        print(index, dict)

        
        



            