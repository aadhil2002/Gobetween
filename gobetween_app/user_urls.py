from django.urls import path
from gobetween_app.user_views import Request_Company, Request_Driver, Trip_Track, driver_search, u_feedback_reply, user_index_view,edit_profile_view,company_search,trip_status,Add_complaint,Complaint_reply,Add_feedback,profile_view,trip_payment,View_Trip







urlpatterns = [
    path('',user_index_view.as_view()),
    path('edit_profile',edit_profile_view.as_view()),
    path('view_profile',profile_view.as_view()),
    path('company_search',company_search.as_view()),
    path('driver_search',driver_search.as_view()),
    path('trip_status',trip_status.as_view()),
    path('request_company',Request_Company.as_view()),
    path('request_driver',Request_Driver.as_view()),
    path('complaint',Add_complaint.as_view()),
    path('view_complaint',Complaint_reply.as_view()),
    path('feedback',Add_feedback.as_view()),
    path('view_feedback',u_feedback_reply.as_view()),
    path('trip_view',View_Trip.as_view()),
    path('trip_payment',trip_payment.as_view()),
    path('track_trip',Trip_Track.as_view())
]

def urls():
    return urlpatterns, 'user', 'user'