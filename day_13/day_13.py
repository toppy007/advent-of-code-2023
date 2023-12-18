with open ('input.txt', 'r') as file:
    input = file.readlines()

result = []
current_sublist = []

for line in input:
    item = line.rstrip('\n')
    if not item.strip():
        result.append(current_sublist)
        current_sublist = []
    else:
        current_sublist.append(list(item))

if current_sublist:
    result.append(current_sublist)

def transpose_reflection(original):
    transposed = []
    for i in range(len(original[0])):
        line = []
        for item in original:
            line.append(item[i])
        transposed.append(line)
    return transposed

def compare_line(line1, line2):
    for i in range(len(line1)):
        if line1[i] != line2[i]:
            return False

    return True

def compare_line_smug(data):
    new_data = [list(line) for line in data]

    for i, line1 in enumerate(new_data):
        for j, line2 in enumerate(new_data):
            print(line1, j)
            print(line2, i)
            
            print ("------------") 
            if i != j:
                
                count = 0
                record = 0

                for x in range(len(line1)):
                    if line1[x] != line2[x]:
                        record = x
                        count += 1
                
                if count == 1:
                    new_data[i][record] = '#'
                    new_data[j][record] = '#'
                    break

    return new_data


def find_short_side(data, line1, line2):
    difference1 = abs(line1 - 0)
    difference2 = abs(line2 - len(data))

    return min(difference1, difference2)

def true_or_false(data, line1, line2):
    dif1 = line1 - 0 
    dif2 = len(data) - line2 
    
    if dif1 < dif2:
        return 0
    elif dif1 >= dif2:
        return 1

trans_total = []
trans_total_old = []
all_true = True
total = []
final = []

for data in result:
    trans_tot = 0
    trans_tot_old = 0
    tot = 0
    smug = compare_line_smug(data)
    
    old_col = []
    new_col = []
    
    for i in range(len(data)-1):
        print(data[i])
        pair2 = compare_line(data[i], data[i+1])
        if pair2 == True:
            start_point = find_short_side(data, i, i+1)

            side = true_or_false(data, i, i+1)
    
            condition_results = ""
            up_value = (i)
            
            if side == 0:
                for x in range(0, start_point+1):
                    pair = compare_line(data[i-x], data[i+1+x])
                    condition_results += str(pair)
            elif side == 1:
                for x in range(0, start_point):
                    pair = compare_line(data[i-x], data[i+1+x])
                    condition_results += str(pair)
            if 'False' not in condition_results:
                old_col.append(i+1)
    
    print('-------------')
    
    for i in range(len(smug)-1):
        pair2 = compare_line(smug[i], smug[i+1])
        print(smug[i])
        if pair2 == True:
            start_point = find_short_side(smug, i, i+1)
            side = true_or_false(smug, i, i+1)
    
            condition_results = ""
            up_value = (i)
            
            if side == 0:
                for x in range(0, start_point+1):
                    pair = compare_line(smug[i-x], smug[i+1+x])
                    condition_results += str(pair)
            elif side == 1:
                for x in range(0, start_point):
                    pair = compare_line(smug[i-x], smug[i+1+x])
                    condition_results += str(pair)
            if 'False' not in condition_results:
                print('try', i+1)
                new_col.append(i+1)
                
    print(new_col, old_col)
    
    for i in old_col:
        new_col.remove(i)
    
    if len(new_col) > 0:       
        trans_tot_old = new_col[0] 
            
    trans = transpose_reflection(data)
    trans_smug = compare_line_smug(trans)
    
    old = []
    new = []

    for i in range(len(trans)-1):
        pair = compare_line(trans[i], trans[i+1])
        if pair == True:
            
            start_point = find_short_side(trans, i, i+1)
            side = true_or_false(trans, i, i+1)

            condition_results = ""
            up_value = (i)
            
            if side == 0:
                for x in range(0, start_point+1):
                    pair = compare_line(trans[i-x], trans[i+1+x])
                    condition_results += str(pair)
            elif side == 1:   
                for x in range(0, start_point):
                    pair = compare_line(trans[i-x], trans[i+1+x])
                    condition_results += str(pair) 
            if 'False' not in condition_results:
                old.append(i+1)
            
    for i in range(len(trans_smug)-1):
        pair = compare_line(trans_smug[i], trans_smug[i+1])
        if pair == True:
            start_point = find_short_side(trans_smug, i, i+1)
            side = true_or_false(trans_smug, i, i+1)

            condition_results = ""
            up_value = (i)
            
            if side == 0:
                for x in range(0, start_point+1):
                    pair = compare_line(trans_smug[i-x], trans_smug[i+1+x])
                    condition_results += str(pair)
            elif side == 1:   
                for x in range(0, start_point):
                    pair = compare_line(trans_smug[i-x], trans_smug[i+1+x])
                    condition_results += str(pair)      
            if 'False' not in condition_results:
                new.append(i+1)
        
    for i in old:
        new.remove(i)
    
    if len(new) > 0:       
        tot = new[0]        

    if trans_tot == trans_tot_old:
        final.append(tot)
    else:
        trans_tot *= 100
        final.append(trans_tot)

print(trans_total_old)
print(trans_total)
print('total',total)
print(final)
print((sum(final))) 