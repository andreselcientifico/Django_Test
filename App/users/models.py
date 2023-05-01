from django.db import models

class User(models.Model):
    user_name = models.CharField("User Name",max_length=30)
    anonymous_name = models.CharField("Anonymous Name",max_length=30)
    password = models.CharField(max_length=16)
    email = models.EmailField()
    pub_date = models.DateTimeField("date published")


class Date_User(models.Model):
    Names = models.CharField("Names",max_length=20)
    Last_Names = models.CharField("Last Names",max_length=20)
    Number_phone = models.IntegerField()

    def __str__(self):
        return self.Names