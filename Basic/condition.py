username = input('请输入用户名：')
password = input('请输入密码：')

if username == 'admin' and password == '123456' :
    print('Success')
else:
    print('Fail')

x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x>= -1:
    y = x + 2
else:
    y = 5 * x + 3
print('%.2f = %.2f' % (x, y))

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and a + c > b \
  and b + c > a :
    print('周长：%f' % (a + b + c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5 
    print('面积: %f' % (area))
else:
    print('No')