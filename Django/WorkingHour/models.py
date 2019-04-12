from django.db import models

# Create your models here.

class User(models.Model):
    userid = models.AutoField(primary_key=True)
    account = models.CharField(max_length=100)
    level = models.IntegerField()
    department = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    class Meta:
        db_table = "user"

class Project(models.Model):
    project_id = models.CharField(primary_key=True, max_length=20)
    project_kind = models.CharField(max_length=20)
    project_name = models.CharField(max_length=100)
    leader_id = models.CharField(max_length=20)
    team_leader_id = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    start_date = models.DateField()
    over_date = models.DateField()
    class Meta:
        db_table = "project"

class WorkForm(models.Model):
    workForm_id = models.CharField(primary_key=True, max_length=20)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    handle_id = models.IntegerField()
    score = models.IntegerField()
    fast_handle_time = models.DateTimeField()
    is_accept = models.IntegerField(default=1)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    
    class Meta:
        db_table = "workform"

class WorkCount(models.Model):
    update_id = models.CharField(primary_key=True, max_length=20)
    workForm = models.ForeignKey(WorkForm, on_delete=models.CASCADE)
    workkinds = models.CharField(max_length=50)
    count = models.IntegerField()
    order = models.IntegerField()
    description = models.CharField(max_length=300)

    class Meta:
        db_table = "workcount"
    
class WorkKinds(models.Model):
    work_kind = models.IntegerField()
    description = models.CharField(max_length=50)
    class Meta:
        db_table = "workkinds"

class FormStream(models.Model):
    stream_id = models.CharField(primary_key=True, max_length=20)
    handler = models.ForeignKey(User, on_delete=models.CASCADE)
    opinion = models.CharField(max_length=500)
    datetime = models.DateTimeField()
    class Meta:
        db_table = "formstream"