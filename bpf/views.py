from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import viewsets

from bpf.serializers import OrganizationSerializer, EmployeeSerializer
from bpf.models import Organization, Employee



class OrganizationViewSet(viewsets.ModelViewSet):
   queryset = Organization.objects.all()
   serializer_class = OrganizationSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
   queryset = Employee.objects.all()
   serializer_class = EmployeeSerializer