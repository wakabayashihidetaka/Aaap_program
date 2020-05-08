# Generated by Django 2.2.12 on 2020-05-08 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssessmentAnswer',
            fields=[
                ('answer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('question1_answer', models.IntegerField()),
                ('question2_answer', models.IntegerField()),
                ('question3_answer', models.IntegerField()),
                ('question4_answer', models.IntegerField()),
                ('question5_answer', models.IntegerField()),
                ('question6_answer', models.IntegerField()),
                ('question7_answer', models.IntegerField()),
                ('question8_answer', models.IntegerField()),
                ('question9_answer', models.IntegerField()),
                ('question10_answer', models.IntegerField()),
                ('question11_answer', models.IntegerField()),
                ('question12_answer', models.IntegerField()),
                ('question13_answer', models.IntegerField()),
                ('question14_answer', models.IntegerField()),
                ('question15_answer', models.IntegerField()),
                ('question16_answer', models.IntegerField()),
                ('question17_answer', models.IntegerField()),
                ('question18_answer', models.IntegerField()),
                ('question19_answer', models.IntegerField()),
                ('question20_answer', models.IntegerField()),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=25)),
                ('company_id', models.IntegerField()),
                ('department_id', models.IntegerField()),
                ('age', models.IntegerField()),
                ('gender', models.IntegerField()),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='AssessmentOutput',
            fields=[
                ('output_id', models.IntegerField(primary_key=True, serialize=False)),
                ('type1_id', models.IntegerField()),
                ('type2_id', models.IntegerField()),
                ('type3_id', models.IntegerField()),
                ('type4_id', models.IntegerField()),
                ('type5_id', models.IntegerField()),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True)),
                ('answer_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aaap.AssessmentAnswer')),
            ],
        ),
        migrations.AddField(
            model_name='assessmentanswer',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aaap.User'),
        ),
    ]
