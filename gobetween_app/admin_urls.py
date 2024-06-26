from django.urls import path
from django.views.generic import TemplateView

from gobetween_app.admin_views import  admin_index_view,company_verify,ApproveView, company_view, driver_verify, driver_view,Complaint_View, fd_feedback_View, freelance_driver_verify, freelance_driver_view,u_feedback_View,d_feedback_View,c_feedback_View,add_location, user_view,vehicle_type







urlpatterns = [
    path('',admin_index_view.as_view()),
    path('company_verify',company_verify.as_view()),
    path('driver_verify',driver_verify.as_view()),
    path('freelance_driver_verify',freelance_driver_verify.as_view()),
    path('company_view',company_view.as_view()),
    path('driver_view',driver_view.as_view()),
    path('freelance_driver_view',freelance_driver_view.as_view()),
    path('user_view',user_view.as_view()),
    path('approve',ApproveView.as_view()),
    path('view_complaint',Complaint_View.as_view()),
    path('u_view_feedback',u_feedback_View.as_view()),
    path('d_view_feedback',d_feedback_View.as_view()),
    path('fd_view_feedback',fd_feedback_View.as_view()),
    path('c_view_feedback',c_feedback_View.as_view()),
    path('add_location',add_location.as_view()),
    path('vehicle_type',vehicle_type.as_view()),
]

def urls():
    return urlpatterns, 'admin', 'admin'