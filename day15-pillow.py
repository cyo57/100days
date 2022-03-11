from PIL import Image
import requests

path = './res/image.png'

image = Image.open(path)


# image.format, image.size, image.mode
# image.show()

def img_crop():
    '''图像的裁剪'''
    rect = 80, 80, 160, 160
    image.crop(rect).show()


def img_thumb():
    '''图像的缩略图'''
    size = [300, 300]
    image.thumbnail(size)
    image.show()


def img_guido():
    '''图像的缩放和粘贴'''
    pass


if __name__ == '__main__':
    # img_crop()
    img_thumb()
