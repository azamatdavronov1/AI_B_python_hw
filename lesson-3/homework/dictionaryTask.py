# # 1
# def get_value(dictionary, key, default_value=None):
#     return dictionary.get(key, default_value)
# my_dict = {"name": "Azamat", "age": 20, "city": "Tashkent"}
# print(get_value(my_dict, "age"))
# print(get_value(my_dict, "country", "Not Found"))


# # 2
# def check_key(dictionary, key):
#     return key in dictionary
# my_dict = {"name": "Azamat", "age": 20, "city": "Tashkent"}
# print(check_key(my_dict, "age"))


# # 3
# def numOfKeys(dictionary):
#     count = 0
#     for key in dictionary:
#         count +=1
#     return count
# d = {"thing" : "Cool", "Another" : "Cool"}
# print(numOfKeys(d))


## 4
# def allKeys(dictionary):
#     lst =[]
#     for i in dictionary:
#         lst.append(i)
#     return lst
# d = {"thing" : "Cool", "Another" : "Cool"}
# print(allKeys(d))


# # 5
# def allValues(dictionary):
#     lst = []
#     for key, value in dictionary.items():
#         lst.append(value)
#     return lst
# d = {"thing" : "Cool", "Another" : "Cool"}
# print(allValues(d))


# # 6
# def merge_dicts(dict1, dict2):
#     return dict1 | dict2
# a = {"name": "Azamat", "age": 20}
# b = {"city": "Tashkent", "country": "Uzbekistan"}
# merged = merge_dicts(a, b)
# print(merged)


# #7
# def remove_key(d, key):
#     d.pop(key, None)
#     return d
# print(remove_key({'a': 1, 'b': 2}, 'a'))


# # 8
# def clear_dict():
#     return {}
# print(clear_dict())


# # 9
# def isEmpty(dictionary):
#     return not bool(dictionary)
# print(isEmpty({'a':1, 'b':2, 'c':3}))


# #10
# def get_key_value(d, key):
#     return (key, d[key]) if key in d else None
# print(get_key_value({'a': 1, 'b': 2}, 'a'))


# # 11
# def updateValue(dictionary, key, value):
#     dictionary[key] = value
#     return dictionary
# print(updateValue({'a': 1, 'b': 2}, 'a', 'value'))


# # 12
# def count_value_occurrences(d, value):
#     return list(d.values()).count(value)
# print(count_value_occurrences({'a': 1, 'b': 2, 'c': 1}, 1))


# # 13
# def invert_dict(d):
#     return {value: key for key, value in d.items()}
# print(invert_dict({'a': 1, 'b': 2}))


# #14
# def allKeys(dictionary, value):
#     return [k for k, v in dictionary.items() if v == value]
# print(allKeys({'a': 1, 'b': 2, 'c': 3, 'd': 3}, 3))


# # 15
# def dictFromList(list1, list2):
#     return dict(zip(list1, list2))
# print(dictFromList([1,2,3],[3,4,5]))


# # 16
# def has_nested_dict(d):
#     return any(isinstance(v, dict) for v in d.values())
# print(has_nested_dict({'a': 1, 'b': {'c': 2}}))


# # 17
# def nestedValues(d, k1, k2):
#     return d.get(k1, {}).get(k2, {})
# print(nestedValues({"a":{"b":1}}, "a", "b"))


# #18
# from collections import defaultdict
# def create_default_dict(default_value):
#     return defaultdict(lambda: default_value)
# d = create_default_dict(0)
# print(d['a'])


# # 19
# def count_unique_values(d):
#     return len(set(d.values()))
# print(count_unique_values({'a': 1, 'b': 2, 'c': 1}))


# # 20
# def sort_dict_by_key(d):
#     return dict(sorted(d.items()))
# print(sort_dict_by_key({'b': 2, 'a': 1}))


# #21
# def sort_dict_by_value(dictionary):
#     return dict(sorted(dictionary.items(), key=lambda item: item[1]))
# print(sort_dict_by_value({"c": 1, "b": 2, "a": 3}))


# #22
# def filter_dict_by_value(d, condition):
#     return {k: v for k, v in d.items() if condition(v)}
# print(filter_dict_by_value({'a': 1, 'b': 2, 'c': 3}, lambda x: x > 1))


# # 23
# def checkCommonKeys(d1, d2):
#     return bool(set(d1.keys()).intersection(d2.keys()))
# print(checkCommonKeys({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))


# # 24
# def create_dict_from_tuple(tuples):
#     return dict(tuples)
# print(create_dict_from_tuple([('a', 1), ('b', 2)]))


# # 25
# def get_first_key_value(d):
#     return next(iter(d.items()), None)
# print(get_first_key_value({'a': 1, 'b': 2}))
# print(get_first_key_value({}))















