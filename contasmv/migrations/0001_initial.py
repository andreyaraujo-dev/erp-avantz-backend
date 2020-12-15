# Generated by Django 3.1.2 on 2020-12-13 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContasMv',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('instit_id', models.PositiveIntegerField()),
                ('idctfin', models.PositiveIntegerField()),
                ('idsecao', models.PositiveIntegerField()),
                ('tipo', models.PositiveIntegerField()),
                ('descr', models.CharField(blank=True, max_length=60, null=True)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dat', models.DateTimeField(blank=True, null=True)),
                ('idorigem', models.PositiveIntegerField()),
                ('usuario', models.PositiveIntegerField()),
                ('mcx', models.PositiveIntegerField()),
                ('sit', models.PositiveIntegerField()),
                ('saldocons', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'contasmv',
                'managed': False,
            },
        ),
    ]