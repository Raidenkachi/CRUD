from django.db import models

# Create your models here.
class Student(models.Model):
    firstname= models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    age=models.IntegerField(null=True)
    phonenumber=models.IntegerField(null=True)

    class Meta:
        db_table="Student"

    def __str__(self):
        return self.firstname+' '+ self.lastname


class Employee(models.Model):
    Name = models.CharField(max_length=50)
    Position = models.CharField(max_length=50)
    Office = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    Startdate = models.CharField(max_length=50)
    Salary = models.CharField(max_length=50)

    class Meta:
        db_table = "Add employee"

    def __str__(self):
        return self.Name + ' ' + self.Position


class Mobile(models.Model):
    VenueName = models.CharField(max_length= 50)
    Address = models.CharField(max_length=50)
    ZipPostCode = models.CharField(max_length=50)
    ContactPhone = models.CharField(max_length=50)
    WebAddress = models.CharField(max_length=50)
    EmailAddress = models.CharField(max_length=50)

    class Meta:
        db_table ="Add venue"

    def __str__(self):
        return self.VenueName + ' ' + self.Address