from .views import *

from django.urls import path
urlpatterns = [
    path("home/<pk>/",adminsuser, name="adminsuser"),
    path("adminUPDATEUSER/<pk>/",adminUPDATEUSER, name="adminUPDATEUSER"),
    path("deposit/<pk>/",alldeosit, name="alldeosit"),
    path("withdrwal/<pk>/",allwithdrwal, name="allwithdrwal"),
    path("allinvestment/<pk>/",allinvestment, name="allinvestment"),
    
    
    
    # Api
    path("deleteuser/<pk>/",deleteuser, name="deleteuser"),
    path("deletedeposit/<pk>/",deletedeposit, name="deletedeposit"),
    path("investapix/<pk>/",investapix, name="investapix"),
    path("depositapi/<pk>/",depositapi, name="depositapi"),
    path("withapis/<pk>/",withapis, name="withapis"),
    path("deletewithdral/<pk>/",deletewithdral, name="deletewithdral"),
    path("deletetoninvestment/<pk>/",deletetoninvestment, name="deletetoninvestment"),
]