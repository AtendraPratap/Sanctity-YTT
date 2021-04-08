# Generated by Django 3.1.3 on 2021-03-08 07:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('account_number', models.CharField(max_length=200, null=True)),
                ('IFSC_CODE', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Basic_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateField(default=django.utils.timezone.now)),
                ('created_time', models.TimeField(default=django.utils.timezone.now)),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10, null=True)),
                ('father_name', models.CharField(max_length=100, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('current_address', models.TextField(null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('district', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('pincode', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
                ('email_id', models.EmailField(blank=True, max_length=100, null=True)),
                ('permanent_address', models.TextField(null=True)),
                ('mobile_number_1', models.CharField(max_length=10, null=True)),
                ('mobile_number_2', models.CharField(blank=True, max_length=10, null=True)),
                ('pan', models.CharField(blank=True, max_length=200, null=True)),
                ('aadhar', models.CharField(blank=True, max_length=200, null=True)),
                ('pan_image', models.FileField(blank=True, null=True, upload_to='pan/')),
                ('aadhar_front', models.FileField(blank=True, null=True, upload_to='aadhar_f/')),
                ('aadhar_back', models.FileField(blank=True, null=True, upload_to='aadhar_b/')),
                ('user_image', models.ImageField(null=True, upload_to='user_image/')),
                ('dsa_experience', models.IntegerField(blank=True, null=True)),
                ('business_name', models.CharField(max_length=200, null=True)),
                ('pan_or_aadhar', models.FileField(null=True, upload_to='dsa_docs/')),
            ],
        ),
        migrations.CreateModel(
            name='Business_Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, max_length=30, null=True)),
                ('lastName', models.CharField(blank=True, max_length=30, null=True)),
                ('contactNum', models.CharField(blank=True, max_length=13, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateField(default=django.utils.timezone.now)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PL_Docs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary_slip', models.FileField(blank=True, null=True, upload_to='PL/salary_slip/')),
                ('bank_statement', models.FileField(blank=True, null=True, upload_to='PL/bank_statement/')),
                ('residential_proof', models.FileField(blank=True, null=True, upload_to='PL/res_proof/')),
            ],
        ),
        migrations.CreateModel(
            name='PL_reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_1_name', models.CharField(max_length=200, null=True)),
                ('ref_2_name', models.CharField(max_length=200, null=True)),
                ('ref_1_contact', models.CharField(max_length=200, null=True)),
                ('ref_2_contact', models.CharField(max_length=200, null=True)),
                ('ref_1_relationship', models.CharField(max_length=200, null=True)),
                ('ref_2_relationship', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PL',
            fields=[
                ('basic_details_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='website.basic_details')),
                ('newsletter', models.BooleanField(default=True)),
                ('education', models.CharField(choices=[('10th', '10th'), ('10+2', '10+2'), ('Graduate', 'Graduate'), ('Post-Graduate', 'Post-Graduate')], max_length=20, null=True)),
                ('married', models.BooleanField(default=False)),
                ('property_ownership_status', models.CharField(choices=[('Rented', 'Rented'), ('Leased', 'Leased'), ('Self', 'Self'), ('Other', 'Other')], max_length=20, null=True)),
                ('no_of_years_at_residence', models.IntegerField(blank=True, null=True)),
                ('employment_type', models.CharField(choices=[('Salaried', 'Salaried'), ('Self-Employed', 'Self-Employed'), ('Self', 'Self'), ('Other', 'Other')], max_length=15, null=True)),
                ('bank_details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.bank_details')),
                ('docs', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.pl_docs')),
                ('references', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.pl_reference')),
            ],
            bases=('website.basic_details',),
        ),
    ]
