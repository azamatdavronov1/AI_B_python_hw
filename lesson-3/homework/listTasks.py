# # 1
# def occurences(element, array):
#     count = 0
#     for i in array:
#         if i==element:
#             count+=1
#     return count
# arr = [1,2,3,4,5,1]
# number = 1
# result = occurences(number, arr)
# print(result)


##2
# def sum(array):
#     all = 0
#     for i in range(len(array)):
#         all = all + array[i]
#     return all
# array = [1,2,3,9]
# print(sum(array))


# #3
# def maximum(array):
#     largest = max(array)
#     return largest
# array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(maximum(array1))


# # 4
# def minimum(array):
#     largest = min(array)
#     return largest
# array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(minimum(array1))


# # 5
# def check(element, array):
#     if element in array:
#         return True
# array = [1,2,3,4,5,6,7,8,9]
# print(check(343 ,array))


# # 6
# def first(array):
#     first_element = array[0]
#     return first_element
# array = [1]
# try:
#     result = first(array)
#     print(result)
# except Exception as e:
#     print("Something went wrong")


# # 7
# def last(array):
#     last_element = array[len(array) - 1]
#     return last_element
# array = [1, 5, 6]
# try:
#     result = last(array)
#     print(result)
# except Exception as e:
#     print("Something went wrong")


# # 8
# def slice(original):
#     sliced = []
#     i = 0
#     while (len(sliced) < 3 and i < len(original)):
#         sliced.append(original[i])
#         i += 1
#     return sliced
# first_list = [1, 2, 3, 4, 5, 6]
# second_list = slice(first_list)
# print(second_list)


# # 9
# def reverse_list(array):
#     return array[::-1]
# array = [1,2,3,4,5,6,7,8,9]
# print(reverse_list(array))


# # 10
# def sorter(array):
#     return sorted(array)
# array = [1,2,3, 43, 1, 11, 32, 566, 44]
# print(sorter(array))


# # 11
# def remover(array):
#     unique = []
#     for num in array:
#         if num not in unique:
#             unique.append(num)
#     return unique
#
# array = [1, 22, 11, 11, 12, 33, 22]
# print(remover(array))


# # 12
# def inserter(index_num, array, element):
#     array.insert(index_num, element)
#     return array
# array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(inserter(4, array, 33))


# # 13
# def indexOfElement(element, array):
#     for i in range(len(array)):
#         if array[i] == element:
#             return i
# array = [1,2,3,4,5,6,7,8,9,10]
# print(indexOfElement(8, array))


# #14
# def emptyList(array):
#     if len(array) == 0:
#         return True
#     else:
#         return False
# array = [1]
# print(emptyList(array))


# #15
# def EvenNumbers(array):
#     new = []
#     for i in range(0, len(array)):
#         if array[i] % 2 == 0:
#             new.append(array[i])
#     return len(new)
# array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(EvenNumbers(array))


# #16
# def OddNumbers(numbers):
#     new = []
#     for i in range(0,len(numbers)):
#         if numbers[i] % 2 != 0:
#             new.append(numbers[i])
#     return len(new)
# array = [1,2,3,4,5,6,7,8,9,10]
# print(OddNumbers(array))


# #17
# def concatenate(list1, list2):
#     return list1 + list2
# array1 = [1, 2, 3, 4, 5]
# array2 = [6, 7, 8, 9, 10]
# print(concatenate(array1, array2))


# #18
# def sublist(list, sublist):
#     count = 0
#     for i in range(len(sublist)):
#         if sublist[i] in list:
#             count += 1
#     if count == len(sublist):
#         return True
#     else:
#         return False
#
# array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# subarray = [1,2,3,4,5,6,7,77]
# print(sublist(array,subarray))


# # 19
# def replacement(array, element, replacer):
#     indexElement = array.index(element)
#     for i in range(len(array)):
#         if array[i] == element:
#             array[i] = replacer
#     return array
# array = [1,2,3,4,5,6,7,8,9]
# print((replacement(array,3,111)))


# # 20
# def secondLargest(array):
#     the_largest = max(array)
#     array.remove(the_largest)
#     return max(array)
# array = [1,2,3,4,5,6,7,8,9]
# print(secondLargest(array))


# # 21
# def secondMin(array):
#     the_largest = min(array)
#     array.remove(the_largest)
#     return min(array)
# array = [1,2,3,4,5,6,7,8,9]
# print(secondMin(array))


