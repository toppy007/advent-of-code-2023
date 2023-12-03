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

total = 0
symbole = ['*', '-', '&', '+', '/', '$', '@', '=', '#', '%']

for index, line in enumerate(res):
    data = create_part_data(line)
    matches = []
    for dict in data:
        index_varible = dict.get("index")
        for i in index_varible:
            for x in symbole:
                if (res[index-1][i-1] == x
                    or res[index-1][i] == x
                    or res[index-1][i+1] == x
                    or res[index][i-1] == x
                    or res[index][i] == x
                    or res[index][i+1] == x
                    or res[index+1][i-1] == x
                    or res[index+1][i] == x
                    or res[index+1][i+1] == x):
                    matches.append(dict)
                    break

    res_list = [i for n, i in enumerate(matches)
        if i not in matches[:n]]
    
    for dict in res_list:
        part_number = (dict.get("part"))
        print(part_number)
        total += int(part_number)
print(total)
        
    
    
  
        



            