with open ('input.txt', 'r') as file:
    input = file.readlines()

clean = []
for line in input:
    if line != '\n':
        clean.append(line.rstrip('\n'))
    else:
        None

data = {}
scores = []

for line in clean:
    without_empty_strings = []
    res = line.split(': ')
    info = [res[1].strip(' ')]
    new = info[0].split(' ')
    for i in new:
        if i != "":
            without_empty_strings.append(i)
    scores.append(without_empty_strings)
    
data.update([('time', scores[0])])
data.update([('distance', scores[1])])

time = data.get('time')
distance = data.get('distance')

total = []

for i in range(0, (len(time))):
    collection = []
    count = 1
    while count <= int(time[i]):
        dis = (int(time[i]) - count) * count
        count += 1
        if int(dis) > int(distance[i]):
            collection.append(dis)
    
    total.append(len(collection))
    print(len(collection))
res = 1

print(len(total))

for i in range(len(total)):
    res = res * total[i]
    
print(res)
    


            
        
    