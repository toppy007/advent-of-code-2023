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


def section_one():
    res = prepend_boarder(input)
    
    total = 0
    # symbole = ['*', '-', '&', '+', '/', '$', '@', '=', '#', '%']
    
    symbole = ['*']
    part2 = []
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
    
        part2.append(res_list)
    
    return part2, res

def star_location_and_line():

    sec, res = section_one()

    starfound = []

    for j, i in enumerate(sec):
            for dict in i:
                indexes = dict.get('index')
                for i in indexes:
                    if res[j-1][i-1] == '*':
                        dict.update([('star', i-1),('post', j-1)])
                        # print(dict)
                    elif res[j-1][i] == '*':
                        dict.update([('star', i),('post', j-1)])
                        # print(dict)
                    elif res[j-1][i+1] == '*':
                        dict.update([('star', i+1),('post', j-1)])
                        # print(dict)
                    elif res[j][i-1] == '*':
                        dict.update([('star', i-1),('post', j)])
                        # print(dict)
                    elif res[j][i] == '*':
                        dict.update([('star', i),('post', j)])
                        # print(dict)
                    elif res[j][i+1] == '*':
                        dict.update([('star', i+1),('post', j)])
                        # print(dict)
                    elif res[j+1][i-1] == '*':
                        dict.update([('star', i-1),('post', j+1)])
                        # print(dict)
                    elif res[j+1][i] == '*':
                        dict.update([('star', i),('post', j+1)])
                        # print(dict)
                    elif res[j+1][i+1] == '*':
                        dict.update([('star', i+1),('post', j+1)])
                        # print(dict)
                    else:
                        None
                starfound.append(dict)
                
    return(starfound)
            
star_location = star_location_and_line()

part_2_answer = 0

for dict in star_location:
    part = dict.get('part')
    list = dict.get('index')
    location = dict.get('star')
    line_number = dict.get('post')
    for dict_search in star_location:
        match_part = dict_search.get('part')
        match_list = dict_search.get('index')
        match_loction = dict_search.get('star')
        match_line_number = dict_search.get('post')
        
        if int(match_loction) == int(location) and int(match_line_number) == int(line_number) and int(part) != int(match_part):
            print(part, match_part)
            part_mutiple = int(part) * int(match_part)
            print(part_mutiple)
            part_2_answer += part_mutiple
              
print(part_2_answer/2)


                
    


    
    
  
        



            