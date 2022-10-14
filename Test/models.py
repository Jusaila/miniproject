from django.db import models

# Create your models here.

class Test(models.Model):
    t_id = models.AutoField(db_column='t-id', primary_key=True)  # Field renamed to remove unsuitable characters.
    questions = models.CharField(db_column='Questions', max_length=200)  # Field name made lowercase.
    answers = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'Test'
