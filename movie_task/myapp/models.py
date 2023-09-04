from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,UserManager
from django.utils.translation import gettext_lazy as _
from uuid import uuid4
from django.contrib.postgres.fields import ArrayField,JSONField
# Create your models here.


class Register(AbstractBaseUser):
    objects=UserManager()

    username=models.CharField(max_length=150,unique=True)
    email=models.CharField(max_length=100,unique=True)
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    


    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


class CollectionModel(models.Model):
    user=models.ForeignKey(Register,on_delete=models.CASCADE,related_name='info')
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=300,null=True,blank=True)
    uuid=models.UUIDField(default=uuid4, editable=False)
    movies=ArrayField(models.JSONField(blank=True,null=True))

    def __str__(self) -> str:
        return self.title


class CountModel(models.Model):
    count=models.IntegerField()






