from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.views.generic import TemplateView, View
from django.utils import timezone
import datetime

from gobetween_app.models import Feedback, UserType, assign_trip, driver_leave, driver_request, user_reg, comp_reg, driver_reg,add_vehicle,trip_request,add_vehicle_type

class company_index_view(TemplateView):
    template_name = 'company/company_index.html'

    def get_context_data(self, **kwargs):
        com=comp_reg.objects.get(user_id=self.request.user.id)
        context = super().get_context_data(**kwargs)
        today = datetime.date.today()
        context = {'today' : today }
        context['v_list'] = add_vehicle.objects.filter(company_id=com.id)
        return context

    
class Add_Vehicle(TemplateView):
    template_name = 'company/add_vehicle.html'

    def get_context_data(self, **kwargs):
        context = super(Add_Vehicle,self).get_context_data(**kwargs)
        
        veh=add_vehicle_type.objects.all()
        
        context['veh'] = veh
        return context
    
    def post(self , request,*args,**kwargs):
        
        com=comp_reg.objects.get(user_id=self.request.user.id)
        car_number= request.POST['car_number']
        car_name = request.POST['car_name']
        vehtype = request.POST['vehtype']
        brand= request.POST['brand']
        year = request.POST['year']
        rc_no = request.POST['rc_no']
        rc_exp = request.POST['rc_expiry_date']
        insurance_no = request.POST['insurance_no']
        insurance_exp = request.POST['insurance_expiry_date']
        if add_vehicle.objects.filter(car_number=car_number):
            print ('pass')
            return render(request,'company/add_vehicle.html',{'message':"already exist"})
        else:
            vehicle = add_vehicle()
            vehicle.company_id=com.id
            vehicle.car_number = car_number
            vehicle.car_name = car_name
            vehicle. vehtype= vehtype
            vehicle.brand= brand
            vehicle.year = year
            vehicle.rc_no = rc_no
            vehicle.rc_exp = rc_exp
            vehicle.insurance_no = insurance_no
            vehicle.insurance_exp = insurance_exp 
            vehicle.status = 'available'
            vehicle.save()


            return render(request, 'company/add_vehicle.html', {'message': "Successfully Added"})


class Update_Vehicle(TemplateView):

    template_name = 'company/update_vehicle.html'
    def get_context_data(self, *args, **kwargs):
        id = self.request.GET['id']
        context = super().get_context_data(*args, **kwargs)  
        
        vehtype=add_vehicle_type.objects.all()
        vehicle = add_vehicle.objects.filter(id=id)
        context['vehtype'] = vehtype
        context['vehicle'] = vehicle
        return context
    
    def post(self , request,*args,**kwargs):
        
        id = self.request.GET['id']
        car_number= request.POST['car_number']
        car_name = request.POST['car_name']
        vehtype = request.POST['vehtype']
        brand= request.POST['brand']
        year = request.POST['year']
        rc_no = request.POST['rc_no']
        rc_exp = request.POST['rc_expiry_date']
        insurance_no = request.POST['insurance_no']
        insurance_exp = request.POST['insurance_expiry_date']

        vehicle = add_vehicle.objects.get(pk=id)
        vehicle.car_number = car_number
        vehicle.car_name = car_name
        vehicle.vehtype= vehtype
        vehicle.brand= brand
        vehicle.year = year
        vehicle.rc_no = rc_no
        vehicle.rc_exp = rc_exp
        vehicle.insurance_no = insurance_no
        vehicle.insurance_exp = insurance_exp 
        vehicle.save()


        return render(request, 'company/company_index.html', {'message': "Successfully Updated"})     
    

