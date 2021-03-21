# Generated by Django 3.1.7 on 2021-03-21 17:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Legislation', '0008_auto_20210321_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subsection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_number', models.CharField(default=None, max_length=220, null=True)),
                ('section_title', models.CharField(default=None, max_length=220, null=True)),
                ('section_content', models.TextField(blank=True, null=True)),
                ('writing_score', models.IntegerField()),
                ('bipartisan_score', models.IntegerField()),
                ('popularity_score', models.IntegerField()),
                ('transparency_score', models.IntegerField()),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Legislation.bill')),
            ],
        ),
        migrations.CreateModel(
            name='SubsectionComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubsectionLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('subsection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Legislation.subsection')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubsectionDisike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('subsection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Legislation.subsection')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubsectionCommentLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Legislation.subsectioncomment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubsectionCommentDisike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Legislation.subsectioncomment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='subsectioncomment',
            name='comment_dislikes',
            field=models.ManyToManyField(blank=True, related_name='subsection_comment_dislike_user', through='Legislation.SubsectionCommentDisike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='subsectioncomment',
            name='comment_likes',
            field=models.ManyToManyField(blank=True, related_name='subsection_comment_like_user', through='Legislation.SubsectionCommentLike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='subsectioncomment',
            name='subsection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Legislation.subsection'),
        ),
        migrations.AddField(
            model_name='subsectioncomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='subsection',
            name='subsection_comments',
            field=models.ManyToManyField(blank=True, related_name='subsection_comment_user', through='Legislation.SubsectionComment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='subsection',
            name='subsection_dislikes',
            field=models.ManyToManyField(blank=True, related_name='subsection_dislike_user', through='Legislation.SubsectionDisike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='subsection',
            name='subsection_likes',
            field=models.ManyToManyField(blank=True, related_name='subsection_like_user', through='Legislation.SubsectionLike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bill',
            name='bill_subsections',
            field=models.ManyToManyField(blank=True, related_name='bill_subsections', to='Legislation.Subsection'),
        ),
    ]
