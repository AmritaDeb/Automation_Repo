# # count=0
# # for letters in 'Hello World':
# #     if letters=='l':
# #         count+=1
# # print(count)
# #
# # str = "amrita"
# # print(str[1:4])
# # print(str[4:-1])
# # print(str[:-1])
# # print(str[::-1])
#
# str = "amrita"
# ltr_count = 0
# str_count = 0
# result = []
# for letter in str:
#     ltr_count+=1
#     if letter not in result:
#         result.append(letter)
#     else:
#         print(letter)
#
# new_str = ''
# for i in result:
#     new_str += i
# print(result)
# print(new_str)
# print(ltr_count)

def countVowel(str):
    count = 0
    vowel = "aeiou"
    for i in str:
        if i in vowel:
            count += 1
    print(count)
countVowel("akedifoguhgvjheio")

s1 = "amrita"
s2 = "arpita"
print(set(s1))
l = list(set(s1) & set(s2))
print(l)

