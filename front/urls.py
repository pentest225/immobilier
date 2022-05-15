from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index,name="home"),
    path('about',views.about,name="about"),
    path('property',views.property,name="property"),
    #TODO : FIND THE WEY TO PARSE THE SLUG 
    path('property-single/<int:property_id>',views.property_single,name="property_single"),
    path('agent',views.agent,name="agent"),
    path('agent-single/<int:angent_id>',views.agent_single,name="agent_single"),
    path('contact',views.contact,name="contact"),
]