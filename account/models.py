from django.db import models

# Create your models here.

class UserAccount(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255, null=True, blank=True)

  def __str__(self):
      return self.firstname
  

class Post(models.Model):
    user= models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
