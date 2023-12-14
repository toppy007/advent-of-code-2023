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

def find_short_side(data, line1, line2):
    difference1 = abs(line1 - 0)
    difference2 = abs(line2 - len(data))

    print(difference1, difference2)
    return min(difference1, difference2)

def true_or_false(data, line1, line2):
    dif1 = line1 - 0 
    dif2 = len(data) - line2 
    
    if dif1 < dif2:
        print('the mirror start', len(data), line1, line2)
        return 0
    elif dif1 >= dif2:
        print('the mirror at the end')
        return 1


trans_total = []
all_true = True
total = []
count = 0

for data in result:
    count+= 1
    print('loooking at first mirror', count)
    for d in data:
        print(d)
    for i in range(len(data)-1):
        pair = compare_line(data[i], data[i+1])
        if pair == True:
            start_point = find_short_side(data, i, i+1)
            side = true_or_false(data, i, i+1)
            
            condition_results = ""
            up_value = (i)
            
            if side == 0:
                for x in range(0, start_point+1):
                    print(condition_results)
                    print('is lower', start_point, condition_results, i-x, i+1+x)
                    pair = compare_line(data[i-x], data[i+1+x])
                    condition_results += str(pair)
            elif side == 1:
                for x in range(0, start_point):
                    print('is higher', start_point, condition_results, i-x, i+1+x)
                    pair = compare_line(data[i-x], data[i+1+x])
                    print(data[i-x], data[i+1+x])
                    condition_results += str(pair)
                    print(condition_results)
            
            if 'False' not in condition_results:
                print(condition_results)
                print('mirror found')
                trans_total.append(i+1)
                break
                
    else:
        print('loooking at transposed mirror')
        trans = transpose_reflection(data)
        for t in trans:
            print(t)

        for i in range(len(trans)-1):
            pair = compare_line(trans[i], trans[i+1])
            print(pair)
            if pair == True:
                print(i, i+1)
        
                start_point = find_short_side(trans, i, i+1)
                side = true_or_false(trans, i, i+1)

                condition_results = ""
                up_value = (i)
                
                if side == 0:
                    print('is lowed than half')
                    for x in range(0, start_point+1):
                        print(start_point, condition_results, i-x, i+1+x)
                        pair = compare_line(trans[i-x], trans[i+1+x])
                        print(condition_results)
                        condition_results += str(pair)
                elif side == 1:   
                    for x in range(0, start_point):
                        print(start_point, condition_results, i-x, i+1+x)
                        print(condition_results)
                        pair = compare_line(trans[i-x], trans[i+1+x])
                        condition_results += str(pair)
                        
                if 'False' not in condition_results:
                    print(condition_results)
                    print('mirror found')
                    total.append(i+1)
    
                    break


print(total)
print(trans_total)


print(sum(total))
print(sum(trans_total))
print(sum(total) + ((sum(trans_total))*100))