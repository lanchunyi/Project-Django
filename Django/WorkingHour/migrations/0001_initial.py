# Generated by Django 2.1.2 on 2019-04-12 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormStream',
            fields=[
                ('stream_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('opinion', models.CharField(max_length=500)),
                ('datetime', models.DateTimeField()),
            ],
            options={
                'db_table': 'formstream',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('project_kind', models.CharField(max_length=20)),
                ('project_name', models.CharField(max_length=100)),
                ('leader_id', models.CharField(max_length=20)),
                ('team_leader_id', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=500)),
                ('start_date', models.DateField()),
                ('over_date', models.DateField()),
            ],
            options={
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('account', models.CharField(max_length=100)),
                ('level', models.IntegerField()),
                ('department', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='WorkCount',
            fields=[
                ('update_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('workkinds', models.CharField(max_length=50)),
                ('count', models.IntegerField()),
                ('order', models.IntegerField(max_length=100)),
                ('description', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'workcount',
            },
        ),
        migrations.CreateModel(
            name='WorkForm',
            fields=[
                ('workForm_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('handle_id', models.IntegerField()),
                ('score', models.IntegerField()),
                ('fast_handle_time', models.DateTimeField()),
                ('is_accept', models.IntegerField(default=1, max_length=2)),
                ('create_time', models.DateTimeField()),
                ('modify_time', models.DateTimeField()),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WorkingHour.Project')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='WorkingHour.User')),
            ],
            options={
                'db_table': 'workform',
            },
        ),
        migrations.CreateModel(
            name='WorkKinds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_kind', models.IntegerField(max_length=5)),
                ('description', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'workkinds',
            },
        ),
        migrations.AddField(
            model_name='workcount',
            name='workForm_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WorkingHour.WorkForm'),
        ),
        migrations.AddField(
            model_name='formstream',
            name='handler_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WorkingHour.User'),
        ),
    ]