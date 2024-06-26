from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.views.generic.base import View
from gobetween_app.models import Feedback, user_reg, comp_reg, driver_reg,Complaint,location_add,add_vehicle_type

class admin_index_view(TemplateView):
    template_name = 'admin/admin_index.html'
    


class company_verify(TemplateView):
    template_name = 'admin/company_verify.html'

    def get_context_data(self, **kwargs):
        context = super(company_verify,self).get_context_data(**kwargs)

        app_company = comp_reg.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')

        context['app_company'] = app_company
        return context
    
    def post(self, request, *args, **kwargs):
        id = request.POST['id']
        reason = request.POST['reason']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.is_active='0'
        user.save()
        act = comp_reg.objects.get(user_id=id)
        act.reject_reason=reason
        act.save()

        return render(request,'admin/admin_index.html',{'message':"Account Removed"})


class ApproveView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.save()
        return render(request,'admin/admin_index.html',{'message':" Account Approved"})


    

class driver_verify(TemplateView):
     template_name = 'admin/driver_verify.html'

     def get_context_data(self, **kwargs):
         context = super(driver_verify,self).get_context_data(**kwargs)
         app_driver = driver_reg.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1',status='hired')
         context['app_driver'] = app_driver
         return context
        
     def post(self, request, *args, **kwargs):
        id = request.POST['id']
        reason = request.POST['reason']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.is_active='0'
        user.save()
        act = driver_reg.objects.get(user_id=id)
        act.reject_reason=reason
        act.save()
        return render(request,'admin/admin_index.html',{'message':" Account Rejected"})
     
class freelance_driver_verify(TemplateView):
     template_name = 'admin/freelance_driver_verify.html'

     def get_context_data(self, **kwargs):
         context = super(freelance_driver_verify,self).get_context_data(**kwargs)
         app_driver = driver_reg.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1',status='freelance')
         context['app_driver'] = app_driver
         return context
        
     def post(self, request, *args, **kwargs):
        id = request.POST['id']
        reason = request.POST['reason']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.is_active='0'
        user.save()
        act = driver_reg.objects.get(user_id=id)
        act.reject_reason=reason
        act.save() 
        return render(request,'admin/admin_index.html',{'message':" Account Rejected"})

    
class driver_view(TemplateView):
    template_name = 'admin/driver_view.html'

    def get_context_data(self, **kwargs):
        context = super(driver_view,self).get_context_data(**kwargs)
        app_company = driver_reg.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1',status='hired')
        context['app_company'] = app_company
        return context
    
    def post(self, request, *args, **kwargs):
        id = request.POST['id']
        reason = request.POST['reason']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.is_active='0'
        user.save()
        act = driver_reg.objects.get(user_id=id)
        act.reject_reason=reason
        act.save()

        return render(request,'admin/admin_index.html',{'message':"Account Removed"})
    
class freelance_driver_view(TemplateView):
    template_name = 'admin/freelance_driver_view.html'

    def get_context_data(self, **kwargs):
        context = super(freelance_driver_view,self).get_context_data(**kwargs)
        app_company = driver_reg.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1',status='freelance')
        context['app_company'] = app_company
        return context
    
    def post(self, request, *args, **kwargs):
        id = request.POST['id']
        reason = request.POST['reason']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.is_active='0'
        user.save()
        act = driver_reg.objects.get(user_id=id)
        act.reject_reason=reason
        act.save()

        return render(request,'admin/admin_index.html',{'message':"Account Removed"})

class company_view(TemplateView):
    template_name = 'admin/company_view.html'

    def get_context_data(self, **kwargs):
        context = super(company_view,self).get_context_data(**kwargs)
        app_company = comp_reg.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')
        context['app_company'] = app_company
        return context
    
    def post(self, request, *args, **kwargs):
        id = request.POST['id']
        reason = request.POST['reason']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.is_active='0'
        user.save()
        act = comp_reg.objects.get(user_id=id)
        act.reject_reason=reason
        act.save()

        return render(request,'admin/admin_index.html',{'message':"Account Removed"})