class Available(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        vehicle = add_vehicle.objects.get(pk=id)
        vehicle.status='available'
        vehicle.save()
        return render(request,'company/company_index.html',{'message':"Vehicle is now Available"})

class UnAvailable(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        vehicle = add_vehicle.objects.get(pk=id)
        vehicle.status='unavailable'
        vehicle.save()
        return render(request,'company/company_index.html',{'message':"Vehicle is now Unavailable"})

class Add_UPI(TemplateView):
    template_name = 'company/add_payment_UPI.html'
    def get_context_data(self, **kwargs):
        context = super(Add_UPI,self).get_context_data(**kwargs)
        
        upi = comp_reg.objects.get(user_id=self.request.user.id)
        
        context['upi'] = upi
        return context
    
    def post(self,request,*arg,**kwargs):
        upi_id=request.POST['upi_id']
        comp = comp_reg.objects.get(user_id=self.request.user.id)
        

        table_loc= comp
        table_loc.upi_qrcode=upi_id
        table_loc.save()
            
        return render(request,'company/company_index.html',{'message':'Successfully Added'})        
        
class Add_Driver(TemplateView):
    template_name = 'company/add_driver.html'
    def post(self,request,*arg,**kwargs):
        com=comp_reg.objects.get(user_id=self.request.user.id)
        print(com)
        name=request.POST['name']
        print(name)
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
        print(password)
        photo=request.FILES['driver_photo']
        driving_experience=request.POST['driving_exp']
        if User.objects.filter(email=email,username=username):
            print ('pass')
            return render(request,'company/company_index.html',{'message':"already added the username or email"})

        else:
            user = User.objects.create_user(username=username,password=password,email=email,first_name=name,is_staff='0',last_name='1')
            user.save()
            table_dri= driver_reg()
            table_dri.user=user
            table_dri.company_id=com.id
            table_dri.mobile=mobile
            table_dri.license_no=license_no
            table_dri.state=state
            table_dri.DateOB=DateOB
            table_dri.driving_experience=driving_experience
            table_dri.photo=photo
            table_dri.gender=gender
            table_dri.address= address
            table_dri.district=district
            table_dri.pincode=pincode
            table_dri.status="hired"
            table_dri.status1="available"
            table_dri.save()
            usertype = UserType()
            usertype.user = user
            usertype.type ='driver'
            usertype.save()
            
            return render(request,'company/company_index.html',{'message':'Successfully Added'})

        
class User_Request(TemplateView):
    template_name = 'company/user_request.html'
    def get_context_data(self, **kwargs):
        context = super(User_Request,self).get_context_data(**kwargs)
        com=comp_reg.objects.get(user_id=self.request.user.id)
        
        user_r = trip_request.objects.filter(company_id=com.id,status='pending')
        context['user_r'] = user_r
        return context
    
    def post(self , request,*args,**kwargs):
        user = comp_reg.objects.get(id=self.request.user.id)
        t=trip_request()
        t.company_id=user.id
        t.user = user
        t.save()


        return render(request, 'company/user_request.html', {'message': "successfully added"})


class Trip_Accept(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        trip = trip_request.objects.get(pk=id)
        trip.status='approval'
        trip.save()
        return redirect(request.META['HTTP_REFERER'])


    
class Trip_Reject(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        trip = trip_request.objects.get(pk=id)
        trip.status='reject'
        trip.save()
        return redirect(request.META['HTTP_REFERER'])
    
    

class Driver_List(TemplateView):
    template_name = 'company/view_driver.html'
    def get_context_data(self, **kwargs):
        com=comp_reg.objects.get(user_id=self.request.user.id)

        context = super().get_context_data(**kwargs)
        context['dr'] = driver_reg.objects.filter(company_id=com.id)
        return context
    

class Driver_Search(TemplateView):
    template_name = 'company/driver_search.html'
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['dr'] = driver_reg.objects.filter(status='freelance',status1='available')
        return context

class request_driver(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        com=comp_reg.objects.get(user_id=self.request.user.id)
        req = driver_request()
        req.driver_id=id
        req.company_id=com.id
        req.status='pending'
        req.save()
        return render(request, 'company/company_index.html', {'message': "Request successfully added"})
    

class Driver_Request_Status(TemplateView):
    template_name = 'company/driver_request_status.html'
    def get_context_data(self, **kwargs):
        context = super(Driver_Request_Status,self).get_context_data(**kwargs)
        com=comp_reg.objects.get(user_id=self.request.user.id)

        driver_t = driver_request.objects.filter(company_id=com.id)
        context['driver_t'] = driver_t
        return context

class Trip_view(TemplateView):
    template_name = 'company/view_trip.html'
    def get_context_data(self, **kwargs):
        context = super(Trip_view,self).get_context_data(**kwargs)
        com=comp_reg.objects.get(user_id=self.request.user.id)

        user_t = trip_request.objects.filter(status='approval',company_id=com.id)
        context['user_t'] = user_t
        return context
    

class Vehicle_List(TemplateView):
    template_name = 'company/view_vehicle.html'
    def get_context_data(self, **kwargs):
        com=comp_reg.objects.get(user_id=self.request.user.id)
        context = super().get_context_data(**kwargs)
        today = datetime.date.today()
        context = {'today' : today }
        context['v_list'] = add_vehicle.objects.filter(company_id=com.id)
        return context
    

class Assign_driver(TemplateView):
    template_name ='company/assign_trip_to_driver.html'
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        com=comp_reg.objects.get(user_id=self.request.user.id)

        id = self.request.GET['id']
        trip = trip_request.objects.get(id=id)
        
        dri_req=driver_request.objects.get(company_id=com.id,status='approved')
        if dri_req is not None:
            veh1=add_vehicle.objects.filter(driver_id=dri_req.driver_id,status='available')
            dri1= driver_reg.objects.filter(company_id=com.id,status='freelance',status1='available')
            context['veh1']= veh1
            context['dri1']= dri1


        aval_dri_veh=trip_request.objects.filter(status='assigned')
        veh=add_vehicle.objects.filter(company_id=com.id,status='available')
        dri= driver_reg.objects.filter(company_id=com.id,status='hired',status1='available')
        
        context['trip']= trip
        context['dri']= dri
        context['veh']= veh
        context['aval_dri_veh']= aval_dri_veh
  
        return context

    def post(self, request, *args, **kwargs):
        id = self.request.GET['id']
        trip_amt = request.POST['trip_amt']
        kms = request.POST['kms']
        id=request.POST['id']
        id2 = request.POST['id2']
        driver = request.POST['driver']
        vehicle=request.POST['vehicle']
        total=int(trip_amt)*int(kms)
        se=assign_trip()
        si=trip_request.objects.get(id=id)
        si.status='assigned'
        se.km_per_amt=trip_amt
        se.kms=kms
        se.total_amt=total
        se.driver_id=driver
        se.veh_id=vehicle
        se.comp_id=id2
        se.trip_id=id
        se.status='assigned'
        se.save()
        si.save()
        return render(request, 'company/company_index.html', {'message': "successfully added"})

    


class Add_feedback(TemplateView):
    template_name = 'company/feedback.html'
    def post(self, request, *args, **kwargs):
        user=User.objects.get(id=self.request.user.id)
        name= request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        feedback=request.POST['feedback']

        feed = Feedback()
        feed.user=user
        feed.type='company'
        feed.name=name
        feed.email=email
        feed.subject=subject
        feed.feedback=feedback
        feed.status = 'added'
        feed.save()
        return render(request, 'company/feedback.html', {'message': "feedback added"})

class c_feedback_reply(TemplateView):
    template_name = 'company/view_feedback.html'

    def get_context_data(self, **kwargs):
        context = super(c_feedback_reply,self).get_context_data(**kwargs)

        reply = Feedback.objects.filter(status='replied',type='company',user_id=self.request.user.id)

        context['reply'] = reply
        return context
    
class profile_view(TemplateView):
    template_name = 'company/view_profile.html'
    def get_context_data(self, **kwargs):
        context = super(profile_view,self).get_context_data(**kwargs)
        
        app_comp = comp_reg.objects.filter(user_id=self.request.user.id)

        context['app_comp'] = app_comp
        return context

class edit_profile_view(TemplateView):
    template_name = 'company/company_edit_profile.html'
    def get_context_data(self, **kwargs):
        context = super(edit_profile_view,self).get_context_data(**kwargs)
        
        app_comp = comp_reg.objects.filter(user_id=self.request.user.id)

        context['app_comp'] = app_comp
        return context
    
    def post(self,request,*args,**kwargs):
        id = self.request.GET['id']
        user_id = request.POST['user_id']

        dri = comp_reg.objects.get(pk=id)
        user = User.objects.get(pk=user_id)
        user.first_name = request.POST['company_name']
        dri.mobile = request.POST['mobile']
        user.email = request.POST['email']
        dri.district = request.POST['district']
        dri.state = request.POST['state']
        dri.address = request.POST['address']
        dri.pincode = request.POST['pincode']
        user.save()
        dri.save()
        return render(request,'company/company_index.html',{'message':"Profile Updated"})
    
    
    
class trip_schedule(TemplateView):
    template_name ='company/schedule_trip.html'
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        com=comp_reg.objects.get(user_id=self.request.user.id)

        tr=trip_request.objects.filter(company_id=com.id,status="paid")
        at=assign_trip.objects.all()
        context['tr']= tr
        context['at']= at
        return context
    
    def post(self, request, *args, **kwargs):
        id = request.POST['id']
        se=trip_request.objects.get(pk=id)
        se.time=request.POST['time']
        se.date=request.POST['date']
        se.status='scheduled'
        se.save()
        return render(request, 'company/company_index.html', {'message': "successfully added"})
    
class All_Trip(TemplateView):
    template_name="company/all_trip.html"
    def get_context_data(self, **kwargs):
        context = super(All_Trip,self).get_context_data(**kwargs)

        trip_stat = trip_request.objects.filter(payment="paid")
        ts = assign_trip.objects.all()
        context['trip_stat'] = trip_stat
        context['ts'] = ts
        return context
    
    
class monthly_report(TemplateView):
    template_name ='company/monthly_report.html'
    
    # def get_context_data(self, **kwargs):
    #     context =super(monthly_report,self).get_context_data(**kwargs)
    #     tri = trip_request.objects.all()
    #     context['tri']= tri
    #     return context
    def post(self,request,*args,**kwargs):
        # id = request.POST['id']
        options= request.POST['options']
        # ang=assign_trip.objects.get(id=id)
        if options=='user':
            user=assign_trip.objects.all()
            return render(request,'company/user_report.html',{'result':user})
        elif options=='driver':
            driver=assign_trip.objects.all()
            return render(request,'company/driver_report.html',{'result':driver})
        elif options=='trip':
            trip=assign_trip.objects.all()
            return render(request,'company/trip_report.html',{'result':trip})
        else:
            return render(request,'company/monthly_report.html')
        


class user_report(TemplateView):
    template_name = 'admin/user_report.html'

class driver_report(TemplateView):
    template_name = 'admin/driver_report.html'

class trip_report(TemplateView):
    template_name = 'admin/trip_report.html'

class Leave_View(TemplateView):
    template_name="company/leave_view.html"
    def get_context_data(self, **kwargs):
        context = super(Leave_View,self).get_context_data(**kwargs)
        com=comp_reg.objects.get(user_id=self.request.user.id)

        l_view = driver_leave.objects.filter(company_id=com.id,status="pending")
        context['l_view'] = l_view
        return context

class Leave_Approve(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        leave = driver_leave.objects.get(pk=id)
        leave.status='approved'
        leave.save()
        return render(request,'company/company_index.html',{'message':"Leave Approved"})

class Leave_Reject(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        leave = driver_leave.objects.get(pk=id)
        leave.status='rejected'
        leave.save()
        return render(request,'company/company_index.html',{'message':"Leave Rejected"})
    

class Approved_Leave_View(TemplateView):
    template_name="company/approved_leave_view.html"
    def get_context_data(self, **kwargs):
        context = super(Approved_Leave_View,self).get_context_data(**kwargs)
        com=comp_reg.objects.get(user_id=self.request.user.id)

        l_view = driver_leave.objects.filter(company_id=com.id,status="approved")
        context['l_view'] = l_view
        return context
    

class Rejected_Leave_View(TemplateView):
    template_name="company/rejected_leave_view.html"
    def get_context_data(self, **kwargs):
        context = super(Rejected_Leave_View,self).get_context_data(**kwargs)
        com=comp_reg.objects.get(user_id=self.request.user.id)

        l_view = driver_leave.objects.filter(company_id=com.id,status="rejected")
        context['l_view'] = l_view
        return context
    


class Driver_Available(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        driver = driver_reg.objects.get(pk=id)
        driver.status1='available'
        driver.save()
        return render(request,'company/company_index.html',{'message':"Driver is now Available"})

class Driver_UnAvailable(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        driver = driver_reg.objects.get(pk=id)
        driver.status1='unavailable'
        driver.save()
        return render(request,'company/company_index.html',{'message':"Driver is now Unavailable"})
    
    
# class Update_Driver(TemplateView):

#     template_name = 'company/update_driver.html'
#     def get_context_data(self, *args, **kwargs):
#         id = self.request.GET['id']
#         context = super().get_context_data(*args, **kwargs)  
        
#         driver = driver_reg.objects.filter(id=id)

#         context['driver'] = driver
#         return context
    
#     def post(self , request,*args,**kwargs):
        
#         id = self.request.GET['id']
#         mobile=request.POST['mobile']
#         license_no=request.POST['license_no']
#         email=request.POST['email']
#         state=request.POST['state']
#         district=request.POST['district']
#         gender=request.POST['gender']
#         DateOB=request.POST['DateOB']
#         pincode=request.POST['pincode']
#         address=request.POST['address']


#         table_dri= driver_reg()
#         table_dri.mobile=mobile
#         table_dri.license_no=license_no
#         table_dri.state=state
#         table_dri.DateOB=DateOB
#         table_dri.gender=gender
#         table_dri.address= address
#         table_dri.district=district
#         table_dri.pincode=pincode
#         table_dri.save()
        

#         return render(request, 'company/company_index.html', {'message': "Successfully Updated"})     