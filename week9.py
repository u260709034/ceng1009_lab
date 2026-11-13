# # # def is_odd(n):
# # #     return n % 2 == 1
# # #
# # #
# # #
# # # print(is_odd(12))
# #
# #
# # # def is_leap(year):
# # #     if year % 400 == 0:
# # #         return True
# # #     elif year % 100 == 0:
# # #         return False
# # #     elif year % 4 == 0:
# # #         return True
# # #     else:
# # #         return False
# # # print(is_leap(2026))
# #
# #
# #
# #
# # # def print_triangular_number(n):
# # #     total = 0
# # #     for i in range(1, n + 1):
# # #         total = total + i
# # #         print(i, total)
# # #
# # # print_triangular_number(10)
# #
# #
# #
# #
# #
# #
# # # def is_prime(n):
# # #     if n < 2:
# # #         return False
# # #     for i in  range(2, n):
# # #         if n % i == 0:
# # #             return False
# # #         return True
# # # print(is_prime(11))
# #
# #
# #
# #
# #
# # # def reverse(s):
# # #     result = ''
# # #     for ch in s:
# # #         result = ch + result
# # #     return result
# # # print(reverse("hello"))
# #
# #
# #
# # def remove_alloccurances(sub, s):
# #     return s.replace(sub, "")
# #
# # print(remove_alloccurances("l", "hello world"))
#
#
#
# # def substitute(message, key):
# #     alphabet = "abcçdefgğhıijklmnoöuüprsştyvz"
# #     result = ""
# #     for char in message:
# #         index = alphabet.find(ch.lower)
# #         if index == -1:
# #             result = result + char
# #     elif ch.isupper():
# #     result + result + key[index].upper()
# #     else:
# #     result = result + key[index].lower()
# #     return result
# #
# #
# # key = "qwertyıoüğ"
# # print(substitute("hello world", key)
#
#
#
#
# def remove_dots(s):
#     result = ""
#     for ch in s:
#         if ch not in result:
#             result = result + ch
#             return result
# print(remove_dots("yeah"))
#
#
