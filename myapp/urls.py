from django.urls import path
from myapp import views  # Add this line to import views from your application

urlpatterns = [
   
    path('profile/', views.profile, name='profile'),
    path('inbox/', views.inbox_view, name='inbox'),
    path('delete/<int:message_id>/', views.message_delete, name='delete_message'),
    path('reply/<int:message_id>/', views.message_reply, name='reply_message'),
]