from django.db import models
from django.utils import timezone
import datetime

class Blog(models.Model):
    title = models.CharField(max_length=255)
    leader = models.CharField(max_length=255, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)  
    body = models.TextField()    
    photo_main = models.ImageField(upload_to='images/', blank=True)
    
    def __str__(self):
        return self.title
        
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    # academic_title = models.CharField(max_length=100, blank=True)
    # role_title = models.CharField(max_length=100, blank=True)
    # academic_degree = models.CharField(max_length=25, blank=True)
    # alma_mater = models.CharField(max_length=50, blank=True)
    # phone = models.CharField(max_length=25, blank=True)
    # email = models.CharField(max_length=100, blank=True)
    # web = models.CharField(max_length=100, blank=True)
    # carpentry = models.BooleanField(default=False)
    # py_lang = models.BooleanField(default=False)      
    # r_lang = models.BooleanField(default=False)
    