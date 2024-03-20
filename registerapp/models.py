from django.db import models

# Create your models here.
class Form(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField(default='')
    number = models.PositiveBigIntegerField(default=8000000)
    state = models.CharField(max_length = 100)
    dob = models.DateField()
    address = models.CharField(max_length = 450)
    course = models.CharField(max_length = 70, choices = [ 
        ('Course options','Course options'),
        ('Javascript','Javascript'),
        ('Python','Python'),
        ('Data Analysis','Data Analysis'),
        ('Graphics Design','Graphics Design'),
        ('Cyber-security','Cyber-security'),
        ('Graphics Design','Graphics Design'),
    ] ,blank=False,default='Course options')
    reg_date = models.DateTimeField(auto_now_add = True)
    start_date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.first_name