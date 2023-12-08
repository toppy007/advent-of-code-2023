with open ('input.txt' , 'r') as file:
    input = file.readlines()
    
clean = []
for line in input:
    if line != '\n':
        clean.append(line.rstrip('\n'))
    else:
        None
        
directions = (list(clean[0]))
map = clean[1:len(clean)]

map_dict = {}

for i in map:

    j = i.split(' = ')
    k = j[1].replace('(', '')
    p = k.replace(')', '')
    postion_list = p.split(', ')
    
    map_dict.update([(j[0], postion_list)])

start = 'AAA'
counter = 0
turns = 0 

while start != 'ZZZ':
    x = map_dict.get(start)
    print(x)

    if counter > len(directions)-1:
        counter = 0
        
    dir = (directions[counter])
    
    if dir == 'L':
        start = x[0]  
        counter += 1
    else:
        start = x[1]
        counter += 1
    
    turns += 1
    print(turns)
    
    