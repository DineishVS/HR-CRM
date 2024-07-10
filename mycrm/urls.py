from django.urls import path
from .views import *

urlpatterns = [
    path('', login_view, name='login'),
    path('login/', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('home/', home_view, name='home'),
    path('register/', register_user, name='register'),
    path('record/<int:id>/', employee_record, name='record'),
    path('delete_record/<int:id>/', delete_record, name='delete'),
    path('update_record/<int:id>/', update_record, name='update'),
    path('addrecord/', add_record, name='add'),
    path('upload_csv/', upload_csv, name='upload_csv'),

]
