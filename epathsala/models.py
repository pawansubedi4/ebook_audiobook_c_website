from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.

def validate_pdf(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError('Only PDF files are allowed.')
    
def validate_audio_file(value):
    valid_extensions = ['.mp3', '.m4a']
    if not any(value.name.lower().endswith(ext) for ext in valid_extensions):
        raise ValidationError('Only .mp3 and .m4a audio files are allowed.')
    

class Category(models.Model):
    c_name=models.CharField(max_length=100)
    description=models.TextField(default='non')

    def __str__(self):
        return self.c_name
    
class Ebook(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(default='default.jpg')
    price=models.IntegerField(default=0)
    detail=models.CharField(max_length=1000)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    author = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='epathsala/', validators=[validate_pdf])
    uploaded = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class audiobook(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(default='default.jpg')
    price=models.IntegerField(default=0)
    detail=models.CharField(max_length=1000)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    author = models.CharField(max_length=255)
    audio= models.FileField(upload_to='epathsala/',validators=[validate_audio_file])
    uploaded = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class comment(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    uploaded = models.DateTimeField(auto_now_add=True)