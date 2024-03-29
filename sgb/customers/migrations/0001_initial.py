# Generated by Django 4.1 on 2023-11-26 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('CreatedBy', models.PositiveIntegerField(blank=True, null=True, verbose_name='Create by')),
                ('CreationTime', models.DateTimeField(auto_now_add=True, verbose_name='Time of Creation')),
                ('UpdatedOn', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('AccountId', models.IntegerField(default=1, verbose_name='Account Id')),
                ('IAMUserId', models.BigIntegerField(unique=True, verbose_name='IAM User Id')),
                ('CustomerId', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('Name', models.CharField(blank=True, default='', max_length=225, null=True, verbose_name='Name')),
                ('Telephone', models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='Phone number')),
                ('Email', models.EmailField(max_length=250, verbose_name='Email address')),
                ('SocialMediaLink', models.CharField(blank=True, default='', max_length=155, null=True, verbose_name='Social media link')),
                ('HighestEducation', models.CharField(blank=True, default='', max_length=150, null=True, verbose_name='Highest education')),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
                'db_table': 'Customer',
            },
        ),
        migrations.CreateModel(
            name='CustomerCreditRiskParameter',
            fields=[
                ('CreatedBy', models.PositiveIntegerField(blank=True, null=True, verbose_name='Create by')),
                ('CreationTime', models.DateTimeField(auto_now_add=True, verbose_name='Time of Creation')),
                ('UpdatedOn', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('AccountId', models.IntegerField(default=1, verbose_name='Account Id')),
                ('CustomerCreditRiskParameterId', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('IsGoodCreditRisk', models.BooleanField(blank=True, null=True, verbose_name='Is Good Credit Risk')),
                ('Status', models.PositiveIntegerField(blank=True, null=True, verbose_name="Status of the debtor's checking account with the bank (categorical)")),
                ('Duration', models.PositiveIntegerField(blank=True, null=True, verbose_name='Credit duration in months (quantitative)')),
                ('CreditHistory', models.PositiveIntegerField(blank=True, null=True, verbose_name='History of compliance with previous or concurrent credit contracts (categorical)')),
                ('Purpose', models.PositiveIntegerField(blank=True, null=True, verbose_name='Purpose for which the credit is needed (categorical)')),
                ('Amount', models.PositiveIntegerField(blank=True, null=True, verbose_name='Credit amount in DM (quantitative)')),
                ('Savings', models.PositiveIntegerField(blank=True, null=True, verbose_name="Debtor's savings (categorical)")),
                ('EmploymentDuration', models.PositiveIntegerField(blank=True, null=True, verbose_name="Duration of debtor's employment with current employer (ordinal; discrete quantitative)")),
                ('InstallmentRate', models.PositiveIntegerField(blank=True, null=True, verbose_name="Credit installments as a percentage of debtor's disposable income (ordinal; discrete quantitative)")),
                ('PersonalStatusSex', models.PositiveIntegerField(blank=True, null=True, verbose_name='Combined information on sex and marital status; categorical')),
                ('OtherDebtors', models.PositiveIntegerField(blank=True, null=True, verbose_name='Is there another debtor or a guarantor for the credit? (categorical)')),
                ('PresentResidence', models.PositiveIntegerField(blank=True, null=True, verbose_name='Length of time (in years) the debtor lives in the present residence (ordinal)')),
                ('MostValuableProperty', models.PositiveIntegerField(blank=True, null=True, verbose_name="The debtor's most valuable property (choices)")),
                ('Age', models.PositiveIntegerField(blank=True, null=True, verbose_name='Age in years (quantitative)')),
                ('OtherInstallmentPlans', models.PositiveIntegerField(blank=True, null=True, verbose_name='Installment plans from providers other than the credit-giving bank (categorical)')),
                ('Housing', models.PositiveIntegerField(blank=True, null=True, verbose_name='Type of housing the debtor lives in (categorical)')),
                ('NumberCredits', models.PositiveIntegerField(blank=True, null=True, verbose_name='Number of credits including the current one the debtor has (or had) at this bank (ordinal, discretequantitative)')),
                ('Job', models.PositiveIntegerField(blank=True, null=True, verbose_name="Quality of debtor's job (ordinal)")),
                ('PeopleLiable', models.PositiveIntegerField(blank=True, null=True, verbose_name='Number of persons who financially depend on the debtor (i.e., are entitled to maintenance) (binary,discrete quantitative)')),
                ('HasTelephone', models.BooleanField(blank=True, null=True, verbose_name="Is there a telephone landline registered on the debtor's name?")),
                ('IsForeignWorker', models.PositiveIntegerField(blank=True, null=True, verbose_name='Is the debtor a foreign worker?')),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CustomerCreditRiskParameters', to='customers.customer')),
            ],
            options={
                'verbose_name': 'Customer Parameter',
                'verbose_name_plural': 'Customer Parameters',
                'db_table': 'CustomerParameters',
            },
        ),
    ]
