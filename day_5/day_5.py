with open ('input.txt', 'r') as file:
    input = file.readlines()

clean = []
for line in input:
    if line != '\n':
        clean.append(line.rstrip('\n'))
    else:
        None
        
cat = []
for index, line in enumerate(clean):
    if line.find('map') >= 0:
        cat.append(index)


groups = []
for i in range(len(cat)):
    if i < (len(cat)-1):
        groups.append(clean[cat[i]:cat[i+1]])
    else:
        groups.append(clean[cat[i]:len(clean)])

data = {}
seeds = clean[0].split(': ')
seeds_data = seeds[1].split(' ')
data.update([(seeds[0], seeds_data)])

for i in groups:
    dict_name = i[0].split(' ')
    codes = []
    for x in range(1, (len(i))):
        split = i[x].split(' ')
        codes.append(split)
    data.update([(dict_name[0], codes)])

seeds = data.get('seeds')
exchanges = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']

collection = [seeds[i:i+2] for i in range(0, len(seeds), 2)]
print(collection)

seed_inputs = []

for it in collection:
    seed_inputs += list(range(int(it[0]), int(it[0]) + int(it[1])))

print(seed_inputs)

res = []
for s in seed_inputs:
    val = s
    for e in exchanges:
        codes = data.get(e)
        for c in codes:
            if int(val) >= int(c[1]) and int(val) <= (int(c[1]) + (int(c[2])-1)):
                val = int(c[0]) + abs((int(c[1])) - int(val))
                break
            else:
                None
    res.append(val)
    
print(res)
print(min(res))
        