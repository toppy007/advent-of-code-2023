with open ('input.txt', 'r') as file:
    input = file.readlines()
    
split = False

workflow = []
part_rating = []

for i in input:
    if i == '\n':
        split = True
    if split == False:
        workflow.append(i.rstrip('}\n'))
    else:
        part_rating.append(i.rstrip('\n').strip('}{'))
        
part_dicts = []

for i in part_rating:
    parts_list = i.split(',')
    item_sec = {}
    for x in parts_list:
        item = x.split('=')
        item_sec.update([(item[0], item[1])])
    
    part_dicts.append(item_sec) 

workflow_dicts = []

for i in workflow:
    condition_codes = {}
    codes = []

    workflow_codes = i.split('{')
    condition_codes.update([('group', workflow_codes[0])])
    workflow_conditions = workflow_codes[1].split(',')
    
    for x in range(len(workflow_conditions)-1):
        cond = workflow_conditions[x].split(':')
        codes.append([cond[0], cond[1]])

    condition_codes.update([('codes', codes)])
    condition_codes.update([('last', workflow_conditions[-1])])
    workflow_dicts.append(condition_codes)

def split_workflow_algo(i, workflow_dicts):
    new_parts = []        
    workflow_dict = next(filter(lambda x: x['group'] == i.get('group'), workflow_dicts), None)
    
    for index, j in enumerate(workflow_dict['codes']):
        if j[0][0] in i:
            value = i.get(j[0][0])
            comparison_type = j[0][1]
            limit = j[0][2:]
        
        if comparison_type == '<':
            if value[0] <= int(limit) <= value[1]: 
                range_split1 = (value[0], int(limit)-1)
                range_split2 = (int(limit), value[1])
                
                next_part = i.copy()
                
                next_part.update([(j[0][0], range_split1)])
                i.update([(j[0][0], range_split2)])
                
                next_part.update([('group', j[1])])
                i.update([('group', workflow_dict['last'])])
                
        elif comparison_type == '>':
            if value[0] <= int(limit) <= value[1]:                    
                range_split1 = (value[0], int(limit))
                range_split2 = (int(limit)+1, value[1])

                next_part = i.copy()
                
                next_part.update([(j[0][0], range_split2)])
                i.update([(j[0][0], range_split1)])
                
                next_part.update([('group', j[1])])
                i.update([('group', workflow_dict['last'])])

        if len(workflow_dict['codes']) == index + 1:
            new_parts.append(i)
        new_parts.append(next_part)
    
    return new_parts

accepted_parts = []
proccessing = True
parts_dict = [{'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000), 'group': 'in'}]

while proccessing:
    new_parts_list = [] 
    for part in parts_dict:

        returned_parts = split_workflow_algo(part, workflow_dicts)
        print('these got returned', returned_parts)
        
        print(len(returned_parts))
        for i in returned_parts:
            if i.get('group') == 'R':
                None
            elif i.get('group') == 'A':
                accepted_parts.append(i)
            else:
                new_parts_list.append(i)
    
    parts_dict = new_parts_list   
    
    if len(new_parts_list) == 0:
        proccessing = False
 
total = 0   
for i in accepted_parts:
    score = 1
    score *= i['x'][1] - (i['x'][0]-1)
    score *= i['m'][1] - (i['m'][0]-1)
    score *= i['a'][1] - (i['a'][0]-1)
    score *= i['s'][1] - (i['s'][0]-1)
    total += score
    
print(total)