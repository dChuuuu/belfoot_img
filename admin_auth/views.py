from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


from img_converter import views

def admin_authorization(request=None, user=None):
    '''Представление для авторизации для доступа к API'''
    users = ['root1', 'root2']

    if user.username in users:

        return views.ImageConverterAPI().post(request=request)

    return Response({"error": "authorization failed"}, status.HTTP_403_FORBIDDEN)


class AdminAuthenticate(APIView):

    '''Обычная аутентификация для доступа к суперпользователю'''
    @csrf_exempt

    def post(self, request):

        if request.user.__str__() == 'AnonymousUser':
            username = request.data['user']['username']
            password = request.data['user']['password']
            user = authenticate(request, username=username, password=password)

            try:
                login(request, user)
            except:
                return Response({"error": "authorization failed"}, status.HTTP_403_FORBIDDEN)


            return admin_authorization(request=request, user=user)


        try:
            login(request, request.user)
        except:
            return Response({"error": "authorization failed"}, status.HTTP_403_FORBIDDEN)
        else:
            return Response(status.HTTP_200_OK)