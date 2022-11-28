from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
class userDetails(models.Model):
    class Programme_choices(models.TextChoices):
        BTECH      = 'BT', _('BTech')
        MTECH      = 'MT', _('MTech')
        MEDICAL_UG = 'MU', _('Medical UG')
        MEDICAL_PG = 'MP', _('Medical PG')

    class Gender_choices(models.TextChoices):
        MALE      = 'M', _('Male')
        FEMALE    = 'F', _('Female')
        
    class Category_choices(models.TextChoices):
        GENERAL  = 'G', _('General')
        SC       = 'SC', _('SC')
        ST       = 'ST', _('ST')
        OBC      = 'OBC', _('Other backward Classes')
        EWS      = 'EWS', _('Economically Weaker Section')
        
    #  foreign ley is one to many relationships
    user     = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=12, blank=False)
    programme= models.CharField(max_length=12, choices=Programme_choices.choices)
    course   = models.CharField(max_length=50)
    gender   = models.CharField(max_length=2, choices=Gender_choices.choices)
    avatar   = models.ImageField(upload_to='avatar', blank=True)
    category = models.CharField(max_length=3, choices=Category_choices.choices)
    income   = models.IntegerField()
    #  add a field to add pk so thar it can be refereced

    def __str__(self):
        return self.user.first_name

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         userDetails.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()