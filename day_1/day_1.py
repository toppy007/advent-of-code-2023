with open ("input.txt", "r") as file:
    input = file.readlines()

def find_int(line):

    first = 0

    for char in line:
        if char.isdigit():
            first = char
            break
    
    return first

def convert_word_to_num(line):
    find = [('one','1'), ('two','2'), ('three','3'), ('four','4'), ('five','5'), ('six','6'), ('seven','7'), ('eight','8'), ('nine','9')]
    
    for word, num in find:
        while line.find(word) >= 0:
            index = line.find(word)
            if index >= 0:
                list_new = list(line)
                list_new.insert((index+2), num)
                line = "".join(list_new)
        
    return line     
            
total = 0

test = ('two1nine','eightwothree','abcone2threexyz','xtwone3four','4nineeightseven2','zoneight234','7pqrstsixteen')

for line in input:
    words = convert_word_to_num(line)
     
    first = find_int(words)
    reverse_line = words[::-1]
    secound = find_int(reverse_line)
    join = int(str(first) + str(secound))
    total += join

print(total)
        
            
