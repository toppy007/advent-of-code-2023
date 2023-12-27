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

part_rating.pop(0)
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


def workflow_algo(i, workflow_dicts):
    group = ['in']
    accepted_parts = []

    while len(group) == 1:
        workflow_dict = next(filter(lambda x: x['group'] == group[-1], workflow_dicts), None)
        found = False
        for index, j in enumerate(workflow_dict['codes']):

            if j[0][0] in i:
                value = i.get(j[0][0])
                comparison_type = j[0][1]
                limit = j[0][2:]
    
            group.clear()
            if comparison_type == '>':
                if int(value) > int(limit):
                    if j[1] == 'R':
                        found = True
                    elif j[1] == 'A':
                        accepted_parts.append(i)
                        found = True
                    else:
                        group.append(j[1])
                        found = True
                
                else:
                    next_workflow = workflow_dict['last']
                    if index+1 == len(workflow_dict['codes']):
                        if next_workflow == 'R':
                            found = True
                        elif next_workflow == 'A':
                            accepted_parts.append(i)
                            found = True
                        else:
                            group.append(workflow_dict['last'])
                            found = True
                    
            elif comparison_type == '<':
                if int(value) < int(limit):
                    if j[1] == 'R':
                        found = True
                    elif j[1] == 'A':
                        accepted_parts.append(i)
                        found = True
                    else:
                        group.append(j[1])
                        found = True
                else:
                    next_workflow = workflow_dict['last']
                    if index+1 == len(workflow_dict['codes']):
                        if next_workflow == 'R':
                            found = True
                        elif next_workflow == 'A':
                            accepted_parts.append(i)
                            found = True
                        else:
                            group.append(workflow_dict['last'])
                            found = True
                    
            if found == True:
                break
            
    return accepted_parts

total = 0

for x in part_dicts:
    output = workflow_algo(x, workflow_dicts)
    if len(output) != 0:
        total += sum(int(value) for value in output[0].values())
        
print(total)