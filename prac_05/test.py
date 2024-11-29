import operator
from operator import itemgetter
dict_of_names = {'Derek' : 7, 'Xaiver' : 80, 'Bob' : 612, 'Chantelle' : 9}
list_of_names = list(dict_of_names.items())
list_of_names.sort(key=operator.itemgetter(1), reverse=True)

longest_word = 0
for name in list_of_names:
    longest_word = len(name[0])
    print(longest_word)
    if longest_word < len(name[0]):
        longest_word = len(name[0])
    else:
        pass

for name in list_of_names:
    print(longest_word)
    print(f"{name[0] :{longest_word}} = {name[1]}")
