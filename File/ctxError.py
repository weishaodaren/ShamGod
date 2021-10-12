def main():
    try:
        """
        通过with关键字指定文件对象上下文环境
        离开时自动释放文件资源
        """ 
        with open('lala.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')

if __name__ == '__main__':
    main()
