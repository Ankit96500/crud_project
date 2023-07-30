from django.urls import path
from enroll import views

urlpatterns = [
     path('<int:id>/',views.delete,name='deldata'),
     path('all/<int:upid>/',views.update,name='dataupdate'),
 ]
