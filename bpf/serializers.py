from rest_framework import serializers

from bpf.models import Organization, Employee



class EmployeeSerializer(serializers.ModelSerializer):
   class Meta:
       model = Employee
       fields = '__all__'

class OrganizationSerializer(serializers.ModelSerializer):
   employees=EmployeeSerializer(many=True, read_only=True)
   class Meta:
       model = Organization
       fields = '__all__'


