from django.urls import path
from api import views
from django.contrib.auth import views as auth_views

app_name = ' api'

urlpatterns = [
    path('', views.form, name='form'),
    path('registration/', views.registration, name='registration'),
    path('submitanswer/', views.submitanswer, name='submitanswer'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('index/', views.index, name='index'),
    path('courses/', views.courses, name='courses'),
    path('about/', views.about, name='about'),
    path('trainers/', views.trainers, name='trainers'),
    path('events/', views.events, name='events'),
    path('pricing/', views.pricing, name='pricing'),
    path('contact/', views.contact, name='contact'),
    path('course-details', views.courseDetails, name='course-details'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user/', views.user, name='user'),
    path('admindashboard/', views.admindashboard, name='admindashboard'),
    path('viewquestions/', views.viewquestions, name='viewquestions'),
    path('questionsetupload/', views.questionsetupload, name='questionsetupload'),
    path('questionpanel/', views.questionpanel, name='questionpanel'),
    path('createquestions/', views.createquestions, name='createquestions'),
    path('displayquestions/<int:id>/', views.displayquestions, name='displayquestions'),
    path('displayquestion/', views.displayquestion, name='displayquestion'),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="passwrod_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='main/password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="main/password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='main/password/password_reset_complete.html'), name='password_reset_complete'),      
    
    path('createquestion/', views.create_question, name='createquestion'),
    path('showquestion/', views.show_question, name='showquestion'),

    path('displayquestionnn/', views.displayquestionnn, name='displayquestionnn'),
    path('landing/', views.landing, name='landing'),

    path('studentlogin/', views.studentlogin, name='studentlogin'),
]

