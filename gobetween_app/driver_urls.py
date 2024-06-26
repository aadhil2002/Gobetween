from django.urls import path

from gobetween_app.driver_views import   Apply_Leave,  Leave_View, completed_trip, driver_index,company_view,Add_feedback,d_feedback_replay,profile_view,edit_profile_view,assigned_trip








urlpatterns = [
    path('',driver_index.as_view()),
    path('company_view',company_view.as_view()),
    path('feedback',Add_feedback.as_view()),
    path('d_view_feedback',d_feedback_replay.as_view()),
    path('profile_view',profile_view.as_view()),
    path('edit_profile',edit_profile_view.as_view()),
    path('assigned_trip',assigned_trip.as_view()),
    path('Completed_trips',completed_trip.as_view()),
    path('apply_leave',Apply_Leave.as_view()),
    path('leave_status',Leave_View.as_view()),
    


]

def urls():
    return urlpatterns, 'driver', 'driver'