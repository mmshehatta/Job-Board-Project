from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

def uploadProfileImage(instance , filename):
    imageName , extension = filename.split('.')
    return "accounts/%s.%s"%(instance.user , extension)

# ****************** City Model *******************************
class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# ****************** Profile Model *******************************
class Profile(models.Model):
    user = models.OneToOneField(User , related_name='user_peofile' , on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    image = models.ImageField(upload_to=uploadProfileImage)
    bio  = models.CharField(max_length=100)
    city = models.ForeignKey(City , related_name='user_city' , on_delete=models.CASCADE,null=True)
    def __str__(self):
        return str(self.user)


@receiver(post_save , sender=User)
def create_user_profile(sender , instance , created , **Kwargs):
    if created:
        Profile.objects.create(user=instance)


# def save_user_profile(sender , insatace , **Kwargs):
#     insatace.profile.save()

