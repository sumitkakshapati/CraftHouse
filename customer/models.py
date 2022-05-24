from django.db import models
from django.utils.translation import ugettext_lazy as _

from authemail.models import EmailAbstractUser,EmailUserManager
        
class User(EmailAbstractUser):

    objects = EmailUserManager()
    image = models.ImageField(upload_to ='user/',null=True,blank = True)
    date_of_birth = models.DateField(null = True, blank = True)

    def __str__(self):
        return self.first_name

class AddressBook(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, default = 0 )
    zone = models.CharField(max_length = 100)
    district= models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    address2 = models.CharField(max_length = 100)

    def __str__(self):
        return self.city

