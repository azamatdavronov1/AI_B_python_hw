# # 1
# def numOccurences(tupl):
#     count = []
#     for i in tupl:
#         if i not in count:
#             count.append(i)
#     return len(count)
# tup1 = (1, 2, 3, 4, 5)
# print(numOccurences(tup1))


# # 2
# def maximum(tup):
#     return max(tup)
# tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(maximum(tup))


# # 3
# def minimum(tup):
#     return min(tup)
# tup = (1, 2, 3, 4)
# print(minimum(tup))


# # 4
# def checkIfExists(tup, element):
#     if element in tup:
#         return True
#     else:
#         return False
# tup = (1, 2, 3)
# print(checkIfExists(tup, 0))


# # 5
# def firstElement(tup):
#     if len(tup) == 0:
#         return None
#     else:
#         return tup[0]
# tup = (1, 2,3 ,4 )
# print(firstElement(tup))


# # 6
# def lastElement(tup):
#     if len(tup) == 0:
#         return None
#     else:
#         return tup[-1]
# tup = (1, 2, 3, 4)
# print(lastElement(tup))


# # 7
# def tupleLength(tup):
#     return len(tup)
# tup = (1, 2, 3, 4, 5)
# print(tupleLength(tup))


# # 8
# def sliceTuple(tup):
#     return tup[:3]
# tup = (1, 2, 3, 4, 5)
# print(sliceTuple(tup))


# # 9
# def concatenateTuples(tup1, tup2):
#     return tup1 + tup2
# tup1 = (1, 2, 3)
# tup2 = (4, 5, 6)
# print(concatenateTuples(tup1, tup2))


# # 10
# def isTupleEmpty(tup):
#     return len(tup) == 0
# tup = ()
# print(isTupleEmpty(tup))


# # 11
# def getAllIndices(tup, element):
#     return [i for i in range(len(tup)) if tup[i] == element]
# tup = (1, 2, 3, 2, 4, 2)
# print(getAllIndices(tup, 2))


# # 12
# def secondLargest(tup):
#     if len(tup) < 2:
#         return None
#     unique_sorted = sorted(set(tup), reverse=True)
#     return unique_sorted[1] if len(unique_sorted) > 1 else None
# tup = (1, 2, 3, 4, 5)
# print(secondLargest(tup))


# # 13
# def secondSmallest(tup):
#     if len(tup) < 2:
#         return None
#     unique_sorted = sorted(set(tup))
#     return unique_sorted[1] if len(unique_sorted) > 1 else None
# tup = (1, 2, 3, 4, 5)
# print(secondSmallest(tup))

# # 14
# def singleElementTuple(element):
#     return (element,)
# tup = singleElementTuple(5)
# print(tup)


# # 15
# def listToTuple(lst):
#     return tuple(lst)
# lst = [1, 2, 3, 4, 5]
# print(listToTuple(lst))


# # 16
# def ifSorted(tup):
#     return tup == tuple(sorted(tup))
# tup = (1, 2, 3, 4, 1)
# print(ifSorted(tup))


# #17
# def maxOfSub(tup, lengthOfSub, startingOfSub):
#     return max(tup[startingOfSub:startingOfSub + lengthOfSub])
# tup = (1, 2, 3, 4, 5, 6)
# print(maxOfSub(tup, 4, 1))


# # 18
# def minOfSub(tup, lengthOfSub, startingOfSub):
#     return min(tup[startingOfSub:startingOfSub + lengthOfSub])
# tup = (1, 2, 3, 4, 5, 6)
# print(minOfSub(tup, 4, 1))


# # 19
# def removal(tup, element):
#     return tuple(x for x in tup if x != element)
# tupl = (1, 2, 3, 4)
# print(removal(tupl, 2))


# # 20
# def create_nested_tuple(tup, n):
#     return tuple(tup[i:i + n] for i in range(0, len(tup), n))
# tuplecha = (1, 2, 3, 4, 5, 6, 7, 8)
# print(create_nested_tuple(tuplecha, 3))


# # 21
# def repeat_elements(tup, n):
#     return tuple(element for element in tup for _ in range(n))
# tuplecha = (1, 2, 3)
# print(repeat_elements(tuplecha, 3))


# # 22
# def rangeTuple(tup, start, end):
#     tup = sorted(tup)
#     start = tup[0]
#     end = tup[-1]
#     return range(start, end)
# tup = (1, 2, 3, 4, 5, 6, 7, 8)
# print(rangeTuple(tup, 0, len(tup)-1))


# # 23
# def reverseTuple(tup):
#     return tup[::-1]
# tup = (2, 3, 5)
# print(reverseTuple(tup))


#  #24
# def ifPalindrome(tup):
#     new_tup = tup[::-1]
#     if new_tup == tup:
#         return True
# tup = (1, 2, 1)
# print(ifPalindrome(tup))


# # 25
# def uniqueness(tup):
#     new = []
#     for i in tup:
#         if i not in new:
#             new.append(i)
#     return tuple(new)
# arr = (1, 2, 3, 4, 4, 5)
# print(uniqueness(arr))

































