from django.contrib.auth.models import User
from django.views.generic import TemplateView, View
from django.shortcuts import render,redirect
from gobetween_app.models import  Feedback, add_vehicle, add_vehicle_type, comp_reg, driver_reg,driver_request,assign_trip, trip_request
from django.utils import timezone
import datetime


class driver_index(TemplateView):
    template_name="freelance_driver/driver_index.html"

    def get_context_data(self, **kwargs):
        com=driver_reg.objects.get(user_id=self.request.user.id)
        context = super().get_context_data(**kwargs)
        today = datetime.date.today()
        context = {'today' : today }
        context['v_list'] = add_vehicle.objects.filter(driver_id=com.id)
        driver = driver_reg.objects.filter(user_id=self.request.user.id)
        context['driver'] = driver
        return context


class Add_UPI(TemplateView):
    template_name = 'freelance_driver/add_payment_UPI.html'

    def get_context_data(self, **kwargs):
        context = super(Add_UPI,self).get_context_data(**kwargs)
        
        upi = driver_reg.objects.get(user_id=self.request.user.id)
        
        context['upi'] = upi
        return context
    
    def post(self,request,*arg,**kwargs):
        upi_id=request.POST['upi_id']
        comp = driver_reg.objects.get(user_id=self.request.user.id)
        

        table_loc= comp
        table_loc.qrcode=upi_id
        table_loc.save()
            
        return render(request,'freelance_driver/driver_index.html',{'message':'Successfully Added'})        

    


class company_view(TemplateView):
    template_name="freelance_driver/company_view.html"
    def get_context_data(self, **kwargs):
        context = super(company_view,self).get_context_data(**kwargs)

        company_list = comp_reg.objects.all()
        driver = driver_reg.objects.filter(user_id=self.request.user.id)
        
        context['driver'] = driver
        context['company_list'] = company_list
        return context

class company_request(TemplateView):
    template_name = 'freelance_driver/company_request.html'
    
    def get_context_data(self, **kwargs):
        context = super(company_request,self).get_context_data(**kwargs)
        com=driver_reg.objects.get(user_id=self.request.user.id)
        comp = driver_request.objects.filter(driver_id=com.id,status='pending')
        
        context['comp'] = comp
        return context

    
