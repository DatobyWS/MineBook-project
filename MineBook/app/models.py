
from datetime import datetime
from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

# Create your models here.

# class Member(models.Model):
#     first_name = models.CharField(default="",max_length=50)
#     last_name = models.CharField(default="",max_length=100)
#     user_name = models.CharField(default="",max_length=50)
#     email = models.EmailField(default="",max_length=100)
#     passwd = models.CharField(default="",max_length=100)
#     img_skin = models.ImageField(default="",max_length=100)
    
#     def __str__(self):
#         return self.user_name + " " + self.email 




User = get_user_model()
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='proflie_images',default='profile-defilt.png')
    location = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.user.username 

User = get_user_model()
class Server_Page(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id_user = models.IntegerField(default="")
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='proflie_images',default='profile-defilt.png')
    ip = models.CharField(max_length=100,blank=True)
    server_name= models.CharField(max_length=100,blank=True)
    trailer=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.user.username 

class Status(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    time=models.CharField(blank=True,max_length=60)
    players=models.IntegerField()
    name=models.CharField(blank=True,max_length=60)
    def __str__(self):
        return self.user.username 

class Post(models.Model):
    id_post = models.UUIDField(primary_key=True,default=uuid.uuid4)
    user = models.CharField(max_length=100)
    img = models.ImageField(upload_to='post_images')
    caption = models.TextField() 
    created_at = models.DateTimeField(default=datetime.now)
    num_like = models.IntegerField(default=0)
    locaion = models.CharField(max_length=250)
    def __str__(self):
        return self.user


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(default='default.jpg', upload_to='profile_pics')

#     def __str__(self):
#         return f'{self.user.username} Profile'

#     def save(self, *args, **kwargs):
#         super().save()

#         img = Image.open(self.image.path)

#         if img.height > 300 or img.width > 300:
#             output_size = (300, 300)
#             img.thumbnail(output_size)
#             img.save(self.image.path)


# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     date_posted = models.DateTimeField(default=timezone.now)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title

#     def get_absolute_url(self):
#         return reverse('post-detail', kwargs={'pk': self.pk})