# Generated by Django 4.0.5 on 2022-06-18 15:42

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created_at', models.CharField(max_length=20, null=True)),
                ('deleted_at', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('username', models.CharField(help_text='用户名', max_length=100, unique=True)),
                ('nickname', models.CharField(help_text='用户昵称', max_length=100)),
                ('password', models.CharField(help_text='加密后的密码', max_length=100)),
                ('type', models.CharField(default='default', help_text='类型', max_length=20)),
                ('is_supper', models.BooleanField(default=False, help_text='是否管理员')),
                ('is_active', models.BooleanField(default=True, help_text='是否启用')),
                ('last_login', models.CharField(blank=True, help_text='最后登陆时间', max_length=20)),
                ('last_ip', models.CharField(blank=True, help_text='最后登陆IP地址', max_length=50)),
                ('wx_token', models.CharField(help_text='用于发送微信消息的token', max_length=50, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='created', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='deleted', to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]