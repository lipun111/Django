import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crudfbvproject.settings')
django.setup()

from webapp.models import *
from faker import Faker
from random import *
fake = Faker()


def fake_view(n):
    for i in range(n):
        eid = randint(1001, 9999)
        ename = fake.name()
        esal = randint(10000, 30000)
        eaddr = fake.city()
        emp_record = Employee.objects.get_or_create(eno=eid, ename=ename, esal=esal, eaddr=eaddr)
fake_view(30)
