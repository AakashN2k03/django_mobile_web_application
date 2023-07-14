from django.db import models
import datetime
import os


def getFileName(request,filename):
  now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
  new_filename="%s%s"%(now_time,filename)
  return os.path.join('uploads/',new_filename)

class category(models.Model):
  name=models.CharField(max_length=50,blank=False,null=False)
  image=models.ImageField(upload_to=getFileName,blank=True,null=True)
  description=models.TextField(max_length=300,null=False,blank=False)
  status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
  created_at=models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
     return self.name
  
class products(models.Model):
     key=models.ForeignKey(category,on_delete=models.CASCADE)
     name=models.CharField(max_length=30,blank=False,null=False)
     image=models.ImageField(upload_to=getFileName,blank=True,null=True)
     description=models.TextField(max_length=300,null=False,blank=False)
     status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
     trending=models.BooleanField(default=False,help_text="0-show,1-Hidden")
     quantity=models.IntegerField(null=False,blank=False)
     original_price=models.FloatField(null=False,blank=False)
     selling_price=models.FloatField(null=False,blank=False)
     created_at=models.DateTimeField(auto_now_add=True)

     def __str__(self):
      return self.name
     
class iphone(models.Model):
     name=models.CharField(max_length=30,blank=False,null=False)
     image=models.ImageField(upload_to=getFileName,blank=True,null=True)
     status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
     trending=models.BooleanField(default=False,help_text="0-show,1-Hidden")
     quantity=models.IntegerField(null=False,blank=False)
     original_price=models.FloatField(null=False,blank=False)
     selling_price=models.FloatField(null=False,blank=False)
     created_at=models.DateTimeField(auto_now_add=True)

     def __str__(self):
      return self.name     

class vivo(models.Model):
     name=models.CharField(max_length=30,blank=False,null=False)
     image=models.ImageField(upload_to=getFileName,blank=True,null=True)
     status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
     trending=models.BooleanField(default=False,help_text="0-show,1-Hidden")
     quantity=models.IntegerField(null=False,blank=False)
     original_price=models.FloatField(null=False,blank=False)
     selling_price=models.FloatField(null=False,blank=False)
     created_at=models.DateTimeField(auto_now_add=True)

     def __str__(self):
      return self.name     

class samsung(models.Model):
     name=models.CharField(max_length=30,blank=False,null=False)
     image=models.ImageField(upload_to=getFileName,blank=True,null=True)
     status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
     trending=models.BooleanField(default=False,help_text="0-show,1-Hidden")
     quantity=models.IntegerField(null=False,blank=False)
     original_price=models.FloatField(null=False,blank=False)
     selling_price=models.FloatField(null=False,blank=False)
     created_at=models.DateTimeField(auto_now_add=True)

     def __str__(self):
      return self.name      
class oneplus(models.Model):
     name=models.CharField(max_length=30,blank=False,null=False)
     image=models.ImageField(upload_to=getFileName,blank=True,null=True)
     status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
     trending=models.BooleanField(default=False,help_text="0-show,1-Hidden")
     quantity=models.IntegerField(null=False,blank=False)
     original_price=models.FloatField(null=False,blank=False)
     selling_price=models.FloatField(null=False,blank=False)
     created_at=models.DateTimeField(auto_now_add=True)

     def __str__(self):
      return self.name 
      
class redmi(models.Model):
     name=models.CharField(max_length=30,blank=False,null=False)
     image=models.ImageField(upload_to=getFileName,blank=True,null=True)
     status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
     trending=models.BooleanField(default=False,help_text="0-show,1-Hidden")
     quantity=models.IntegerField(null=False,blank=False)
     original_price=models.FloatField(null=False,blank=False)
     selling_price=models.FloatField(null=False,blank=False)
     created_at=models.DateTimeField(auto_now_add=True)

     def __str__(self):
      return self.name    

class tren(models.Model):
     name=models.CharField(max_length=30,blank=False,null=False)
     image=models.ImageField(upload_to=getFileName,blank=True,null=True)
     status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
     trending=models.BooleanField(default=False,help_text="0-show,1-Hidden")
     quantity=models.IntegerField(null=False,blank=False)
     original_price=models.FloatField(null=False,blank=False)
     selling_price=models.FloatField(null=False,blank=False)
     created_at=models.DateTimeField(auto_now_add=True)

     def __str__(self):
      return self.name                   
     
    

