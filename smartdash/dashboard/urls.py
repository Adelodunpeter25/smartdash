from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='home'),
    path('utilities/', views.utilities_page, name='utilities'),
    path('quotes/', views.random_quote, name='random_quote'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('profile/', views.profile_view, name='profile'),
    path('calculator/', views.calculator_view, name='calculator'),
    path('notepad/', views.notepad_view, name='notepad'),
    path('unit_converter/', views.unit_converter_view, name='unit_converter'),
]
