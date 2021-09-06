# Generated by Django 2.2 on 2021-08-27 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('first_name', models.CharField(max_length=255)),
                ('middle_initial', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('cell_phone', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=255)),
                ('social_security', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=2)),
                ('zip_code', models.CharField(max_length=5)),
                ('ubic_number', models.CharField(max_length=255)),
                ('union', models.CharField(max_length=255)),
                ('local', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('company_anti_discrimination_policy', models.CharField(max_length=255)),
                ('consent_for_anti_discrimination', models.CharField(max_length=255)),
                ('direct_deposit_option', models.CharField(max_length=255)),
                ('bank_name', models.CharField(max_length=255)),
                ('routing_number', models.CharField(max_length=255)),
                ('account_number', models.CharField(max_length=255)),
                ('w4filing_status', models.CharField(max_length=255)),
                ('total_number_allowances', models.CharField(max_length=255)),
                ('step2', models.CharField(max_length=255)),
                ('step3_a', models.CharField(max_length=255)),
                ('step3_b', models.CharField(max_length=255)),
                ('step3c_total', models.CharField(max_length=255)),
                ('step4_a', models.CharField(max_length=255)),
                ('step4_b', models.CharField(max_length=255)),
                ('step4_c', models.CharField(max_length=255)),
                ('step2b1', models.CharField(max_length=255)),
                ('step2b2a', models.CharField(max_length=255)),
                ('step2b2b', models.CharField(max_length=255)),
                ('step2b2c', models.CharField(max_length=255)),
                ('step2b3', models.CharField(max_length=255)),
                ('step2b4', models.CharField(max_length=255)),
                ('step4b1', models.CharField(max_length=255)),
                ('step4b2', models.CharField(max_length=255)),
                ('step4b3', models.CharField(max_length=255)),
                ('step4b4', models.CharField(max_length=255)),
                ('step4b5', models.CharField(max_length=255)),
                ('immigration_status', models.CharField(max_length=255)),
                ('alien_restriation_number', models.CharField(max_length=255, null=True)),
                ('expiry_date', models.DateField(null=True)),
                ('alien_restriation_number2', models.CharField(max_length=255, null=True)),
                ('form_admission_number', models.CharField(max_length=255, null=True)),
                ('foreign_passport_number', models.CharField(max_length=255, null=True)),
                ('select_documents', models.CharField(max_length=255)),
                ('uploaded_documents', models.ImageField(upload_to='')),
                ('signature', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
