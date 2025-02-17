# Generated by Django 5.0.3 on 2024-03-15 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(default='', max_length=254)),
                ('number', models.PositiveBigIntegerField(default=8000000)),
                ('state', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=450)),
                ('course', models.CharField(choices=[('Course options', 'Course options'), ('Javascript', 'Javascript'), ('Python', 'Python'), ('Data Analysis', 'Data Analysis'), ('Graphics Design', 'Graphics Design'), ('Cyber-security', 'Cyber-security'), ('Graphics Design', 'Graphics Design')], default='Course options', max_length=70)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
