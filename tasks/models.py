from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
# from django.utils import timezone
# import datetime


# Create your models here.

class XxnfTasks(models.Model):
    task_id = models.AutoField(primary_key=True)
    set_num = models.IntegerField(blank=True, null=True)
    round_num = models.IntegerField(blank=True, null=True)
    question_num = models.IntegerField(blank=True, null=True)
    topic = models.CharField(max_length=120, blank=True, null=True)
    description = models.CharField(max_length=5000, blank=True, null=True)
    owner = models.CharField(max_length=120, blank=True, null=True)
    status = models.CharField(max_length=25, blank=True, null=True)
    creation_dt = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=25, blank=True, null=True)
    last_update_dt = models.DateField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=25, blank=True, null=True)
    tag = models.BooleanField(blank=True, null=True)
    remarks = models.CharField(max_length=5000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'xxnf_tasks'

def __int__(self):
	return self.task_id

def get_absolute_url(self):
	return reverse('tasks:tasks_edit', kwargs={'pk': self.pk})



