def main():
    """复制图片"""
    
    try:
        with open('10.png', 'rb') as fs:
            data = fs.read()
            print(type(data)) # <class 'bytes'>
        
        with open('110.png', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开')
    except IOError as e:
        print('读写文件出现错误！')
    print('程序执行结束')


if __name__ == '__main__':
    main()