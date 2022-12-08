from django.db import models

class Workshop(models.Model):
    name        = models.CharField(max_length=50)
    date        = models.DateField()
    venue       = models.CharField(max_length=100)
    provider    = models.CharField(max_length=50)
    logo        = models.ImageField(upload_to='workshop/logo', blank=True)
    details     = models.TextField()
    link        = models.CharField(max_length=100)
    price       = models.IntegerField()
    points      = models.IntegerField()
    certificate = models.FileField(upload_to='workshop/certificate', blank=True)
 
    def __str__(self):
        return self.name

class Lecture(models.Model):
    name        = models.CharField(max_length=50)
    date        = models.DateField()
    venue       = models.CharField(max_length=100)
    provider    = models.CharField(max_length=50)
    logo        = models.ImageField(upload_to='lecture/logo', blank=True)
    details     = models.TextField()
    link        = models.CharField(max_length=100)
    price       = models.IntegerField()
    points      = models.IntegerField()
    certificate = models.FileField(upload_to='lecture/certificate', blank=True)
    speaker     = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
        
class Exam(models.Model):
    name        = models.CharField(max_length=50)
    date        = models.DateField()
    venue       = models.CharField(max_length=100)
    provider    = models.CharField(max_length=50)
    logo        = models.ImageField(upload_to='exam/logo', blank=True)
    details     = models.TextField()
    link        = models.CharField(max_length=100)
    price       = models.IntegerField()
    points      = models.IntegerField()
    certificate = models.FileField(upload_to='exam/certificate', blank=True)
    eligibility = models.CharField(max_length=50)   
    
    def __str__(self):
        return self.name