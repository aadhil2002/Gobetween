from django.urls import path

from gobetween_app.freelance_driver_views import Add_UPI, Add_feedback, C_Approve_Request, C_Reject_Request, D_Add_Vehicle, D_Assign_trip, D_Available, D_Trip_view, D_UnAvailable, D_Update_Vehicle, D_Vehicle_List, Driver_Available, Driver_UnAvailable, Trip_Accept, Trip_Reject, User_Request, assigned_trip, company_request, company_search, company_view, completed_trip, d_feedback_replay, driver_index, edit_profile_view, profile_view










urlpatterns = [
    path('',driver_index.as_view()),
    path('company_view',company_view.as_view()),
    path('company_request',company_request.as_view()),
    path('company_search',company_search.as_view()),
    path('approve',Trip_Accept.as_view()),
    path('reject',Trip_Reject.as_view()),
    path('user_request',User_Request.as_view()),
    path('feedback',Add_feedback.as_view()),
    path('d_view_feedback',d_feedback_replay.as_view()),
    path('profile_view',profile_view.as_view()),
    path('view_profile',profile_view.as_view()),
    path('edit_profile',edit_profile_view.as_view()),
    path('assigned_trip',assigned_trip.as_view()),
    path('Completed_trips',completed_trip.as_view()),
    path('d_add_vehicle',D_Add_Vehicle.as_view()),
    path('d_vehicle_list',D_Vehicle_List.as_view()),
    path('Add_UPI',Add_UPI.as_view()),
    path('Available',D_Available.as_view()),
    path('UnAvailable',D_UnAvailable.as_view()),
    path('Update_vehicle',D_Update_Vehicle.as_view()),
    path('trip_view',D_Trip_view.as_view()),
    path('assigntrip',D_Assign_trip.as_view()),
    path('c_approve_request',C_Approve_Request.as_view()),
    path('c_reject_request',C_Reject_Request.as_view()),
    path('Driver_Available',Driver_Available.as_view()),
    path('Driver_UnAvailable',Driver_UnAvailable.as_view())
]

def urls():
    return urlpatterns, 'freelance_driver', 'freelance_driver'