# Generated by Django 4.0.6 on 2023-04-02 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('CreatedBy', models.PositiveIntegerField(blank=True, null=True, verbose_name='Create by')),
                ('CreationTime', models.DateTimeField(auto_now_add=True, verbose_name='Time of Creation')),
                ('UpdatedOn', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('AccountId', models.IntegerField(default=1, verbose_name='Account Id')),
                ('is_staff', models.BooleanField(verbose_name='Is staff')),
                ('VisitorId', models.BigAutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('Name', models.CharField(blank=True, default='', max_length=225, null=True, verbose_name='Name')),
                ('Telephone', models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='Phone Number')),
                ('Email', models.EmailField(blank=True, default='', max_length=250, null=True, verbose_name='Email Address')),
                ('SocialMediaLink', models.CharField(blank=True, default='', max_length=155, null=True, verbose_name='Social Media Link')),
                ('HighestEducation', models.CharField(blank=True, default='', max_length=150, null=True, verbose_name='Highest Education')),
                ('Query', models.TextField(blank=True, null=True, verbose_name='Write Your Query')),
            ],
            options={
                'verbose_name': 'Visitor',
                'verbose_name_plural': 'Visitors',
                'db_table': 'Visitor',
            },
        ),
    ]
