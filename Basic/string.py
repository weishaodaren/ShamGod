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

list1 = [1, 3, 5, 7, 100]
print(len(list1))

for index in range(len(list1)):
    print(list1[index])
for elem in list1:
    print(elem)
for index, elem in enumerate(list1):
    print(index, elem)

list1.append(200)
list1.insert(1,400)
list1 +=[1000, 2000]

if 3 in list1:
    list1.remove(3)
if 1234 in list1:
    list1.remove(1234)

list1.pop(0)
list1.clear()
print(list1)


fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
print(fruits[1:4])
print(fruits[:])
print(fruits[::-1])


list2 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list3 = sorted(list2, reverse=True)
list4 = sorted(list2, key=len)
print(list3)
print(list4)

f = [a for a in range(1, 10)]
print(f)

f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)

import sys

f = [x ** 2 for x in range(1, 1000)]
print(sys.getsizeof(f))

f = (x ** 2 for x in range(1, 1000))
print(sys.getsizeof(f))
print(f)
for val in f:
    print(val)


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a

def main():
    for val in fib(20):
        print(val)

if __name__ == '__main__':
    main()


t = ('weishaodaren', 25, True, 'Shanghai')
print(t[-1])
for member in t:
    print(member)

t = ('K', 90, False, 'M78')
print(list(t))

print(tuple(list2))

set1 = {1, 2, 3, 4, 5, 2}
print(set1)
print('Length =', len(set1))

set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)

set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
print(set4)

set1.add(40)
set1.add(50)
set1.update([11, 22])
set1.discard(50)
set1.remove(1)
set1.pop()
print(set1)

print(set2 ^ set1, '^')
print(set2 & set1, '&')
print(set2 | set1, '|')
print(set2 - set1, '-')
print(set2 <= set1)
print(set2 , '=<2')
print(set1, '=<1')
