from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from rest_framework.decorators import api_view
from rest_framework.exceptions import ParseError
from rest_framework.response import Response


@api_view(['POST'])
def login(request):
    if 'email' not in request.data or 'password' not in request.data:
        raise ParseError()

    email = request.data['email']
    password = request.data['password']
    user = authenticate(request, username=email, password=password)

    if user is not None:
        django_login(request, user)
        return Response()
    else:
        raise ParseError()


@api_view(['POST'])
def logout(request):
    django_logout(request)
    return Response()
