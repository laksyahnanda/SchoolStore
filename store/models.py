from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # slug = models.SlugField(max_length=50, unique=True)
    wikipedia_link = models.URLField()

    class Meta:
        ordering=('name',)
        verbose_name='department'
        verbose_name_plural='departments'

    def __str__(self):
        return '{}'.format(self.name)

class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    # slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering=('name',)
        verbose_name='course'
        verbose_name_plural='courses'

    def __str__(self):
        return '{}'.format(self.name)

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    mail_id = models.EmailField()
    address = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    # course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=20)
    materials_provide = models.CharField(max_length=100)
    order_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.name