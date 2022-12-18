
from django.urls import path
from Todolist import views

urlpatterns = [

    path('', views.TodO, name="TodO"),
    path('delete/<int:id>/',views.Delete, name="Delete"),
    path('edit/<int:id>/',views.Edit, name="Edit"),
    path('update/<int:id>',views.Update, name="Update")
        
]
