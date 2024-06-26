from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import TemplateView
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.hashers import check_password
from gobetween_app.models import UserType, assign_trip, user_reg, driver_reg, comp_reg

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'


class user_registration(TemplateView):
    template_name="user_reg.html"
    def post(self,request,*arg,**kwargs):
        first_name=request.POST['first_name']
        print(first_name)
        last_name=request.POST['last_name']
        print(last_name)
        name=first_name+" "+last_name
        mobile=request.POST['mobile']
        print(mobile)
        email=request.POST['email']
        print(email)
        state=request.POST['state']
        print(state)
        district=request.POST['district']
        print(district)
        gender=request.POST['gender']
        print(gender)
        DateOfBirth=request.POST['DateOfBirth']
        print(DateOfBirth)
        pincode=request.POST['pincode']
        print(pincode)
        address=request.POST['address']
        print(address)
        username=request.POST['username']
        print(username)
        password=request.POST['password']
        print(password)
        try:
            user = User.objects.create_user(first_name=name,email=email,password=password,username=username,last_name='1',is_active='1')
            table_user=user_reg()
            table_user.user =user
            table_user.mobile =mobile
            table_user.state =state
            table_user.DateOfBirth =DateOfBirth
            table_user.gender =gender
            table_user.address = address
            table_user.district =district 
            table_user.pincode=pincode
            table_user.save()
            usertype = UserType()
            usertype.user = user
            usertype.type ='user'
            usertype.save()
            return render(request,'index.html',{'messages':'successfully registered'})
        except:
            messages = "Enter Another Username, user already exist"
            return render(request,'index.html',{'message':messages})

    
class driver_registartion(TemplateView):
     template_name="driver_reg.html"
     def post(self,request,*arg,**kwargs):
         first_name=request.POST['first_name']
         print(first_name)
         last_name=request.POST['last_name']
         print(last_name)
         name=first_name+" "+last_name
         mobile=request.POST['mobile']
         print(mobile)
         license_no=request.POST['license_no']
         print(license_no)
         email=request.POST['email']
         print(email)
         state=request.POST['state']
         print(state)
         district=request.POST['district']
         print(district)
         gender=request.POST['gender']
         print(gender)
         DateOB=request.POST['DateOB']
         print(DateOB)
         pincode=request.POST['pincode']
         print(pincode)
         address=request.POST['address']
         print(address)
         username=request.POST['username']
         print(username)
         password=request.POST['password']
         photo=request.FILES['driver_photo']
         driving_experience=request.POST['driving_exp']
         
         
         print(password)
         try:
             user = User.objects.create_user(first_name=name,email=email,password=password,username=username,last_name='0',is_active='1')
             table_driver= driver_reg()
             table_driver.user_id=user.id
             table_driver.mobile=mobile
             table_driver.license_no=license_no
             table_driver.state=state
             table_driver.driving_experience=driving_experience
             table_driver.photo=photo
             table_driver.DateOB=DateOB
             table_driver.gender=gender
             table_driver.address= address
             table_driver.district=district
             table_driver.pincode=pincode
             table_driver.status="freelance"
             table_driver.status1="available"
             table_driver.save()
             usertype = UserType()
             usertype.user = user
             usertype.type ='freelance_driver'
             usertype.save()
             return render(request,'index.html',{'messages':'successfully registered'})
         except:
             messages = "Enter Another Username, user already exist"
             return render(request,'index.html',{'message':messages})

class comp_registration(TemplateView):
    template_name="comp_reg.html"
    def post(self,request,*arg,**kwargs):
        company_name=request.POST['company_name']
        print(company_name)
        company_name=request.POST['company_name']
        print(company_name)    
        mobile=request.POST['mobile']
        print(mobile)
        email=request.POST['email']
        print(email)
        state=request.POST['state']
        print(state)
        district=request.POST['district']
        print(district)
        pincode=request.POST['pincode']
        print(pincode)
        address=request.POST['address']
        print(address)
        username=request.POST['username']
        print(username)
        password=request.POST['password']
        print(password)
        try:
            user = User.objects.create_user(first_name=company_name,email=email,password=password,username=username,last_name='0',is_active='1')
            table_company= comp_reg()
            table_company.user=user
            table_company.mobile=mobile
            table_company.state=state
            table_company.address= address
            table_company.district=district
            table_company.pincode=pincode
            table_company.save()
            usertype = UserType()
            usertype.user = user
            usertype.type ='company'
            usertype.save()
            return render(request,'index.html',{'messages':'successfully registered'})
        except:
            messages = "Enter Another Username, user already exist"
            return render(request,'index.html',{'message':messages})



class login_view(TemplateView):
    template_name="login.html"
    def post(self,request,*args,**kwargs):
        username=request.POST['username']
        print(username)
        password =request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not  None:
            login(request,user)
            if user.last_name=='1':
                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type=="driver":
                    return redirect('/driver')
                elif UserType.objects.get(user_id=user.id).type=="freelance_driver":
                    return redirect('/freelance_driver')
                elif UserType.objects.get(user_id=user.id).type == "company":
                    return redirect('/company')
                elif UserType.objects.get(user_id=user.id).type == "user":
                    return redirect('/user')
                else:
                    return render(request,'login.html',{'message':" User Account Not Authenticated"})
            else:
                return render(request,'login.html',{'message':" User Account Not Authenticated"})
        else:
            if not (User.objects.filter(username=username).exists()):
                return render(request,'index.html',{'message':"Invalid Username"})
            else:
                    user1=User.objects.get(username=username)
                    if not check_password(password, user1.password):
                     return render(request,'index.html',{'message':"Invalid Password"})
                    else:
                        user2=User.objects.get(username=username).id
                        if UserType.objects.get(user_id=user2).type == "company":
                            if comp_reg.objects.get(user_id=user2).reject_reason is not None:
                                return render(request,'index.html',{'message':"Your account as suspended due to"+" "+comp_reg.objects.get(user_id=user2).reject_reason})
                        elif ((UserType.objects.get(user_id=user2).type == "driver")or(UserType.objects.get(user_id=user2).type == "freelance_driver")):
                            if driver_reg.objects.get(user_id=user2).reject_reason is not None:
                                return render(request,'index.html',{'message':"Your account as suspended due to"+" "+driver_reg.objects.get(user_id=user2).reject_reason})
                        elif UserType.objects.get(user_id=user2).type == "user":
                            if user_reg.objects.get(user_id=user2).reject_reason is not None:
                                return render(request,'index.html',{'message':"Your account as suspended due to"+" "+user_reg.objects.get(user_id=user2).reject_reason})
                        
                


            
            
            
class about(TemplateView):
    template_name = 'about.html'



class contact(TemplateView):
    template_name = 'contact.html'


           