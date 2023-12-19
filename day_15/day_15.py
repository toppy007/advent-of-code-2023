with open ('input.txt', 'r') as file:
    input = file.readlines()

data_list = []

split_data = input[0].split(',')

for i in split_data:
    label_dict = {}
    if '=' in i:
        label_dict.update([('operation', '=')])
        info = i.split('=')
        label_dict.update([('label', info[0])])
        label_dict.update([('focal length', info[1])])
    else:
        label_dict.update([('operation', '-')])
        info = i.split('-')
        label_dict.update([('label', info[0])])
       
    data_list.append(label_dict)


def hash_algo(code):
    current_value = 0 
    for i in code:
        current_value += ord(i)
        current_value = current_value * 17
        current_value = current_value % 256
    
    return current_value

boxes = []

for j in range(0, 255):
    box = { f'box {j}': [] }
    boxes.append(box)

for x in data_list:
    label = x.get('label')
    operation = x.get('operation')
    
    box = hash_algo(label)

    if operation == '=':
        get_box = f'box {box}'

        for individal_boxes in boxes:
            if get_box in individal_boxes:
                lens = individal_boxes.get(get_box)
                
                record_exists = False
                for i in range(len(lens)):
                    if lens[i]['label'] == label:
                        focal_length = x.get('focal length') 
                        lens[i].update({'focal length': focal_length})
                        record_exists = True
                        break

                if not record_exists:
                    individal_boxes[get_box].append(x)

    else:
        get_box = f'box {box}'

        for individal_boxes in boxes:
            if get_box in individal_boxes:
                lens = individal_boxes.get(get_box)
                
                for i in range(len(lens)):
                    if lens[i]['label'] == label:
                        del lens[i]
                        break
                                 

lens_total = 0               
for index, i in enumerate(boxes):
    box_number = (index + 1)
    get_box = f'box {index}'
    box_list = i.get(get_box)
    for j in range(len(box_list)):
        focal_length = box_list[j]['focal length']
        print(box_number, j+1, int(focal_length))
        
        len_total = (box_number * (j+1)) * int(focal_length)
        lens_total += len_total
        
    print('-----------')

print(lens_total)
        
        
    
    
    