# dict = {2: ['A', 'B', 'C'], 3:['D', 'G, K']}
# index = [0, 1]
# num = 23
# word = []
# for i in range(len(index)):
#     word.append(dict[num[i]][index[i]])
#
#
#




# tuple = (1, 2, 3)
# for t in tuple:
#     print("Yes!")


#IMPORTANT!!!!
import itertools
lst = list(itertools.combinations('012'*4, 4))
print(len(set(lst)))
print((set(lst)))




# import string
# print(string.ascii_uppercase[0:6])