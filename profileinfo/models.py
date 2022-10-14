from django.db import models

# Create your models here.
class Profileinfo(models.Model):
    p_id = models.AutoField(db_column='p-id', primary_key=True)  # Field renamed to remove unsuitable characters.
    s_id = models.IntegerField(db_column='s-id')  # Field renamed to remove unsuitable characters.
    student_name = models.CharField(db_column='student name', max_length=50)  # Field renamed to remove unsuitable characters.
    student_phone = models.CharField(db_column='student phone',max_length=50)  # Field renamed to remove unsuitable characters.
    parent_name = models.CharField(db_column='parent name', max_length=50)  # Field renamed to remove unsuitable characters.
    parent_phone = models.CharField(db_column='parent phone', max_length=50)
    e_mail = models.CharField(db_column='e-mail', max_length=50)  # Field renamed to remove unsuitable characters.
    stream = models.CharField(max_length=50)
    hobbies = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'profileinfo'

