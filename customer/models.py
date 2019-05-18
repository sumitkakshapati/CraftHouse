from django.db import models
from django.utils.translation import ugettext_lazy as _

from authemail.models import EmailAbstractUser,EmailUserManager
        
class User(EmailAbstractUser):

    objects = EmailUserManager()
    date_of_birth = models.DateField('Date of Birth', null = True, blank = True)
    phoneno = models.CharField(max_length = 255)
    image = models.ImageField(upload_to ='user/',null=True,blank = True)

    def __str__(self):
        return self.first_name

class AddressBook(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, default = 0 )
    zone = models.CharField(max_length = 100)
    district= models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)

    def __str__(self):
        return self.city

