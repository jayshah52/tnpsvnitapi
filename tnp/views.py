# from rest_framework.views import APIView
# from rest_framework.response import Response
# import requests
#
# class UserActivationView(APIView):
#     def get (self, request, uid, token):
#         protocol = 'https://' if request.is_secure() else 'http://'
#         web_url = protocol + request.get_host()
#         post_url = "http://127.0.0.1:8000/djoser_auth/users/activation/"
#         post_data = {'uid': uid, 'token': token}
#         result = requests.post(post_url, data = post_data)
#         content = result.text
#         return Response(content)

from rest_framework import permissions
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from rest_framework.response import Response
from rest_framework.views import APIView

import requests


@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def request_user_activation(request,):
    """
    Intermediate view to activate a user's email.
    """
    post_url = "http://127.0.0.1:8100/api/v1/users/activation/"
    uid = request.query_params.get('uid')
    token = request.query_params.get('token')
    print("UID AND TOKEN", uid, token)
    post_data = {"uid": uid, "token": token}
    result = requests.post(post_url, data=post_data)
    content = result.text
    return Response(content)