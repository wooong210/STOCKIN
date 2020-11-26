# Generated by Django 3.1.2 on 2020-11-26 14:03

from django.conf import settings
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
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('nickname', models.CharField(max_length=20, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=200)),
                ('sector', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('highestPrice', models.IntegerField(blank=True, null=True)),
                ('lowestPrice', models.IntegerField(blank=True, null=True)),
                ('tradeVolume', models.IntegerField(blank=True, null=True)),
                ('tradeValue', models.BigIntegerField(blank=True, null=True)),
                ('startPrice', models.IntegerField(blank=True, null=True)),
                ('yesterdayPrice', models.IntegerField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('isKOSPI', models.BooleanField(blank=True, null=True)),
                ('saleGrowthRate', models.CharField(max_length=15, null=True)),
                ('saleGrowthRateAvg', models.CharField(max_length=15, null=True)),
                ('operatingMarginRate', models.CharField(max_length=15, null=True)),
                ('operatingMarginRateAvg', models.CharField(max_length=15, null=True)),
                ('crawledPER', models.CharField(max_length=15, null=True)),
                ('crawledPERAvg', models.CharField(max_length=15, null=True)),
                ('debtRatio', models.CharField(max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StockHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('endPrice', models.IntegerField(null=True)),
                ('startPrice', models.IntegerField(null=True)),
                ('highestPrice', models.IntegerField(null=True)),
                ('lowestPrice', models.IntegerField(null=True)),
                ('tradeVolume', models.IntegerField(null=True)),
                ('upDown', models.IntegerField(null=True)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.stock')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('press', models.CharField(max_length=200, null=True)),
                ('link', models.CharField(max_length=300, null=True)),
                ('date', models.DateField(null=True)),
                ('stock', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.stock')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default', max_length=64)),
                ('stocks', models.ManyToManyField(to='core.Stock')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_of_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FinancialStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quarter', models.CharField(max_length=15, null=True)),
                ('sales', models.CharField(max_length=15, null=True)),
                ('operatingProfit', models.CharField(max_length=15, null=True)),
                ('netIncome', models.CharField(max_length=15, null=True)),
                ('operatingMargin', models.CharField(max_length=15, null=True)),
                ('netProfitMargin', models.CharField(max_length=15, null=True)),
                ('PER', models.CharField(max_length=15, null=True)),
                ('PBR', models.CharField(max_length=15, null=True)),
                ('ROE', models.CharField(max_length=15, null=True)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.stock')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_set', to=settings.AUTH_USER_MODEL)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_set', to='core.stock')),
            ],
        ),
    ]
