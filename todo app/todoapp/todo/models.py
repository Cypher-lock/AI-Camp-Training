from django.db import models

# Create your models here.
class actionlist(models.Model):
    id = models.IntegerField(primary_key = True) 
    task = models.CharField(max_length=500, blank=False)
    date_added = models.DateField(auto_now_add = True)

    class Meta:
        managed = True
        db_table = 'todo_actionlist'