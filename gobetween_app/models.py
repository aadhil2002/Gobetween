from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=50)

class user_reg(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile =models.CharField(max_length=100,null=True)
    DateOfBirth =models.DateField(max_length=100,null=True)
    gender =models.CharField(max_length=100,null=True)
    district =models.CharField(max_length=100,null=True)
    state =models.CharField(max_length=100,null=True)
    address =models.CharField(max_length=100,null=True)
    pincode =models.CharField(max_length=100,null=True)
    reject_reason=models.CharField(max_length=100,null=True)


class comp_reg(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=100,null=True)
    district=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)
    pincode=models.CharField(max_length=100,null=True)
    upi_qrcode=models.CharField(max_length=100,null=True)
    reject_reason=models.CharField(max_length=100,null=True)

class driver_reg(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    company = models.ForeignKey(comp_reg,on_delete=models.CASCADE,null=True)
    mobile = models.CharField(max_length=100,null=True)
    license_no = models.CharField(max_length=100,null=True)
    DateOB = models.DateField(max_length=100,null=True)
    gender = models.CharField(max_length=100,null=True)
    district = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    pincode = models.CharField(max_length=100,null=True)
    reject_reason=models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)
    status1=models.CharField(max_length=100,null=True)
    photo = models.ImageField(upload_to='driver_images/', null=True)
    driving_experience=models.IntegerField(max_length=100,null=True)
    qrcode=models.CharField(max_length=100,null=True)


class add_vehicle_type(models.Model):
    veh_type= models.CharField(max_length=50, null=True)


class add_vehicle(models.Model):
    company = models.ForeignKey(comp_reg, on_delete=models.CASCADE,null=True)
    driver = models.ForeignKey(driver_reg, on_delete=models.CASCADE,null=True)
    vehtype = models.CharField(max_length=100,null=True)
    car_number=models.CharField(max_length=100,null=True)
    car_name=models.CharField(max_length=100,null=True)
    brand=models.CharField(max_length=100,null=True)
    year=models.CharField(max_length=100,null=True)
    rc_no=models.CharField(max_length=100,null=True)
    rc_exp=models.DateField(max_length=100,null=True)
    insurance_no=models.CharField(max_length=100,null=True)
    insurance_exp=models.DateField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)
    
class trip_request(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=100,null=True)
    pickup_place=models.CharField(max_length=100,null=True)
    to_place=models.CharField(max_length=100,null=True)
    mobile=models.CharField(max_length=100,null=True)
    time=models.CharField(max_length=100,null=True)
    date=models.DateField(max_length=100,null=True)
    no_of_person=models.CharField(max_length=100,null=True)
    status=models.CharField(max_length=100,null=True)
    payment=models.CharField(max_length=100,null=True)
    purpose=models.CharField(max_length=100,null=True)
    company=models.ForeignKey(comp_reg,on_delete=models.CASCADE,null=True)
    driver=models.ForeignKey(driver_reg,on_delete=models.CASCADE,null=True)
    
class driver_request(models.Model):
    driver=models.ForeignKey(driver_reg,on_delete=models.CASCADE,null=True)
    company=models.ForeignKey(comp_reg,on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=100,null=True)
    
class assign_trip(models.Model):
    driver=models.ForeignKey(driver_reg,on_delete=models.CASCADE)
    comp = models.ForeignKey(comp_reg,on_delete=models.CASCADE,null=True)
    veh = models.ForeignKey(add_vehicle,on_delete=models.CASCADE)
    trip=models.ForeignKey(trip_request,on_delete=models.CASCADE)
    km_per_amt=models.IntegerField(max_length=100,null=True)
    kms=models.IntegerField(max_length=100,null=True)
    total_amt=models.CharField(max_length=100,null=True)
    status=models.CharField(max_length=100,null=True)


class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)
    subject=models.CharField(max_length=100,null=True)
    complaint=models.CharField(max_length=500,null=True)
    status = models.CharField(max_length=100, null=True)
    action = models.CharField(max_length=50, null=True)


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    name=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)
    subject=models.CharField(max_length=100,null=True)
    feedback=models.CharField(max_length=500,null=True)
    status = models.CharField(max_length=100, null=True)
    action = models.CharField(max_length=50, null=True)
    


class location_add(models.Model):
    location= models.CharField(max_length=50, null=True)

class driver_leave(models.Model):
    driver=models.ForeignKey(driver_reg,on_delete=models.CASCADE,null=True)
    company=models.ForeignKey(comp_reg,on_delete=models.CASCADE,null=True)
    startdate=models.DateField(max_length=100,null=True)
    enddate=models.DateField(max_length=100,null=True)
    no_of_days=models.IntegerField(max_length=100,null=True)
    reason=models.CharField(max_length=100,null=True)
    status=models.CharField(max_length=100,null=True)
