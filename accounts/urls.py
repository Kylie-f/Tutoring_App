from django.urls import path
from .views import SignUpView, TutorsListView, TutorDetailView, ScheduleView, add_availability, TutorProfileView
from . import views

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('tutors/', TutorsListView.as_view(), name='tutors_list'),  # URL pattern for tutors list
    path('tutors/<int:pk>/', TutorDetailView.as_view(), name='tutor_detail'),  # URL pattern for tutor detail
    path('schedule/', ScheduleView.as_view(), name='schedule'),
    path('add_availability/', add_availability, name='add_availability'),
    path('tutors/profile/<int:id>/', TutorProfileView.as_view(), name='tutor_profile'),  # Updated to ensure clarity
    path('edit_hours/<int:tutor_id>/', views.edit_hours, name='edit_hours'),
]



from django.urls import path
from .views import SignUpView, TutorsListView, TutorDetailView, ScheduleView, add_availability, TutorProfileView



