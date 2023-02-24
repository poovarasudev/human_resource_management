from django.db import models
from core import db


# Create your models here.
class Employee(db.BaseModel):
    JOB_TYPE_PERMANENT = 'Permanent'
    JOB_TYPE_TEMPORARY = 'Temporary'
    JOB_TYPES = [
        (JOB_TYPE_PERMANENT, JOB_TYPE_PERMANENT),
        (JOB_TYPE_TEMPORARY, JOB_TYPE_TEMPORARY)
    ]

    EMPLOYEE_TYPE_TAILOR = 'Tailor'
    EMPLOYEE_TYPE_CUTTING_MASTER = 'Cutting Master'
    EMPLOYEE_TYPES = [
        (EMPLOYEE_TYPE_TAILOR, EMPLOYEE_TYPE_TAILOR),
        (EMPLOYEE_TYPE_CUTTING_MASTER, EMPLOYEE_TYPE_CUTTING_MASTER)
    ]

    name = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=50, unique=True, null=False, blank=False)
    aadhaar_number = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    job_type = models.CharField(max_length=200, choices=JOB_TYPES, default=JOB_TYPE_PERMANENT)
    employee_type = models.CharField(max_length=200, choices=EMPLOYEE_TYPES, default=EMPLOYEE_TYPE_CUTTING_MASTER)

    def __str__(self):
        return self.name


class Client(db.BaseModel):
    name = models.CharField(max_length=250)
    mobile_number = models.CharField(max_length=50, unique=True, null=False, blank=False)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.name

