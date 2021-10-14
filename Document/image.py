from PIL import Image

def main():
    image = Image.open('./12.png')
    print(image)
    image = image.convert('1')
    print(image.mode)
    image = image.convert('L')


if __name__ == '__main__':
    main()