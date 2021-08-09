# s3 = ''''''
# print(s3)

# s1 = '\'hello, world!\''
# print(s1)

# s2 = '\n\\hello, world!\\\n'
# print(s2)

# s1 = r'\'hello, world!\''
# s2 = r'\n\\hello, world!\\\n'
# print(s1, s2, end='')

s1 = 'hello' * 3
s2 = 'kitty'
s1 += s2

# print('k' in s1)
str = 'abc123456'
# print(str[-3::-1])

str1 = 'hello world'
# print(len(str1))
# print(str1.capitalize())
print(str1.title())
print(len(str1))
print(str1.capitalize())
print(str1.upper())
print(str1.center(50, '*'))
print(str1.rjust(50, ' '))
print(str1.isdigit())
print(str1.isalpha())
print(str1.isalnum())
print(str1.strip())

a, b = 5, 10
# py 3.6
print(f'{a} * {b} = {a * b}')