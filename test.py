# PART 1
# 1.
#import csv
#people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]
#for x in people:
#    print(x)
    
# 2.

#people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]
#file = open('people.txt', 'w+')
#for name in people:
#    file.write(name + '\n')


# 3.

#list = open('people.txt', 'r')
#new_list=[]
#for x in list:
#    new_list.append(x.strip())
#print(new_list)

# 4.

#d = {}
#with open('people.txt') as f:
#    for line in f:
#        (key, value) = line.split()
#        d[int(key)] = value
#print(d)

# PART 2

# 1.

#x = 0
#while x < 11:
#    print(x)
#    x = x + 1

# 2.

#x = 0
#for num in x:
#    if num < 11:
#        print(num)
#        num = num + 1
#    else:
#        break

# 3.

#nums = ["0", "2", "8", "20", "43", "82", "195", "204", "367"]

#for x in nums:
#   print(x)
#print('Done!')

# 4.

#list1 = ["apple", "banana", "cherry", "durian", "elderberry", "fig"]
#list2 = ["avocado", "banana", "coconut", "date", "elderberry", "fig"]
#list3 = []

#for l1 in list1:
#    for l2 in list2:
#        if l1 == l2:
#            list3.append(l2)
#print(list3)

# 5.

import random

x = random.randint(1, 100)

while x < 100:
    if x == x % 5:
        print('Number is divisable by 5')
        print(x)
        break
    elif x == x % 3:
        print('Number is divisable by 3')
        print(x)
        continue
    else:
        (None)
    