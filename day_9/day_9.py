with open('input.txt', 'r') as file:
    input_lines = file.readlines()


clean = []
for line in input_lines:
    if line != '\n':
        clean.append(line.rstrip('\n'))

total = []

for line in clean:
    data = line.split(' ')
    for i in data:
        int_data = int(i)

    data = [int(i) for i in data]

    step = []
    count = 1
    reverse = data.reverse()
    step.append(data)

    for s in range(len(data) - 1, 0, -1):
        differences = []
        for i in range(len(data)-1, 0, -1):
            first = (int(data[i]))
            second = (int(data[i - 1]))
            
            differences.insert(0, (first - second))
        data = differences
        step.append(differences)

    next = 0
    for index in range(len(step)-1, 0, -1):

        add = step[index - 1][-1]
        next += add
    print(next)

    total.append(next)
print(sum(total))