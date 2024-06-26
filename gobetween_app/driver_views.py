from django.contrib.auth.models import User
from django.views.generic import TemplateView, View
from django.shortcuts import render,redirect
from gobetween_app.models import  Feedback, add_vehicle,comp_reg, driver_leave, driver_reg,driver_request,assign_trip
from django.utils import timezone
import datetime


class driver_index(TemplateView):
    template_name="driver/driver_index.html"

    def get_context_data(self, **kwargs):
        com=driver_reg.objects.get(user_id=self.request.user.id)
        context = super().get_context_data(**kwargs)
        today = datetime.date.today()
        context = {'today' : today }
        context['v_list'] = add_vehicle.objects.filter(driver_id=com.id)
        driver = driver_reg.objects.filter(user_id=self.request.user.id)
        context['driver'] = driver
        return context



class company_view(TemplateView):
    template_name="driver/company_view.html"
    def get_context_data(self, **kwargs):
        context = super(company_view,self).get_context_data(**kwargs)

        company_list = comp_reg.objects.all()
        driver = driver_reg.objects.filter(user_id=self.request.user.id)
        
        context['driver'] = driver
        context['company_list'] = company_list
        return context



    


class Add_feedback(TemplateView):
    template_name = 'driver/feedback.html'


    def post(self, request, *args, **kwargs):
        user=User.objects.get(id=self.request.user.id)
        name= request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        feedback=request.POST['feedback']

        feed = Feedback()
        feed.user=user
        feed.type='driver'
        feed.name=name
        feed.email=email
        feed.subject=subject
        feed.feedback=feedback
        feed.status = 'added'
        feed.save()
        return render(request, 'driver/feedback.html', {'message': "feedback added"})


class d_feedback_replay(TemplateView):
    template_name = 'driver/view_feedback.html'

    def get_context_data(self, **kwargs):
        context = super(d_feedback_replay,self).get_context_data(**kwargs)
        replay = Feedback.objects.filter(status='replied',type='driver',user_id=self.request.user.id)
        context['replay'] = replay
        return context
    
class profile_view(TemplateView):
    template_name = 'driver/view_profile.html'
    def get_context_data(self, **kwargs):
        context = super(profile_view,self).get_context_data(**kwargs)
        
        driver = driver_reg.objects.filter(user_id=self.request.user.id)
        
        context['driver'] = driver
        return context
    


class edit_profile_view(TemplateView):
    template_name = 'driver/driver_edit_profile.html'
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
        dri.photo = request.FILES['driver_photo']
        dri.driving_experience = request.POST['driving_exp']
        user.save()
        dri.save()
        return render(request,'driver/driver_index.html',{'message':"Profile Updated"})
    
        

class assigned_trip(TemplateView):
    template_name = 'driver/view_assigned_trips.html'
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        com=driver_reg.objects.get(user_id=self.request.user.id)

        at=assign_trip.objects.filter(driver_id=com.id,status="assigned")
        

        context['at']= at 
      
        
        return context
    
    def post(self,request,*args,**kwargs):
        id = request.POST['id']
        tr = assign_trip.objects.get(pk=id)
      
        tr.status='completed'
        tr.save()

        return render(request, 'driver/driver_index.html', {'message': "Trip Completed"})
    

class completed_trip(TemplateView):
    template_name = 'driver/completed_trips.html'

    def get_context_data(self, **kwargs):
        context = super(completed_trip,self).get_context_data(**kwargs)
        com=driver_reg.objects.get(user_id=self.request.user.id)
        completed = assign_trip.objects.filter(driver_id=com.id,status='completed')
       
        

        
        context['completed'] = completed
        return context



     



class Apply_Leave(TemplateView):
    template_name = 'driver/apply_leave.html'
    def get_context_data(self, **kwargs):
        context = super(Apply_Leave,self).get_context_data(**kwargs)
        dri = driver_reg.objects.filter(user_id=self.request.user.id)
        
        context['driver'] = dri
        return context

    def post(self, request, *args, **kwargs):
        driver=driver_reg.objects.get(user_id=self.request.user.id)
        comp=request.POST['company']
        company=comp_reg.objects.get(id=comp)
        startdate=request.POST['startdate']
        enddate=request.POST['enddate']
        reason=request.POST['reason']
        no_of_days=request.POST['no_of_days']



        leave = driver_leave()
        leave.driver=driver
        leave.company=company
        leave.startdate=startdate
        leave.enddate=enddate
        leave.reason=reason
        leave.no_of_days=no_of_days
        leave.status='pending'
        leave.save()
        return render(request, 'driver/driver_index.html', {'message': "Leave Request Sent"})
    

class Leave_View(TemplateView):
    template_name = 'driver/leave_status.html'
    def get_context_data(self, **kwargs):
        context = super(Leave_View,self).get_context_data(**kwargs)
        dri = driver_reg.objects.get(user_id=self.request.user.id)
        leave = driver_leave.objects.filter(driver_id=dri.id)

        
        context['leave'] = leave
        return context
