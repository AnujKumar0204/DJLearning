from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.

class UserAccount(models.Model):
  firstname = models.CharField(max_length=255, null=True, blank=True)
  lastname = models.CharField(max_length=255, null=True, blank=True)
  username = models.CharField(max_length=255, unique=True, )
  password = models.CharField(max_length=255, )
  
  def set_password(self, raw_password):
    # Hash the password before saving
    self.password = make_password(raw_password)
    
  def check_password(self, raw_password):
    # Check if the provided password matches the stored hash
    return check_password(raw_password, self.password)
  
  def __str__(self):
      return self.username
  

class Post(models.Model):
    user= models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    
class InterestCategory(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
      return self.name

class Interest(models.Model):
    category= models.ForeignKey(InterestCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
      return self.name
    
class UserInterestMap(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    # def __str__(self):
    #   return self.user
