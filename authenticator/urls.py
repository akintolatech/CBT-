from django.urls import path
from . import views

# app_name = 'authenticator'

urlpatterns = [
    path('', views.index, name='index'),
    # path('accounts/login/', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('<int:test_id>/results/', views.mark_test, name='mark'),
    path('<int:test_id>/test/', views.test_questions, name='test_questions'),
    path('show_results/', views.view_results, name='results'),
    path('result_viewer/', views.results_viewer, name='results_viewer'),
    path('rv_login/', views.rv_login, name='rv_login'),
    # path('export_results/', views.export_results, name='export_results'),

]