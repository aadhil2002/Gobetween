from django.urls import path
from gobetween_app.company_views import Add_UPI, Approved_Leave_View, Available, Driver_Available, Driver_Request_Status, Driver_Search, Driver_UnAvailable, Leave_Approve, Leave_Reject, Leave_View, Rejected_Leave_View, UnAvailable, Update_Vehicle, c_feedback_reply, company_index_view,Add_Vehicle,Add_Driver,User_Request,Trip_Accept,Trip_Reject,Driver_List,Trip_view,Vehicle_List,Assign_driver,Add_feedback,profile_view,edit_profile_view, request_driver,trip_schedule,monthly_report,user_report,All_Trip,driver_report,trip_report







urlpatterns = [
    path('',company_index_view.as_view()),
    path('add_vehicle',Add_Vehicle.as_view()),
    path('add_upi',Add_UPI.as_view()),
    path('add_driver',Add_Driver.as_view()),
    path('User_Request',User_Request.as_view()),
    path('approve',Trip_Accept.as_view()),
    path('reject',Trip_Reject.as_view()),
    path('Driver_List',Driver_List.as_view()),
    path('Trip_view',Trip_view.as_view()),
    path('view_vehicle',Vehicle_List.as_view()),
    path('assign_driver',Assign_driver.as_view()),
    path('feedback',Add_feedback.as_view()),
    path('c_view_feedback',c_feedback_reply.as_view()),
    path('profile_view',profile_view.as_view()),
    path('comp_edit_profile',edit_profile_view.as_view()),
    path('trip_schedule',trip_schedule.as_view()),
    path('monthly_report',monthly_report.as_view()),
    path('user_report',user_report.as_view()),
    path('driver_report',driver_report.as_view()),
    path('trip_report',trip_report.as_view()),
    path('all_trip',All_Trip.as_view()),
    path('Available',Available.as_view()),
    path('UnAvailable',UnAvailable.as_view()),
    path('Update_vehicle',Update_Vehicle.as_view()),
    path('Driver_Search',Driver_Search.as_view()),
    path('request_driver',request_driver.as_view()),
    path('Driver_Request_Status',Driver_Request_Status.as_view()),
    path('leave_view',Leave_View.as_view()),
    path('approved_leave_view',Approved_Leave_View.as_view()),
    path('rejected_leave_view',Rejected_Leave_View.as_view()),
    path('leave_approve',Leave_Approve.as_view()),
    path('leave_reject',Leave_Reject.as_view()),
    path('Driver_UnAvailable',Driver_UnAvailable.as_view()),
    path('Driver_Available',Driver_Available.as_view())
]

def urls():
    return urlpatterns, 'company', 'company'