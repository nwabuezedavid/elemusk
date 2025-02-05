from app.views import *

from django.urls import path
urlpatterns = [
    path("",home, name="home"),
    path("about/",about, name="about"),
    path("policy/",policy, name="policy"),
    path("contact/",contact, name="contact"),
    path("login/",loginuser, name="loginuser"),
    path("register/",register, name="register"),
    path("register/<pk>/",registerx, name="registerx"),
    path("forgot/",forgot, name="forgot"),
    path("verify/",verify, name="verify"),
    path("logoutuser/",logoutuser, name="logoutuser"),
    path("verified/<pk>/",verified, name="verified"),
    
    
    # Authendpoint
    path("registerApi/",registerApi, name="registerApi"),
    path("registerApi/<pk>/",registerApix, name="registerApix"),
    path("loginApi/",loginApi, name="loginApi"),
    path("passwordApi/",passwordApi, name="passwordApi"),
    path("profileapi/<pk>/",profileapi, name="profileapi"),
    
    # dashboard
    path("dashboard/<pk>/",dashboard, name="dashboard"),
    path("invest/<pk>/",invest, name="invest"),
    path("coininvest/<pk>/",coininvest, name="coininvest"),
    path("fund/<pk>/",coinpayment, name="coinpayment"),
    path("investment_details/<pk>/",investment_details, name="investment_details"),
    path("withdrwal/<pk>/",withdrwalx, name="withdrwal"),
    path("ihistory/<pk>/",ihistory, name="ihistory"),
    path("coinhistory/<pk>/",coinhistory, name="coinhistory"),
    path("referralpage/<pk>/",referralpage, name="referralpage"),
    path("whistory/<pk>/",whistory, name="whistory"),
    path("dhistory/<pk>/",dhistory, name="dhistory"),
    path("payment/<pk>/",payment, name="payment"),
    path("support/<pk>/",support, name="support"),
    path("profile/<pk>/",profile, name="profile"),
    path("changepassword/<pk>/",changepassword, name="changepassword"),
    path("transfer/<pk>/",transfer, name="transfer"),
    path("transferedlgs/<pk>/",transferedlgs, name="transferedlgs"),
    
]