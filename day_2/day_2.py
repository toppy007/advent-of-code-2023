with open ("input.txt", "r") as file:
    input = file.readlines()
    
with open ("test.txt", "r") as file:
    test = file.readlines()

with open ("test_2.txt", "r") as file:
    test_2 = file.readlines()
       
data_structure = {'game' : 2, 'hand' : {'red' : None, 'green' : None, 'blue' : None}}

def dict_for_game(input):
    result = input.split(': ')
    
    game_dict = dict((a.strip(), int(b.strip()))
        for a, b in (element.split(' ')  
            for element in result[0].split(', '))) 
    
    return game_dict

def dict_for_handfull(input):
    game = []
    result = input.split(': ')
    handfull = result[1].split('; ')

    for each in handfull:
        i = each.split(', ')
        color_list = {}
        for colour in i:
            if ' ' in colour:
                key, value = map(str.strip, colour.split(' ', 1))
                color_list[value] = key
                
        game.append(color_list.copy())

    return game

conditions = ( '12 : red', '13 : green', '14 : blue' )

def find_possible_game(input):
    total = []
    for line in input:    
        handfull = dict_for_handfull(line)

        passmark = []
        
        for dictionary in handfull:
            if 'red' in dictionary:
                result = dictionary.get('red')
                if int(result) <= 12:
                    passmark.append('true')
                else:
                    passmark.append('false')

            if 'green' in dictionary:
                result = dictionary.get('green')
                if int(result) <= 13:
                    passmark.append('true')
                else:
                    passmark.append('false')
            
            if 'blue' in dictionary:
                result = dictionary.get('blue')
                if int(result) <= 14:
                    passmark.append('true')
                else:
                    passmark.append('false')
                    
        if not 'false' in passmark:          
            total.append(handfull)
    
    return(total)

total = 0
game = 1

for line in input:    
    handfull = dict_for_handfull(line)
    multiple = []
    
    lowest = []
    for dictionary in handfull:
        if 'red' in dictionary:
            result = dictionary.get('red')
            lowest.append(int(result))
    
    multiple.append(max(lowest))
    
    lowest = []
    for dictionary in handfull:
        if 'blue' in dictionary:
            result = dictionary.get('blue')
            lowest.append(int(result))
    
    multiple.append(max(lowest))
    
    lowest = []
    for dictionary in handfull:
        if 'green' in dictionary:
            result = dictionary.get('green')
            lowest.append(int(result))
    
    multiple.append(max(lowest))

    sum = (multiple[0] * multiple[1] * multiple[2])
    total += sum
    print(game, "/", multiple[0],"-", multiple[1],"-", multiple[2], "/", sum, "/", total)
    game += 1
    

    
    
    

    
    
        
        
