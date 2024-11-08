from django.db import migrations, models
import django.db.models.deletion
import pgvector.django.vector


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('diss_id', models.AutoField(primary_key=True, serialize=False)),
                ('summary', models.TextField(blank=True, null=True)),
                ('summ_emb', pgvector.django.vector.VectorField(blank=True, dimensions=512, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.TextField()),
                ('summary', models.TextField(blank=True, null=True)),
                ('summ_emb', pgvector.django.vector.VectorField(blank=True, dimensions=512, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sources',
            fields=[
                ('source_id', models.AutoField(primary_key=True, serialize=False)),
                ('embedding', pgvector.django.vector.VectorField(dimensions=512)),
                ('text', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sources.users')),
                ('diss_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sources', to='sources.discussion')),
            ],
        ),
        migrations.AddField(
            model_name='discussion',
            name='base_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sources.sources'),
        ),
        migrations.AddField(
            model_name="discussion",
            name="collaborators",
            field=models.ManyToManyField(to="sources.users"),
        ),
    ]
