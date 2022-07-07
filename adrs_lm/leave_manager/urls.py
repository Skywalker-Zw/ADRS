from django.urls import path
from .views import LeaveCreate, LeaveDetail, LeaveList, LeaveUpdate

urlpatterns = [
    path('', LeaveList.as_view(), name='leaves'),
    path('leave/<int:pk>', LeaveDetail.as_view(), name='leave'),
    path('leave_create/', LeaveCreate.as_view(), name='leave_create'),
    path('leave_update/<int:pk>', LeaveUpdate.as_view(), name='leave_update'),
]
