from json import dump

def main():
    """写入json"""

    mydict = {
      'name': 'weishaodaren',
      'age': 17,
      'phone': 911,
      'frineds': ['A', 'B'],
      'games':[
        {'brand': 'BYD', 'max_speed': 180},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 320}
      ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成！')


if __name__ == '__main__':
    main()