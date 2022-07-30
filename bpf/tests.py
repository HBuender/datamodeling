from django.test import TestCase

from bpf.models import Organization, Employee
# Create your tests here.

class OrganizationTestCase(TestCase):
    def setUp(self):
        self.Organization=Organization.objects.create(name="Serviceware")

    def test_Organization(self):
        serviceware = Organization.objects.get(name="Serviceware")
        self.assertEquals(serviceware.name, "Serviceware")
class EmployeeTestCase(TestCase):
    def setUp(self):
        self.Organization=Organization.objects.create(name="Serviceware")
        self.Employee = Employee.objects.create(first_name="Hans", last_name="Hagen", organization=Organization.objects.get(name="Serviceware"))

    def test_Employee(self):
        hans=Employee.objects.get(first_name="Hans")
        self.assertEquals(hans.first_name, "Hans")