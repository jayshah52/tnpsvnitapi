from django.contrib.sites import requests
from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets, filters, permissions
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Student
from .serializers import StudentSerializer

class PermissionsPerMethodMixin(object):
    def get_permissions(self):
        """
        Allows overriding default permissions with @permission_classes
        """
        view = getattr(self, self.action)
        if hasattr(view, 'permission_classes'):
            return [permission_class() for permission_class in view.permission_classes]
        return super().get_permissions()

class StudentPagination(PageNumberPagination):
    page_size = 25


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated,]
    pagination_class = StudentPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('roll_no', 'name')

    def get_queryset(self):
        return self.queryset

    @action(detail=False, methods=['get'])
    def activate(self, request,*args, **kwargs):
        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host()
        post_url = "http://127.0.0.1:8100/djoser_auth/users/activation/"
        uid = request.query_params.get('uid')
        token = request.query_params.get('token')
        print("UID AND TOKEN", uid, token)
        post_data = {'uid': uid, 'token': token}
        result = requests.post(post_url, post_data)
        content = result.text
        print("COOO", content)
        return Response(content)

    @action(detail=False, methods=['get'])
    def get_student(self, request, *args, **kwargs):
        id = request.query_params.get('id')
        student = self.queryset.get(id=id)
        serializer = StudentSerializer(student, context={'request': request})
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def student_info(self, request, *args, **kwargs):
        student = self.queryset.get(username = request.user)
        serializer = StudentSerializer(student, context={'request':request})
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def update_info(self, request, *args, **kwargs):
        data = request.data
        Student.objects.filter(username=request.user).update(**request.data)
        student = self.queryset.get(username=request.user)
        serializer = StudentSerializer(student, context={'request': request})
        return Response(serializer.data)

