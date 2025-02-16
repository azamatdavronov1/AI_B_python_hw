# #1
# def union(set1, set2):
#     new = []
#     for i in set1:
#         if i not in new:
#             new.append(i)
#     for i in set2:
#         if i not in new:
#             new.append(i)
#     return set(new)
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# print(union(set1, set2))


## 2
# def intersection(set1, set2):
#     result = set()
#     for element in set1:
#         if element in set2:
#             result.add(element)
#     return result
#
# setA = {1, 2, 3, 4, 5}
# setB = {3, 4, 5, 6, 7}
# print(intersection(setA, setB))


# # 3
# def differenceOfSet(set1, set2):
#     setGen = set1.difference(set2)
#     return setGen
# setcha = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
# setcha2 = {1, 2, 99}
# print(differenceOfSet(setcha, setcha2))


# # 4
# def SubsetThing(set1, set2):
#     if set1.issubset(set2) or set2.issubset(set1):
#         return True
#     else:
#         return False
#
# set1 = {1, 2, 3, 4}
# set2 = {1, 2, 5}
# print(SubsetThing(set1, set2))


# # 5
# def checkIt(set1, element):
#     if element in set1:
#         return True
#     else:
#         return False
# set1 = {1, 2, 3}
# print(checkIt(set1, 0))


# #6
# def uniqueness(set1):
#     new = set()
#     for i in set1:
#         new.add(i)
#     return new
#
# sett = {1, 2, 3, 3, 4}
# print(uniqueness(sett))


# #7
# def list_to_set(lst):
#     return set(lst)
#
# lst = [1, 2, 2, 3, 4, 4, 5]
# unique_set = list_to_set(lst)
# print(unique_set)


# #8
# def remove_element(s, elem):
#     s.discard(elem)
#     return s
# s = {1, 2, 3, 4}
# s = remove_element(s, 3)
# print(s)


# # 9
# def clear_set(s):
#     return set()
# s = {1, 2, 3, 4}
# s = clear_set(s)
# print(s)


# # 10
# def is_set_empty(s):
#     return len(s) == 0
# s = set()
# print(is_set_empty(s))


# # 11
# def symmetric_difference(a, b):
#     new = set()
#     for i in a:
#         if i not in b:
#             new.add(i)
#     for i in b:
#         if i not in a:
#             new.add(i)
#     return new
# a = {1, 2, 3, 4, 5, 7}
# b = {1, 2, 3, 4, 5, 6}
# print(symmetric_difference(a, b))


# # 12
# def addElement(set1, element):
#     set1.add(element)
#     return set1
# sett = {1, 2, 3}
# print(addElement(sett, 4))


# # 13
# def popElement(set1):
#     set1.pop()
#     return set1
# sett = {1, 2, 3}
# print(popElement(sett))


# # 14
# def find_max(s):
#     return max(s) if s else None
# s = {1, 5, 3, 9, 2}
# print(find_max(s))


# # 15
# def find_min(s):
#     return min(s) if s else None
# s = {1, 5, 3, 9, 2}
# print(find_min(s))


# # 16
# def filter_even(s):
#     return {x for x in s if x % 2 == 0}
# s = {1, 2, 3, 4, 5, 6}
# print(filter_even(s))


# #17
# def filter_odd(s):
#     return {i for i in s if i % 2 != 0}
# s = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(filter_odd(s))


# # 18
# def createRange(start, stop):
#     return set(range(start, stop+1))
# print(createRange(1, 10))


# #19
# def mergeAndDeduplicate(list1, list2):
#     merged = list1 + list2
#     newish = []
#     for i in merged:
#         if i not in newish:
#             newish.append(i)
#     return set(newish)
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 155]
# print(mergeAndDeduplicate(list1, list2))


# # 20
# def checkDisjoint(s1, s2):
#     return s1.isdisjoint(s2)
# set1 = {1, 2,3}
# set2 = {3, 5,6}
# print(checkDisjoint(set1, set2))


# # 21
# def removeDup(lst):
#     new = set(lst)
#     very_new = set()
#     for i in new:
#         if i not in very_new:
#             very_new.add(i)
#     return list(very_new)
# print(removeDup([1,2,3,4,5,6,7,8,9, 9]))


# # 22
# def countUnique(lst):
#     new = set(lst)
#     very_new = set()
#     count = 0
#     for i in new:
#         if i not in very_new:
#             count += 1
#     return count
# lst = [1,2,3,4,5,6,7,8,9,10]
# print(countUnique(lst))


# # 23
# import random
# def generate_random_set(size, start, end):
#     return set(random.sample(range(start, end + 1), min(size, end - start + 1)))
# print(generate_random_set(5, 1, 10))




