class C_Approve_Request(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        id2 = request.GET['id2']
        req = driver_request.objects.get(id=id)
        req.status='approved'
        com=driver_reg.objects.get(user_id=self.request.user.id)
        com.company_id=id2
        com.save()
        req.save()
        return render(request,'freelance_driver/driver_index.html',{'message':"Request Approved"})
    

class C_Reject_Request(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        req = driver_request.objects.filter(id=id)
        req.status='rejected'
        req.save()
        return render(request,'freelance_driver/driver_index.html',{'message':"Request Rejected"}) 

class Add_feedback(TemplateView):
    template_name = 'freelance_driver/feedback.html'


    def post(self, request, *args, **kwargs):
        user=User.objects.get(id=self.request.user.id)
        name= request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        feedback=request.POST['feedback']

        feed = Feedback()
        feed.user=user
        feed.type='freelance_driver'
        feed.name=name
        feed.email=email
        feed.subject=subject
        feed.feedback=feedback
        feed.status = 'added'
        feed.save()
        return render(request, 'freelance_driver/feedback.html', {'message': "feedback added"})


class d_feedback_replay(TemplateView):
    template_name = 'freelance_driver/view_feedback.html'

    def get_context_data(self, **kwargs):
        context = super(d_feedback_replay,self).get_context_data(**kwargs)
        replay = Feedback.objects.filter(status='replied',type='freelance_driver',user_id=self.request.user.id)
        
        context['replay'] = replay
        return context
    
class profile_view(TemplateView):
    template_name = 'freelance_driver/view_profile.html'
    def get_context_data(self, **kwargs):
        context = super(profile_view,self).get_context_data(**kwargs)
        
        driver = driver_reg.objects.filter(user_id=self.request.user.id)
        
        context['driver'] = driver
        return context
    
class company_search(TemplateView):
    template_name="freelance_driver/company_search.html"
    def get_context_data(self, **kwargs):
        context = super(company_search,self).get_context_data(**kwargs)

        company_list = comp_reg.objects.all()
   
        context['company_list'] = company_list
        return context

class edit_profile_view(TemplateView):
    template_name = 'freelance_driver/driver_edit_profile.html'
    def get_context_data(self, **kwargs):
        context = super(edit_profile_view,self).get_context_data(**kwargs)

        driver = driver_reg.objects.filter(user_id=self.request.user.id)
        
        context['driver'] = driver
        return context
    
    def post(self,request,*args,**kwargs):
        id = self.request.GET['id']
        user_id = request.POST['user_id']
        dri = driver_reg.objects.get(pk=id)
        user = User.objects.get(pk=user_id)
        user.first_name = request.POST['driver_name']
        dri.mobile = request.POST['mobile']
        user.email = request.POST['email']
        dri.license_no = request.POST['license_no']
        dri.DateOB = request.POST['DateOB']
        dri.gender = request.POST['gender']
        dri.district = request.POST['district']
        dri.state = request.POST['state']
        dri.address = request.POST['address']
        dri.pincode = request.POST['pincode']
        dri.photo=request.FILES['uploadFromPC']
        dri.driving_experience=request.POST['driving_exp']
        user.save()
        dri.save()
        return render(request,'freelance_driver/driver_index.html',{'message':"Profile Updated"})
    
        

class assigned_trip(TemplateView):
    template_name = 'freelance_driver/view_assigned_trips.html'
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        com=driver_reg.objects.get(user_id=self.request.user.id)

        at=assign_trip.objects.filter(driver_id=com.id,status="assigned")
       

        context['at']= at 
    
        
        return context
    
    def post(self,request,*args,**kwargs):
        id = request.POST['id']
        id2 = request.POST['id2']
        id3 = request.POST['id3']
        id4 = request.POST['id4']
        tr = assign_trip.objects.get(pk=id)
        if id3 == 'freelance':
            tr1 = driver_reg.objects.get(id=id2)
            tr1.company_id=None
            tr1.save()
            driver_request.objects.get(driver_id=id2,company_id=id4).delete()
            tr.status='completed'
            tr.save()
        else:
            tr.status='completed'
            tr.save()

        return render(request, 'freelance_driver/driver_index.html', {'message': "Trip Completed"})
    

class completed_trip(TemplateView):
    template_name = 'freelance_driver/completed_trips.html'

    def get_context_data(self, **kwargs):
        context = super(completed_trip,self).get_context_data(**kwargs)
        com=driver_reg.objects.get(user_id=self.request.user.id)
        completed = assign_trip.objects.filter(driver_id=com.id,status='completed')
        
        
        context['completed'] = completed
        return context


class User_Request(TemplateView):
    template_name = 'freelance_driver/user_request.html'
    def get_context_data(self, **kwargs):
        context = super(User_Request,self).get_context_data(**kwargs)
        com=driver_reg.objects.get(user_id=self.request.user.id)
        
        user_r = trip_request.objects.filter(driver_id=com.id,status='pending')
       
        context['user_r'] = user_r
        return context
    
    def post(self , request,*args,**kwargs):
        user = driver_reg.objects.get(id=self.request.user.id)
        t=trip_request()
        t.driver_id=user.id
        t.user = user
        t.save()


        return render(request, 'freelance_driver/user_request.html', {'message': "successfully added"})
    

class D_Add_Vehicle(TemplateView):
    template_name = 'freelance_driver/add_vehicle.html'

    def get_context_data(self, **kwargs):
        context = super(D_Add_Vehicle,self).get_context_data(**kwargs)
        
        veh=add_vehicle_type.objects.all()
       
        context['veh'] = veh
        return context
    
    def post(self , request,*args,**kwargs):
        
        com=driver_reg.objects.get(user_id=self.request.user.id)
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
            return render(request,'freelance_driver/add_vehicle.html',{'message':"already exist"})
        else:
            vehicle = add_vehicle()
            vehicle.driver_id=com.id
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


            return render(request, 'freelance_driver/driver_index.html', {'message': "Successfully Added"})
        


class D_Update_Vehicle(TemplateView):

    template_name = 'freelance_driver/update_vehicle.html'
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


        return render(request, 'freelance_driver/driver_index.html', {'message': "Successfully Updated"})
         
    

class D_Available(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        vehicle = add_vehicle.objects.get(pk=id)
        vehicle.status='available'
        vehicle.save()
        return redirect(request.META['HTTP_REFERER'])

class D_UnAvailable(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        vehicle = add_vehicle.objects.get(pk=id)
        vehicle.status='unavailable'
        vehicle.save()
        return redirect(request.META['HTTP_REFERER'])
    

class D_Vehicle_List(TemplateView):
    template_name = 'freelance_driver/view_vehicle.html'
    def get_context_data(self, **kwargs):
        com=driver_reg.objects.get(user_id=self.request.user.id)
        context = super().get_context_data(**kwargs)
        today = datetime.date.today()
        
        context = {'today' : today }
        context['v_list'] = add_vehicle.objects.filter(driver_id=com.id)
        
        return context
    
        

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
    
class D_Trip_view(TemplateView):
    template_name = 'freelance_driver/view_trip.html'
    def get_context_data(self, **kwargs):
        context = super(D_Trip_view,self).get_context_data(**kwargs)
        com=driver_reg.objects.get(user_id=self.request.user.id)
        user_t = trip_request.objects.filter(status='approval',driver_id=com.id)
        context['user_t'] = user_t
        return context
     

class D_Assign_trip(TemplateView):
    template_name ='freelance_driver/assign_trip.html'
    
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        com=driver_reg.objects.get(user_id=self.request.user.id)

        id = self.request.GET['id']
        trip = trip_request.objects.get(id=id)
        # aval_dri_veh=trip_request.objects.filter(status='assigned')
        veh=add_vehicle.objects.filter(driver_id=com.id,status='available')

        context['trip']= trip
        context['veh']= veh
        # context['aval_dri_veh']= aval_dri_veh
  
        return context

    def post(self, request, *args, **kwargs):
        id = self.request.GET['id']
        trip_amt = request.POST['trip_amt']
        kms = request.POST['kms']
        id=request.POST['id']
        id2 = request.POST['id2']
        vehicle=request.POST['vehicle']
        total=int(trip_amt)*int(kms)
        se=assign_trip()
        si=trip_request.objects.get(id=id)
        si.status='assigned'
        se.km_per_amt=trip_amt
        se.kms=kms
        se.total_amt=total
        se.driver_id=id2
        se.veh_id=vehicle
        se.trip_id=id
        se.status='assigned'
        se.save()
        si.save()
        return render(request, 'freelance_driver/driver_index.html', {'message': "successfully added"})

class Driver_Available(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        driver = driver_reg.objects.get(pk=id)
        driver.status1='available'
        driver.save()
        return render(request,'freelance_driver/driver_index.html',{'message':"Driver is now Available"})
    
class Driver_UnAvailable(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        driver = driver_reg.objects.get(pk=id)
        driver.status1='unavailable'
        driver.save()
        return render(request,'freelance_driver/driver_index.html',{'message':"Driver is now Unavailable"})