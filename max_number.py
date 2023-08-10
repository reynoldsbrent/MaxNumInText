#Read the file line by line, delete the line break. As files can only contain strings, the number must now be converted into an integer.
#Add the number into a list. When all numbers are in the list, sort the list. Then print out the biggest numbers.

number_list = []
with open('numbers.txt', 'r') as file:
    for line in file:
        line = line.strip()
        line = int(line)
        number_list.append(line)

number_list.sort(reverse=True)
print(number_list[0])
print(number_list[1])
print(number_list[2])