class user_view(TemplateView):
    template_name = 'admin/user_view.html'

    def get_context_data(self, **kwargs):
        context = super(user_view,self).get_context_data(**kwargs)
        app_company = user_reg.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')
        context['app_company'] = app_company
        return context
    
    def post(self, request, *args, **kwargs):
        id = request.POST['id']
        reason = request.POST['reason']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.is_active='0'
        user.save()
        act = user_reg.objects.get(user_id=id)
        act.reject_reason=reason
        act.save()

        return render(request,'admin/admin_index.html',{'message':"Account Removed"})

class Complaint_View(TemplateView):
    template_name = 'admin/view_complaint.html'

    def get_context_data(self, **kwargs):
        context = super(Complaint_View,self).get_context_data(**kwargs)

        compl = Complaint.objects.filter(status='added')

        context['compl'] = compl
        return context

    def post(self, request, *args, **kwargs):
        id = request.POST['id']
        action = request.POST['action']
        act = Complaint.objects.get(id=id)
        act.action = action
        act.status = 'replied'
        act.save()

        return redirect(request.META['HTTP_REFERER'])


class u_feedback_View(TemplateView):
    template_name = 'admin/user_feedback.html'

    def get_context_data(self, **kwargs):
        context = super(u_feedback_View,self).get_context_data(**kwargs)

        compl = Feedback.objects.filter(status='added',type='user')

        context['compl'] = compl
        return context

    def post(self, request, *args, **kwargs):
        id = request.POST['id']
        action = request.POST['action']
        act = Feedback.objects.get(id=id)
        act.action = action

        act.status = 'replied'
        act.save()

        return redirect(request.META['HTTP_REFERER'])

class d_feedback_View(TemplateView):
    template_name = 'admin/driver_feedback.html'

    def get_context_data(self, **kwargs):
        context = super(d_feedback_View,self).get_context_data(**kwargs)

        compl = Feedback.objects.filter(status='added',type='driver')

        context['compl'] = compl
        return context

    def post(self, request, *args, **kwargs):
        id = request.POST['id']
        action = request.POST['action']
        act = Feedback.objects.get(id=id)
        act.action = action

        act.status = 'replied'
        act.save()

        return redirect(request.META['HTTP_REFERER'])
    


class fd_feedback_View(TemplateView):
    template_name = 'admin/freelance_driver_feedback.html'

    def get_context_data(self, **kwargs):
        context = super(fd_feedback_View,self).get_context_data(**kwargs)

        compl = Feedback.objects.filter(status='added',type='freelance_driver')

        context['compl'] = compl
        return context

    def post(self, request, *args, **kwargs):
        id = request.POST['id']
        action = request.POST['action']
        act = Feedback.objects.get(id=id)
        act.action = action

        act.status = 'replied'
        act.save()

        return redirect(request.META['HTTP_REFERER'])

class c_feedback_View(TemplateView):
    template_name = 'admin/company_feedback.html'

    def get_context_data(self, **kwargs):
        context = super(c_feedback_View,self).get_context_data(**kwargs)

        compl = Feedback.objects.filter(status='added',type='company')

        context['compl'] = compl
        return context

    def post(self, request, *args, **kwargs):
        # complaint = actions.objects.get(user_id=self.request.id)
        id = request.POST['id']
        action = request.POST['action']
        act = Feedback.objects.get(id=id)
        # act.complaint=complaint
        act.action = action

        act.status = 'replied'
        act.save()

        return redirect(request.META['HTTP_REFERER'])


class add_location(TemplateView):
    template_name = 'admin/add_location.html'
    def post(self,request,*arg,**kwargs):
        location=request.POST['location']
        print(location)
       
        if location_add.objects.filter(location=location):
            print ('pass')
            return render(request,'admin/add_location.html',{'message':"location already added"})

        else:
           
            table_loc= location_add()
            table_loc.location=location
            table_loc.save()
            
            return render(request,'admin/add_location.html',{'message':'Successfully Added'})
        


class vehicle_type(TemplateView):
    template_name = 'admin/vehicle_type.html'
    def post(self,request,*arg,**kwargs):
        veh_type=request.POST['veh_type']
        print(veh_type)
       
        if add_vehicle_type.objects.filter(veh_type=veh_type):
            print ('pass')
            return render(request,'admin/vehicle_type.html',{'message':"Vehicle already added"})

        else:
           
            table_veh= add_vehicle_type()
            table_veh.veh_type=veh_type
            table_veh.save()
            
            return render(request,'admin/vehicle_type.html',{'message':'Successfully Added'})