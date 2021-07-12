a = 100
b = 12.34
c = 1 + 5j
d = 'hello world'
e = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))

a = 10
b = 3
a += b
a *= a + 2
print(a)

f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))
# 在使用print函数输出时，也可以对字符串内容进行格式化处理，上面print函数中的字符串%1.f是一个占位符，稍后会由一个float类型的变量值替换掉它。同理，如果字符串中有%d，后面可以用一个int类型的变量值替换掉它，而%s会被字符串的值替换掉。除了这种格式化字符串的方式外，还可以用下面的方式来格式化字符串，其中{f:.1f}和{c:.1f}可以先看成是{f}和{c}，表示输出时会用变量f和变量c的值替换掉这两个占位符，后面的:.1f表示这是一个浮点数，小数点后保留1位有效数字。

year = int(input('请输入年份：'))
is_leap = year % 4 == 0 and year % 100 != 0 or \
   year % 400 == 0
print(is_leap)