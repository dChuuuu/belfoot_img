from PIL import Image
import requests
import base64
import os

class Converter:
    '''_size_check - остаточная проверка изображения для корректировки по весу. Вызывается только изнутри класса
        resolution_check - проверка и редактирование изображения по количеству пикселейс использованием коэффициента,
         не менее 900х600'''

    def _size_check(self, image):

        file_size = os.stat('img_converter/temp/image.jpeg').st_size / (1024 * 1024)
        quality = 95
        while file_size > 0.18:
            image.save('img_converter/temp/image.jpeg', 'jpeg', optimize=True, quality=quality)
            quality -= 5
            file_size = os.stat('img_converter/temp/image.jpeg').st_size / (1024 * 1024)

        return image


    def resolution_check(self, response):
        with open('img_converter/temp/image.jpeg', 'wb') as image:
            image.write(response)
        image = Image.open('img_converter/temp/image.jpeg')
        file_size = os.stat('img_converter/temp/image.jpeg').st_size / (1024 * 1024)
        width, height = image.size
        factor = width / height - 1


        while file_size > 0.18 and (width * factor > 900 and height * factor > 600):
            resized_image = image.resize((int(width * factor), int(height * factor)))
            width, height = image.size

            resized_image.save('img_converter/temp/image.jpeg', 'jpeg')
            file_size = os.stat('img_converter/temp/image.jpeg').st_size / (1024 * 1024)


        return self._size_check(image)
