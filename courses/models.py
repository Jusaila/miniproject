from django.db import models

# Create your models here.
class Courses(models.Model):
    co_id = models.AutoField(db_column='co-id', primary_key=True)  # Field renamed to remove unsuitable characters.
    c_id = models.IntegerField(db_column='c-id')  # Field renamed to remove unsuitable characters.
    courses = models.CharField(max_length=100)
    college = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'courses'
