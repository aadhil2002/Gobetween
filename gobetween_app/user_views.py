
from urllib import request
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth import login


from gobetween_app.models import Feedback, driver_reg, location_add, user_reg,comp_reg,assign_trip,trip_request,Complaint


class user_index_view(TemplateView):
    template_name = 'user/user_index.html'
    
class profile_view(TemplateView):
    template_name = 'user/view_profile.html'
    def get_context_data(self, **kwargs):
        context = super(profile_view,self).get_context_data(**kwargs)
        
        app_user = user_reg.objects.filter(user_id=self.request.user.id)

        context['app_user'] = app_user
        return context

class edit_profile_view(TemplateView):
    template_name = 'user/edit_profile.html'
    def get_context_data(self, **kwargs):
        context = super(edit_profile_view,self).get_context_data(**kwargs)
        
        app_user = user_reg.objects.filter(user_id=self.request.user.id)

        context['app_user'] = app_user
        return context
    
    def post(self,request,*args,**kwargs):
        id = self.request.GET['id']
        user_id = request.POST['user_id']
        usr = user_reg.objects.get(pk=id)
        user = User.objects.get(pk=user_id)


        user.first_name = request.POST['driver_name']
        usr.mobile = request.POST['mobile']
        user.email = request.POST['email']
        usr.DateOfBirth = request.POST['DateOfBirth']
        usr.gender = request.POST['gender']
        usr.district = request.POST['district']
        usr.state = request.POST['state']
        usr.address = request.POST['address']
        usr.pincode = request.POST['pincode']
        user.save()    
        usr.save()
        return render(request,'user/user_index.html',{'message':"Profile Updated"})


class company_search(TemplateView):
    template_name="user/search_company.html"
    def get_context_data(self, **kwargs):
        context = super(company_search,self).get_context_data(**kwargs)

        company_list = comp_reg.objects.all()

        context['company_list'] = company_list
        return context

class driver_search(TemplateView):
    template_name="user/search_driver.html"
    def get_context_data(self, **kwargs):
        context = super(driver_search,self).get_context_data(**kwargs)

        driver_list = driver_reg.objects.filter(status="freelance",status1='available')

        context['driver_list'] = driver_list
        return context
    
class Request_Company(TemplateView):
    template_name = 'user/send_company_request_trip.html'
    def get_context_data(self, **kwargs):
        id1= self.request.GET['id']
        print(id1)
        context = super(Request_Company,self).get_context_data(**kwargs)
        
        loc=location_add.objects.all()

        view_details = comp_reg.objects.get(id=id1)
        context['view_details'] = view_details
        context['loc'] = loc
        return context

        
    def post(self , request,*args,**kwargs):
        id1=request.POST['id123']
        name = request.POST['name']
        pickup_place= request.POST['pickup_place']
        to_place= request.POST['to_place']
        mobile= request.POST['mobile']
        time= request.POST['time']
        date= request.POST['date']
        no_of_person= request.POST['no_of_person']
        purpose= request.POST['purpose']
      
        user = User.objects.get(id=self.request.user.id)
        t_req = trip_request()
        t_req.name=name
        t_req.company_id=id1
        t_req.mobile =mobile
        t_req.pickup_place =pickup_place
        t_req.to_place= to_place
        t_req.time = time
        t_req.date = date 
        t_req.no_of_person = no_of_person
        t_req.purpose = purpose
        t_req.status = 'pending'
        t_req.user = user
        t_req.save()


        return render(request, 'user/send_company_request_trip.html', {'message': "successfully added"})
    


