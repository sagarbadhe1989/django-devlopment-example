from django.db import models

class Employee(models.Model):
    Employee_Code= models.CharField(max_length=264,unique=True)
    Name= models.TextField()
    Gender = models.CharField(max_length=264,unique=False)
    Age = models.CharField(max_length=264,unique=False)
    Birth_Date = models.DateField()
    boolean = models.BooleanField(default=False)
    integer = models.IntegerField(blank=True, null=True)
    photo = models.ImageField(upload_to ='blog/%Y/%m/%d')

    def __str__(self):
        return self.Employee_Code

class Employment(models.Model):
    Employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='employment')
    Joining_Date = models.DateField()
    Confirmation_Date = models.DateField()
    Probation_Date = models.DateField()
    Last_Increment_Given_On = models.DateField()
    Employment_status = models.CharField(max_length=264,unique=False)
    Resign_offer_Date = models.DateField()

    def __str__(self):
        return self.Employment_status
