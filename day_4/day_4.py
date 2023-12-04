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

matches = find_matches()

total = 0
for i in matches:
    if i != 0:
        total_at = 1
        for x in range(1, i):
            total_at *=2
        total += total_at

print(total)
    