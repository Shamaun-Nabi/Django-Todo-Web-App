from django.db import models

# Create your models here.
class TodoApp(models.Model):
    text=models.CharField(max_length=400)
    userDate=models.DateField(auto_now_add=True)
    
    def  __str__(self):
        return self.text