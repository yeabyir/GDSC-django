total_sum = 0
count_three = 0
count_five = 0

for i in range(2, 51, 2):
    if i % 3 == 0:
        print("Three", end=", ")
        count_three += 1
    elif i % 5 == 0:
        print("Five", end=", ")
        count_five += 1
    else:
        print(i, end=", ")
    
    total_sum += i

print("\nTotal sum of even numbers from 1 to 50:", total_sum)
print("Count of numbers replaced with 'Three':", count_three)
print("Count of numbers replaced with 'Five':", count_five)
