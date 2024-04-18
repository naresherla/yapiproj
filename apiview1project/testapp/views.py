from django.shortcuts import render

# Create your views here.
from testapp.serializers import Employeeserializer
from testapp.models import Employee
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView,RetrieveAPIView
# from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# class Employeeapiview(APIView):
#     def get(self,request,format=None):
#         qs = Employee.objects.all()
#         serializer = Employeeserializer(qs,many=True)
#         return Response(serializer.data)

class Employeelistapiview(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = Employeeserializer

# class Employeeserachview(ListAPIView):
#     serializer_class = Employeeserializer
#     def get_queryset(self):
#         qs = Employee.objects.all()
#         name = self.request.GET.get('name')
#         if name is not None:
#             qs = qs.filter(ename__icontains=name)
#         return qs

class EmployeeRetriveApiview(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = Employeeserializer
    lookup_field = 'id'

class EmployeeCreateApiview(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = Employeeserializer

class EmployeeUpdateApiview(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = Employeeserializer
    lookup_field = 'id'

class EmployeeDestroyApiview(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = Employeeserializer

# class Employeelistcreateapiview(ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = Employeeserializer
# class EmployeeRetriveupdatedestroyApiview(RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = Employeeserializer