class Request_Driver(TemplateView):
    template_name = 'user/send_driver_request_trip.html'
    def get_context_data(self, **kwargs):
        id1= self.request.GET['id']
        print(id1)
        context = super(Request_Driver,self).get_context_data(**kwargs)
        
        loc=location_add.objects.all()

        view_details = driver_reg.objects.get(id=id1)
        context['view_details'] = view_details
        context['loc'] = loc
        return context

        
    def post(self , request,*args,**kwargs):
        id1=request.POST['id123']
        name = request.POST['name']
        pickup_place= request.POST['pickup_place']
        to_place= request.POST['to_place']
        mobile= request.POST['mobile']
        time= request.POST['time']
        date= request.POST['date']
        no_of_person= request.POST['no_of_person']
        purpose= request.POST['purpose']
      
        user = User.objects.get(id=self.request.user.id)
        t_req = trip_request()
        t_req.name=name
        t_req.driver_id=id1
        t_req.mobile =mobile
        t_req.pickup_place =pickup_place
        t_req.to_place= to_place
        t_req.time = time
        t_req.date = date 
        t_req.no_of_person = no_of_person
        t_req.purpose = purpose
        t_req.status = 'pending'
        t_req.user = user
        t_req.save()


        return render(request, 'user/send_driver_request_trip.html', {'message': "successfully added"})

class trip_status(TemplateView):
    template_name="user/trip_status.html"
    def get_context_data(self, **kwargs):
        context = super(trip_status,self).get_context_data(**kwargs)
        ts = assign_trip.objects.filter(status="assigned")
        context['ts'] = ts
        return context
    

class Add_complaint(TemplateView):
    template_name = 'user/complaint.html'

    def post(self, request, *args, **kwargs):
        user=User.objects.get(id=self.request.user.id)
        name= request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        complaint=request.POST['complaint']

        com = Complaint()
        com.user=user
        com.name=name
        com.email=email
        com.subject=subject
        com.complaint=complaint
        com.status = 'added'
        com.save()
        return render(request, 'user/complaint_reg.html', {'message': "complaint added"})
    
    
class Complaint_reply(TemplateView):
    template_name = 'user/view_complaint.html'

    def get_context_data(self, **kwargs):
        context = super(Complaint_reply,self).get_context_data(**kwargs)

        reply = Complaint.objects.filter(status='replied')

        context['reply'] = reply
        return context
    

class Add_feedback(TemplateView):
    template_name = 'user/feedback.html'
    def post(self, request, *args, **kwargs):
        user=User.objects.get(id=self.request.user.id)
        name= request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        feedback=request.POST['feedback']

        feed = Feedback()
        feed.user=user
        feed.type='user'
        feed.name=name
        feed.email=email
        feed.subject=subject
        feed.feedback=feedback
        feed.status = 'added'
        feed.save()
        return render(request, 'user/feedback.html', {'message': "feedback added"})

class u_feedback_reply(TemplateView):
    template_name = 'user/view_feedback.html'

    def get_context_data(self, **kwargs):
        context = super(u_feedback_reply,self).get_context_data(**kwargs)

        reply = Feedback.objects.filter(status='replied',type='user',user_id=self.request.user.id)

        context['reply'] = reply
        return context
    

class trip_payment(TemplateView):
    template_name="user/payment.html"
    def get_context_data(self, **kwargs):
        context = super(trip_payment,self).get_context_data(**kwargs)
        id= self.request.GET['id']
        trip = assign_trip.objects.get(id=id)
        context['trip'] = trip
        return context
    
    def post(self, request, *args, **kwargs):
        id=request.POST['id']
        feed =trip_request.objects.get(id=id)
        feed.payment='paid'
        feed.status='paid'
        feed.save()
        return render(request, 'user/user_index.html', {'message': "paid"})

class View_Trip(TemplateView):
    template_name="user/trip_view.html"
    def get_context_data(self, **kwargs):
        context = super(View_Trip,self).get_context_data(**kwargs)

        trip_stat = trip_request.objects.filter(payment="paid",user_id=self.request.user.id)
        ts = assign_trip.objects.filter(status="completed")
        context['trip_stat'] = trip_stat
        context['ts'] = ts
        return context


class Trip_Track(TemplateView):
    template_name="user/track_trip.html"
    def get_context_data(self, **kwargs):
        context = super(Trip_Track,self).get_context_data(**kwargs)

        trip_stat = trip_request.objects.filter(payment="paid",user_id=self.request.user.id)
        ts = assign_trip.objects.filter(status="assigned")
        context['trip_stat'] = trip_stat
        context['ts'] = ts
        return context