# Generated by Django 4.0.6 on 2023-03-19 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_remove_user_is_superuser_custompermission'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('CreatedBy', models.PositiveIntegerField(blank=True, null=True, verbose_name='Create by')),
                ('CreationTime', models.DateTimeField(auto_now_add=True, verbose_name='Time of Creation')),
                ('UpdatedOn', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('AccountId', models.IntegerField(default=1, verbose_name='Account Id')),
                ('ModuleId', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('Title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Module',
                'verbose_name_plural': 'Modules',
                'db_table': 'Module',
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('CreatedBy', models.PositiveIntegerField(blank=True, null=True, verbose_name='Create by')),
                ('CreationTime', models.DateTimeField(auto_now_add=True, verbose_name='Time of Creation')),
                ('UpdatedOn', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('AccountId', models.IntegerField(default=1, verbose_name='Account Id')),
                ('PermissionId', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('Title', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Permission',
                'verbose_name_plural': 'Permissions',
                'db_table': 'Permission',
            },
        ),
        migrations.CreateModel(
            name='UserModulePermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreatedBy', models.PositiveIntegerField(blank=True, null=True, verbose_name='Create by')),
                ('CreationTime', models.DateTimeField(auto_now_add=True, verbose_name='Time of Creation')),
                ('UpdatedOn', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('AccountId', models.IntegerField(default=1, verbose_name='Account Id')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='module_permissions', to='users.user')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='user_module_permissions', to='auth.group', verbose_name='user module groups')),
            ],
            options={
                'verbose_name': 'User module permissions',
                'verbose_name_plural': 'User module permissions',
                'db_table': 'UserModulePermission',
            },
        ),
    ]
