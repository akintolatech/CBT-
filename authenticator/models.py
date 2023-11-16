from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django import forms


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        user = self.model(username=username)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    classes = models.CharField(max_length=50)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Class(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Test(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='course/')
    # taken = models.BooleanField(default=False)
    # description = name = models.CharField(max_length=200)
    classes = models.ForeignKey(Class, on_delete=models.CASCADE)
    written_by = models.ManyToManyField(CustomUser, related_name='written_tests')

    def __str__(self):
        return self.name

class Question(models.Model):
    question_text = models.CharField(max_length=500)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    A = models.CharField(max_length=100)
    B = models.CharField(max_length=100)
    C = models.CharField(max_length=100)
    D = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=100)

    def __str__(self):
        return self.question_text


class TestResult(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    svc_no = models.CharField(max_length=100)
    score = models.IntegerField()
    classes = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    date = models.DateTimeField('date submitted')

    def __str__(self):
        return f"{str(self.user)} {self.test.name} Test Result"
