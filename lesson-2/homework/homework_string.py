# # 1st
# import datetime
# now = datetime.datetime.now()
# present =  now.year
# birthyear = input("Please enter your birthyear: ")
# age = now.year - int(birthyear)
# print(age)
import char

# # 2nd
# txt = "LMaasleitbtui"
# txt = txt.lower()
# cars = ["tesla", "bmw", "toyota", "chevrolet", "idk", "i"]
# found = [car for car in cars if car in txt]
# print(found)


# # 3rd
# value = str(input("Enter a word: "))
# print(len(value))
# valLower = value.lower()
# valUpper = value.upper()
# print(valLower)
# print(valUpper)


# # 4th
# word = str(input("Enter a word: "))
# reverse = word[::-1]
# print(reverse)
# if word == reverse:
#     print("The word is a palindrome")
# else:
#     print("The word is not a palindrome")


# #5th
# word = input("Enter a word: ")
# countV = 0
# countC = 0
# vowels = "aeiouAEIOU"
# length = len(word)
# for letter in word:
#     if letter in vowels:
#         countV += 1
#     else:
#         countC += 1
# print("Number of vowels: ", countV)
# print("Number of consonants: ", countC)


# # 6th
# word1 = str(input("Enter a word: "))
# word2 = str(input("Enter another word: "))
# if word1 in word2 or word2 in word1 or word1 == word2:
#     print("One string contains another")
# else:
#     print("they are independent")


# # 7th
# sentence = str(input("Enter a sentence: "))
# print(sentence)
# replacement = str(input("Enter a replacement: "))
# instead = str(input("Enter the word to replace: "))
# updated = sentence.replace(instead, replacement)
# print(updated)

# #8th
# word = input("Enter a word: ")
#
# print("Second character:", word[0] if len(word) > 1 else "not found")
# print("Last character:", word[-1])


# # 9th
# string = str(input("Enter a string: "))
# reversed = string[::-1]
# print(reversed)


# # 10th
# countS = 0
# sentence = str(input("Enter a sentence: "))
# space = " "
# for space in sentence:
#     countS += 1
#     if "." in sentence:
#         break
# print("there are ", countS + 1, " words in the sentence.")


# # 11th
# digits = "0123456789"
# sentence = str(input("Enter a sentence: "))
# for i in digits:
#     if i in sentence:
#         print(True)
#         break
# else:
#     print(False)


# # 12th
# words = []
# while True:
#     num = input("Enter a thing: ")
#     if num == "00":
#         break
#     words.append(num)
# print("-".join(words))


# # 13th
# word = input("Enter a word: ")
# result = word.replace(" ", "")
# print(result)


# # 14th
# w1 = input("Enter a string: ")
# w2 = input("Enter another string: ")
# if w1 == w2:
#     print("The strings are equal")
# else:
#     print("The strings are not equal")


# # 15th
# user_input = input("Enter several words: ")
# words = user_input.split()
# acro = "".join(word[0].upper() for word in words)
# print(acro)


# # 16th
# word = input("Enter a word: ")
# sign = input("Enter a character to remove: ")
# result = word.replace(sign, "")
# print("Updated word:", result)


# # 17th
# user_string = input("Enter a string: ")
# symbol = "*"
# vowels = "AEIOUaeiou"
# for vowel in vowels:
#     user_string = user_string.replace(vowel, symbol)
# print("Updated string:", user_string)


# #18
# sentence = input("Enter a sentence: ")
# words = sentence.split()
# first = words[0]
# last = words[-1]
# print("Start with: ", first)
# print("End with: ", last)



























