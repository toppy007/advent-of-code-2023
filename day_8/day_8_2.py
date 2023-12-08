from math import gcd

def lcm(xs):
  ans = 1
  for x in xs:
    ans = (x*ans)//gcd(x,ans)
  return ans

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

turns = 0

keyA = []
for key in map_dict:
    if key[-1] == 'A':
        keyA.append(key)
        
counter = 0
finished = False

T = {}

while not finished:
    new = []
    for i,k in enumerate(keyA):
        x = map_dict[k]
        
        if counter >= len(directions):
            counter = 0
        dir = directions[counter]
        if dir == 'L':
            key = x[0]
            new.append(key)
        else:
            key = x[1]
            new.append(key)

        if key[-1] == 'Z':
            T[i] = turns+1 
            print(T)
            if len(T) == len(keyA):
                print(lcm(T.values()))
                finished = True
    
    keyA = new
    counter += 1
    turns += 1
        
