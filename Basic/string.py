# # s3 = ''''''
# # print(s3)

# # s1 = '\'hello, world!\''
# # print(s1)

# # s2 = '\n\\hello, world!\\\n'
# # print(s2)

# # s1 = r'\'hello, world!\''
# # s2 = r'\n\\hello, world!\\\n'
# # print(s1, s2, end='')

# s1 = 'hello' * 3
# s2 = 'kitty'
# s1 += s2

# # print('k' in s1)
# str = 'abc123456'
# # print(str[-3::-1])

# str1 = 'hello world'
# # print(len(str1))
# # print(str1.capitalize())
# print(str1.title())
# print(len(str1))
# print(str1.capitalize())
# print(str1.upper())
# print(str1.center(50, '*'))
# print(str1.rjust(50, ' '))
# print(str1.isdigit())
# print(str1.isalpha())
# print(str1.isalnum())
# print(str1.strip())

# a, b = 5, 10
# # py 3.6
# print(f'{a} * {b} = {a * b}')

# list1 = [1, 3, 5, 7, 100]
# print(len(list1))

# for index in range(len(list1)):
#     print(list1[index])
# for elem in list1:
#     print(elem)
# for index, elem in enumerate(list1):
#     print(index, elem)

# list1.append(200)
# list1.insert(1,400)
# list1 +=[1000, 2000]

# if 3 in list1:
#     list1.remove(3)
# if 1234 in list1:
#     list1.remove(1234)

# list1.pop(0)
# list1.clear()
# print(list1)


# fruits = ['grape', 'apple', 'strawberry', 'waxberry']
# fruits += ['pitaya', 'pear', 'mango']
# print(fruits[1:4])
# print(fruits[:])
# print(fruits[::-1])


# list2 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
# list3 = sorted(list2, reverse=True)
# list4 = sorted(list2, key=len)
# print(list3)
# print(list4)

# f = [a for a in range(1, 10)]
# print(f)

# f = [x + y for x in 'ABCDE' for y in '1234567']
# print(f)

# import sys

# f = [x ** 2 for x in range(1, 1000)]
# print(sys.getsizeof(f))

# f = (x ** 2 for x in range(1, 1000))
# print(sys.getsizeof(f))
# print(f)
# for val in f:
#     print(val)


# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#         yield a

# def main():
#     for val in fib(20):
#         print(val)

# if __name__ == '__main__':
#     main()


# t = ('weishaodaren', 25, True, 'Shanghai')
# print(t[-1])
# for member in t:
#     print(member)

# t = ('K', 90, False, 'M78')
# print(list(t))

# print(tuple(list2))

# set1 = {1, 2, 3, 4, 5, 2}
# print(set1)
# print('Length =', len(set1))

# set2 = set(range(1, 10))
# set3 = set((1, 2, 3, 3, 2, 1))
# print(set2, set3)

# set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
# print(set4)

# set1.add(40)
# set1.add(50)
# set1.update([11, 22])
# set1.discard(50)
# set1.remove(1)
# set1.pop()
# print(set1)

# print(set2 ^ set1, '^')
# print(set2 & set1, '&')
# print(set2 | set1, '|')
# print(set2 - set1, '-')
# print(set2 <= set1)
# print(set2 , '=<2')
# print(set1, '=<1')

# scores = {'A': 95, 'B': 80, 'C': 60}
# print(scores)

# items = dict(one=1, two=2, three=3, four=4)
# items2 = dict(zip(['a', 'b', 'c'], '123'))
# items3 = {num: num ** 2 for num in range(1, 10)}
# print(items3)

# for key in scores:
#     print(f'{key}: {scores[key]}')

# scores.update(F=50, Z=0)
# print(scores.pop('A', 95))

# import os
# import time

# def main():
#     content = '叽叽喳喳嘻嘻嘻哈哈哈...'
#     while True:
#         os.system('cls')
#         print(content)
#         time.sleep(0.2)
#         content = content[1:] + content[0]

# if __name__ == '__main__':
#     main()

from random import randint

def generate_code(code_len=4):
    """
    生成指定长度的验证码
    :param code_len: 验证码的长度(默认4个字符)
    :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = randint(0, last_pos)
        code += all_chars[index]
    return code

print(generate_code(99))