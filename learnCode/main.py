from kivy import *

list1='item1', 'item2', 'item3', 'item4'
list2={'item1', 'item2', 'item3', 'item4'}   

print(list1[:])
print(list2)

print(list1[0], "en volgende item", list1[1:4])
#test

friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print ("iteration {iteration} is {name}".format(iteration=i, name=name))
    print('naam is', friends[0])