# Generated by Django 3.2.18 on 2023-03-15 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=20)),
                ('isActive', models.BooleanField()),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('marksPerQuestion', models.PositiveIntegerField()),
                ('isActive', models.PositiveIntegerField()),
                ('totalNumOfQuestion', models.PositiveIntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.course')),
            ],
            options={
                'db_table': 'exam',
            },
        ),
        migrations.CreateModel(
            name='Exam_question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examid', models.PositiveIntegerField()),
                ('questionid', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'exam_question',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('option1', models.CharField(max_length=250)),
                ('option2', models.CharField(max_length=250)),
                ('option3', models.CharField(max_length=250)),
                ('option4', models.CharField(max_length=250)),
                ('correctAns', models.CharField(max_length=250)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.course')),
            ],
            options={
                'db_table': 'question',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User_exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
                ('obtainMarks', models.PositiveIntegerField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.exam')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.user')),
            ],
            options={
                'db_table': 'user_exam',
            },
        ),
        migrations.CreateModel(
            name='User_exam_answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.user_exam')),
                ('answersansStatus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.course')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.exam')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.user')),
            ],
            options={
                'db_table': 'user_exam_answers',
            },
        ),
    ]
