
from django.urls import path
from message_app import views
urlpatterns = [
    #path('',views.home),
    path('about',views.about),
    path('create',views.create),
    path('',views.dashboard),
    path('delete/<rid>',views.delete),
    path('edit/<rid>',views.edit)
]
