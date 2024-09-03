from django.db import models

# Create your models here.

class test(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    t_name = models.CharField(max_length=250)

    class Meta:
        db_table = "test"

class user(models.Model):
    user_id = models.AutoField(primary_key=True, null=False,)
    name = models.CharField(max_length=250, null=False)
    email = models.EmailField(max_length=250, null=False)
    created_by = models.DateTimeField(auto_now_add=True)
    updated_by = models.DateTimeField()

    class Meta:
        db_table = 'user'

class user_auth(models.Model):
    user_id = models.ForeignKey(user, db_column='user_id', null=False, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=250, null=False)
    password = models.CharField(max_length=250, null=False)

    class Meta:
        db_table = 'user_auth'