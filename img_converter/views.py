from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


from img_converter import converter

import requests

from . import serializers
from . import models

import base64
from io import BytesIO

import os

import random

class ImageConverterAPI(APIView):


    def post(self, request):


        url = request.data['data']['url']
        article_id = request.data['data']['article_id']
        image_name = request.data['data']['image_name']
        response = requests.get(url).content

        image = converter.Converter().resolution_check(response)
        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue())



        instance = models.Images(image=str(img_str.decode("utf-8")), article_id=article_id, image_name=image_name)
        instance.save()
        data = {"image_name": f'{instance.image_name}',
                "image": f'{instance.image}'}

        os.remove(os.getcwd() + '/img_converter/temp/image.jpeg')

        return Response(data={"image_data": data}, status=status.HTTP_200_OK)

    def get(self, request):
        article_id = request.data['article_id']
        try:
          instance = models.Images.objects.get(article_id=article_id)
          data = {"article_id": f'{instance.article_id}',
                    "image_id": f'{instance.image_id}',
                    "image": f'{instance.image}'}
          return Response(data={"image_data": data}, status=status.HTTP_200_OK)
        except:
            return Response(data={"error": "not found"}, status=status.HTTP_404_NOT_FOUND)

