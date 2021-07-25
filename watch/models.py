from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    profile_pic= CloudinaryField('image' )
    bio = models.TextField(blank=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=50, blank=False)
    neighbourhood = models.ForeignKey('Neighbourhood', on_delete=models.SET_NULL, null=True, related_name='members', blank=True)
    
    def __str__(self):
        return "%s profile" % self.user

    
    def save_profile(self):
        self.save()
        
        
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()