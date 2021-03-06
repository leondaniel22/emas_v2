# Generated by Django 3.2.6 on 2022-02-24 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_site', '0008_alter_solution_options'),
        ('nlp_component', '0005_auto_20220221_2358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Gruppe',
                'verbose_name_plural': 'Gruppen',
            },
        ),
        migrations.CreateModel(
            name='UserComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='', max_length=5000, verbose_name='Inhalt')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Erstelldatum')),
                ('error_appearance', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='user_site.errorappearance', verbose_name='Erscheinungsbild')),
            ],
            options={
                'verbose_name': 'Neuer Lösungsvorschlag',
                'verbose_name_plural': 'Neue Lösungsvorschläge',
            },
        ),
        migrations.RemoveField(
            model_name='cluster',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='cluster',
            name='error_appearance',
        ),
        migrations.RemoveField(
            model_name='mainobject',
            name='cluster',
        ),
        migrations.RemoveField(
            model_name='operation',
            name='cluster',
        ),
        migrations.RemoveField(
            model_name='relatedobject',
            name='main_object',
        ),
        migrations.RemoveField(
            model_name='requestcomment',
            name='comment_ptr',
        ),
        migrations.RemoveField(
            model_name='requestcomment',
            name='error_appearance',
        ),
        migrations.AddField(
            model_name='keyword',
            name='sentence',
            field=models.ManyToManyField(to='nlp_component.Sentence', verbose_name='Satz'),
        ),
        migrations.DeleteModel(
            name='Addition',
        ),
        migrations.DeleteModel(
            name='Cluster',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='MainObject',
        ),
        migrations.DeleteModel(
            name='Operation',
        ),
        migrations.DeleteModel(
            name='RelatedObject',
        ),
        migrations.DeleteModel(
            name='RequestComment',
        ),
        migrations.AddField(
            model_name='sentence',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='nlp_component.group', verbose_name='Gruppe'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sentence',
            name='user_comment',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='nlp_component.usercomment', verbose_name='Lösungsvorschlag'),
            preserve_default=False,
        ),
    ]
