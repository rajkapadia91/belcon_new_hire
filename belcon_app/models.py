from django.db import models
import re
from django.db.models.signals import post_delete
from django.dispatch import receiver

class EmployerManager(models.Manager):
    def validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        NAME_REGEX = re.compile(r'^[a-zA-Z]+$')   
        if not EMAIL_REGEX.match(postData['email']): 
            errors['email'] = "Email must be in a valid format" 
        if len(postData['password']) < 8:
            errors['password'] = "Password must be atleast 8 characters"   
        if postData['confirm_password'] != postData['password']:
            errors['confirm_password'] = "Passwords do not match"
        return errors    

class Employer(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    # secretkey = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = EmployerManager()


class UserDetails(models.Model):
    start_date = models.DateField()
    first_name = models.CharField(max_length=255)
    middle_initial = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    cell_phone = models.CharField(max_length=20)
    email = models.CharField(max_length=255)
    social_security = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    ubic_number = models.CharField(max_length=255, blank=True, null=True, default="")
    union = models.CharField(max_length=255 ,blank=True, null=True, default="")
    local = models.CharField(max_length=255 ,blank=True, null=True, default="")
    position = models.CharField(max_length=255 ,blank=True, null=True, default="")
    gender = models.CharField(max_length=255)
    company_anti_discrimination_policy = models.CharField(max_length=255)
    consent_for_anti_discrimination = models.CharField(max_length=255)
    direct_deposit_option = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=255 ,blank=True, null=True , default="")
    routing_number = models.CharField(max_length=255 ,blank=True, null=True , default="")
    account_number = models.CharField(max_length=255 ,blank=True, null=True , default="")
    w4filing_status = models.CharField(max_length=255 ,blank=True, null=True , default="")
    total_number_allowances = models.CharField(max_length=255  ,blank=True, null=True , default="")
    step2 = models.CharField(max_length=255, blank=True, null=True, default="None")
    step3_a = models.CharField(max_length=255 ,blank=True, null=True , default="")
    step3_b = models.CharField(max_length=255 ,blank=True, null=True , default="")
    step3c_total = models.CharField(max_length=255 ,blank=True, null=True , default="")
    step4_a = models.CharField(max_length=255,blank=True, null=True , default="")
    step4_b = models.CharField(max_length=255,blank=True, null=True , default="")
    step4_c = models.CharField(max_length=255,blank=True, null=True , default="")
    step2b1 = models.CharField(max_length=255,blank=True, null=True , default="")
    step2b2a = models.CharField(max_length=255,blank=True, null=True , default="")
    step2b2b = models.CharField(max_length=255,blank=True, null=True , default="")
    step2b2c = models.CharField(max_length=255,blank=True, null=True , default="")
    step2b3 = models.CharField(max_length=255,blank=True, null=True , default="")
    step2b4 = models.CharField(max_length=255,blank=True, null=True , default="")
    step4b1 = models.CharField(max_length=255,blank=True, null=True , default="")
    step4b2 = models.CharField(max_length=255,blank=True, null=True , default="")
    step4b3 = models.CharField(max_length=255,blank=True, null=True , default="")
    step4b4 = models.CharField(max_length=255,blank=True, null=True , default="")
    step4b5 = models.CharField(max_length=255,blank=True, null=True , default="")
    immigration_status = models.CharField(max_length=255)
    alien_restriation_number = models.CharField(max_length=255,blank=True, null=True , default="")
    expiry_date = models.DateField(null=True, blank=True)
    alien_restriation_number2 = models.CharField(max_length=255,blank=True, null=True , default="")
    form_admission_number = models.CharField(max_length=255,blank=True, null=True , default="")
    foreign_passport_number = models.CharField(max_length=255,blank=True, null=True , default="")
    direct_deposit_check = models.FileField(blank=True, null=True)
    id_1 = models.FileField(blank=True, null=True)
    id_2 = models.FileField(blank=True,null=True)
    signature = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


@receiver(models.signals.pre_delete, sender=UserDetails)
def remove_file_from_s3(sender, instance, using, **kwargs):
    instance.direct_deposit_check.delete(save=False)
    instance.id_1.delete(save=False)
    instance.id_2.delete(save=False)











