from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='category',
            field=models.CharField(
                choices=[
                    ('Fundamentals', 'Fundamentals'),
                    ('Web Framework', 'Web Framework'),
                    ('Database', 'Database'),
                    ('API', 'API'),
                    ('Frontend', 'Frontend'),
                    ('DevOps', 'DevOps'),
                    ('Other', 'Other'),
                ],
                default='Other',
                max_length=100,
            ),
        ),
    ]
