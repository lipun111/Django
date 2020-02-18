import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'modelproject3.settings')
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
        emp_record = Stu.objects.get_or_create(Sid=eid, Sname=ename, Ssal=esal, Saddr=eaddr)
fake_view(30)