# #22
# def EvenNumbers(array):
#     new = []
#     for i in range(0, len(array)):
#         if array[i] % 2 == 0:
#             new.append(array[i])
#     return new
# array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(EvenNumbers(array))


# #23
# def OddNumbers(numbers):
#     new = []
#     for i in range(0,len(numbers)):
#         if numbers[i] % 2 != 0:
#             new.append(numbers[i])
#     return new
# array = [1,2,3,4,5,6,7,8,9,10]
# print(OddNumbers(array))


# # 24
# def listLength(array):
#     return len(array)
# array = [1,2,3,4,5,6,7,8,9,10]
# print(listLength(array))


# #25
# def copy(original):
#     copied = original
#     return copied
# array = [1, 2, 4]
# print(copy(array))


# 26
# def middle(array):
#     if len(array) % 2 == 0:
#         middle1 = array[int(len(array) / 2)]
#         middle2 = array[int(len(array) / 2 + 1)]
#         print(middle1, middle2)
#     else:
#         middle_itself = array[int(len(array) / 2)]
#         print(middle_itself)
# array = [1,2,3,4,5,6,7,8,9,0]
# middle(array)


# # 27
# def maxSub(list, sublist):
#         count = 0
#         for i in range(len(sublist)):
#             if sublist[i] in list:
#                 count += 1
#         if count == len(sublist):
#             return max(sublist)
#         else:
#             return False
# array = [1,2,3,4,5,6,7,8,9,10]
# sublist = [1,2,3,4,5,6,7,8,9]
# print(maxSub(array, sublist))


# #28
# def minSub(list, sublist):
#     count = 0
#     for i in range(len(sublist)):
#         if sublist[i] in list:
#             count += 1
#     if count == len(sublist):
#         return min(sublist)
#     else:
#         return False
#
#
# array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sublist = [3, 4]
# print(minSub(array, sublist))


# # 29
# def removal(array, indexOfElement):
#     if indexOfElement <= len(array):
#         array.remove(array[indexOfElement])
#         return array
# array = [1,2,3,4,5,6,7,8,9]
# print(removal(array,0))


# #30
# def sortingChecker(array):
#     sortedArray = sorted(array)
#     if array == sortedArray:
#         return True
#     else:
#         return False
# array = [21,2,3,4,5,6,7,8,9,10]
# print(sortingChecker(array))


# # 31
# def repeater(array, number):
#     new_array = []
#     for i in range(len(array)):
#         for j in range(number):
#             new_array.append(array[i])
#     return new_array
# array = [1, 2, 3, 4, 5]
# print(repeater(array, 3))


# # 32
# def mergeAndSort(array1, array2):
#     newArray = array1 + array2
#     newArray.sort()
#     return newArray
# array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# array2 = [0, 111]
# print(mergeAndSort(array1, array2))


# #33
# def indices(array, element):
#     i = 0
#     count = 0
#     while i < len(array):
#         if array[i] == element:
#             count += 1
#         i += 1
#     return count
# array = [1,2,3,4,5,6,7,8,9,9,9]
# print(indices(array,9))


# # 34
# def rotate_list(nums, k):
#     if not nums:
#         return []
#     k %= len(nums)
#     return nums[-k:] + nums[:-k]
# nums = [1, 2, 3, 4, 5]
# k = 1
# print(rotate_list(nums, k))


# # 35
# def rangeList(start, stop, step):
#     array = []
#     for num in range(start, stop, step):
#         array.append(num)
#     return array
# array = rangeList(1, 10, 1)
# print(array)


# # 36
# def sumOfPlus(array):
#     sum = 0
#     for i in array:
#         if i > 0:
#             sum += i
#     return sum
# array = [1, 2, 3, 4, 5]
# print(sumOfPlus(array))


# # 37
# def sumOfNegative(array):
#     sum = 0
#     for i in array:
#         if i < 0:
#             sum += i
#     return sum
# array = [1,2,3,4,5]
# print(sumOfNegative(array))


# # 38
# def palindrome(array):
#     newish = array[::-1]
#     return newish == array
# array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(palindrome(array))


# # 39
# def create_nested_list(lst, n):
#     return [lst[i:i + n] for i in range(0, len(lst), n)]
# original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# nested_list = create_nested_list(original_list, 3)
# print(nested_list)


# # 40
# def uniqe(array):
#     newish = []
#     for i in array:
#         if i not in newish:
#             newish.append(i)
#     return newish
# print(uniqe([1, 2, 3, 4, 5, 5, 6, 6, 6, 1]))












































