from django.db import models

# Create your models here.

class Mail(models.Model):

    name=models.CharField(max_length=250, db_index=True)

    email = models.EmailField(max_length=254, unique=True, default='abxc@gmail.com')

    slug=models.SlugField(max_length=250, unique=True)

    #mobile_number = models.IntegerField(
    #    validators=[RegexValidator(r'^\d{10}$', message='Mobile number must be 10 digits')],
    #    unique=True,
    #    help_text='Enter your mobile number'
    #)

    mobile = models.CharField(max_length=16, unique=True, default='',help_text='Enter your mobile number')

    message=models.TextField(unique=False , default="this is simple message")

    #image=models.ImageField(upload_to='images/')


    class Meta:

        verbose_name_plural='E-mails'


# Mail(1) ,Mail(2) #return the name

    def _str_(self):

        return self.name


