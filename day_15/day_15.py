with open ('input.txt', 'r') as file:
    input = file.readlines()

split_data = input[0].split(',')

main_total = 0
   
for code in split_data:
    current_value = 0 
    for i in code:
        current_value += ord(i)
        current_value = current_value * 17
        current_value = current_value % 256
    main_total += current_value
           
print(main_total)