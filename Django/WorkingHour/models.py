# _*_ encoding:utf-8 _*_

from django.db import models

# Create your models here.


class User(models.Model):
    userid = models.AutoField(primary_key=True, verbose_name=u"用户id")
    account = models.CharField(max_length=100, verbose_name=u"用户账户")
    level = models.IntegerField(verbose_name=u"用户等级")
    department = models.CharField(max_length=100, verbose_name=u"用户所属部门")
    username = models.CharField(max_length=100, verbose_name=u"用户名字")

    class Meta:
        db_table = "user"
        verbose_name = u"用户"
        verbose_name_plural = verbose_name


class Project(models.Model):
    project_id = models.CharField(primary_key=True, max_length=20, verbose_name=u"项目ID")
    project_kind = models.CharField(max_length=20, verbose_name=u"项目类别")
    project_name = models.CharField(max_length=100, verbose_name=u"项目名称")
    leader_id = models.CharField(max_length=20, verbose_name=u"项目领导ID")
    team_leader_id = models.CharField(max_length=20, verbose_name=u"小队领导ID")
    description = models.TextField(max_length=500, verbose_name=u"描述")
    start_date = models.DateField(verbose_name=u"项目开始时间")
    over_date = models.DateField(verbose_name=u"项目到期时间")

    class Meta:
        db_table = "project"
        verbose_name = u"项目"
        verbose_name_plural = verbose_name

class WorkForm(models.Model):
    workForm_id = models.CharField(primary_key=True, max_length=20, verbose_name=u"工作表ID")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name=u"用户ID（外键）")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name=u"项目ID（外键）")
    handle_id = models.IntegerField(verbose_name=u"处理ID")
    score = models.IntegerField(verbose_name=u"分数")
    fast_handle_time = models.DateTimeField(verbose_name=u"第一次处理时间")
    is_accept = models.IntegerField(default=1, verbose_name=u"是否接受")
    create_time = models.DateTimeField(verbose_name=u"工作表创建时间")
    modify_time = models.DateTimeField(verbose_name=u"修改时间")
    
    class Meta:
        db_table = "workform"
        verbose_name = u"工作表"
        verbose_name_plural = verbose_name


class WorkCount(models.Model):
    update_id = models.CharField(primary_key=True, max_length=20, verbose_name=u"更新时间")
    workForm = models.ForeignKey(WorkForm, on_delete=models.CASCADE, verbose_name=u"工作表ID（外键）")
    user_id = models.CharField(max_length=20, default="", verbose_name=u"用户ID")
    workkinds = models.CharField(max_length=50, verbose_name=u"工作类型")
    count = models.IntegerField(verbose_name=u"工作数量")
    order = models.IntegerField(verbose_name=u"订单")
    description = models.CharField(max_length=300, verbose_name=u"描述")

    class Meta:
        db_table = "workcount"
        verbose_name = u"工作量"
        verbose_name_plural = verbose_name
    

class WorkKinds(models.Model):
    work_kind = models.IntegerField()
    description = models.CharField(max_length=50)

    class Meta:
        db_table = "workkinds"
        verbose_name = u"工作种类"
        verbose_name_plural = verbose_name


class FormStream(models.Model):
    stream_id = models.CharField(primary_key=True, max_length=20)
    handler = models.ForeignKey(User, on_delete=models.CASCADE)
    opinion = models.CharField(max_length=500)
    datetime = models.DateTimeField()

    class Meta:
        db_table = "formstream"
        verbose_name = u"工作流"
        verbose_name_plural = verbose_name
