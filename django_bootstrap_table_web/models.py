from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1, default="男")
    age = models.IntegerField(default=0)
    phone = models.CharField(max_length=11, default="")
    adddate = models.IntegerField(default=0)

    def __str__(self):
        return self.name


def user2dict(obj):
    if isinstance(obj, User):
        return {
            "id": obj.id,
            "name": obj.name,
            "age": obj.age,
            "sex": obj.sex,
            "phone": obj.phone,
            "adddate": obj.adddate,
        }
    else:
        return obj
