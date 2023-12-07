with open ('input.txt', 'r') as file:
    input = file.readlines()

hands_bids = []

for line in input:
    data = {}
    clean = line.split(' ')
    data.update([('hand', list(clean[0]))])
    data.update([('bid', clean[1])])
    hands_bids.append(data)
    
convert = [['A', '14'], ['K', '13'], ['Q', '12'], ['J', '11'], ['T', '10']]

for i in hands_bids:
    hand = i.get('hand')
    for c in convert:
        hand = list(map(lambda x: x.replace(c[0], c[1]), hand))
    i.update([('hand', hand)])
    
five_of_kind = []
four_of_a_kind = []
full_house = []
three_of_kind = []
two_pair = []
one_pair = []
high_card = []

for x in hands_bids:
    hand = x.get('hand')
    count = [hand.count(x) for x in set(hand)]
    count = sorted(count)
    x.update([('set of the same', count[-1])])
    x.update([('uniqe count' , len(count))])
    x.update([('order value', count[-1] - len(count))])
    if (count[-1] - len(count)) == 4:
        five_of_kind.append(x)
    elif (count[-1] - len(count)) == 2:
        four_of_a_kind.append(x)
    elif (count[-1] - len(count)) == 1:
        full_house.append(x)
    elif (count[-1] - len(count)) == 0:
        three_of_kind.append(x)
    elif (count[-1] - len(count)) == -1:
        two_pair.append(x)
    elif (count[-1] - len(count)) == -2:
        one_pair.append(x)
    elif (count[-1] - len(count)) == -4:
        high_card.append(x)
        
lists = [five_of_kind, four_of_a_kind, full_house, three_of_kind, two_pair, one_pair, high_card]
finalseq = []

for x in lists:
    sorted_list = []
    for dict in x:
        hand = dict.get('hand')
        bid = dict.get('bid')
        hand.append(bid)
        sorted_list.append(list(map(int, hand)))
    sorted_list = sorted(sorted_list, key=lambda x: (x, x[5]), reverse=True)
    finalseq += (sorted_list)

total = 0   
times = len(finalseq)       
for index, i in enumerate(finalseq):
    total += i[5] * times
    times -= 1

print(total)