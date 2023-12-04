with open ('input.txt', 'r') as file:
    input = file.readlines()
    
def data_structure(input):
    card_collection = []
    for line in input:
        card_data = {"card": 0, 'win_num': [], 'my_num': []}
        card = line.split(': ')
        score = card[1].split(' | ')
        
        card_number = card[0].split('Card ')
        winning_numbers = score[0].split(' ')
        filtered_win_nums = filter(None, winning_numbers)
        my_numbers = score[1].split(' ')
        filtered_my_nums = filter(None, my_numbers)
        
        card_data['card'] += int(''.join(card_number))
        card_data['win_num'] += filtered_win_nums
        card_data['my_num'] += filtered_my_nums
        card_collection.append(card_data)
        
    return card_collection

def find_matches():
    data_struc = data_structure(input)
    card_count = []

    for dict in data_struc:
        count = 0
        win_num = dict.get('win_num')
        my_num = dict.get('my_num')
        for i in win_num:
            for x in my_num:
                if int(i) == int(x):
                    count += 1
        card_count.append(count)
    return card_count

def total_of_wins():
    matches = find_matches()

    total = 0
    for i in matches:
        if i != 0:
            total_at = 1
            for x in range(1, i):
                total_at *=2
            total += total_at

    return total

def find_instances():
    matches = find_matches()
    list_of_cards = [1]*(len(matches))
    

    for index, i in enumerate(list_of_cards):
        cards = 0
        match = matches[index]
        print(list_of_cards[index])
        
        while cards < list_of_cards[index]:
            cards += 1
            for x in range(match):
                list_of_cards[index+x+1] = list_of_cards[index+x+1] + 1
                
    print(list_of_cards)
    print(sum(list_of_cards))
            
instance = find_instances()
