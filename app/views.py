from django.shortcuts import render,redirect
from django.http import JsonResponse ,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User  # To associate with Django's built-in User model
from .models import *
from django.core.mail import send_mail,  EmailMultiAlternatives
from  django.utils.html import strip_tags
from django.template.loader import get_template, render_to_string
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    con ={
         'site':site.objects.get(idx=1),
    }
    return render (request, "home/home.html",con)
def about(request):
    con ={
         'site':site.objects.get(idx=1),
    }
    return render (request, "home/about.html",con)
def policy(request):
    con ={
         'site':site.objects.get(idx=1),
    }
    return render (request, "home/policy.html",con)
def contact(request):
    ee = False
    con ={
         'site':site.objects.get(idx=1),
        "ee":ee
    }
    return render (request, "home/contact.html",con)

 
 
 
#  Auth


def loginuser(request):
    ee = False
    con ={
         'site':site.objects.get(idx=1),
        "ee":ee
    }
    return render (request, "auth/login.html",con)

def register(request):
    ee = False
    
    con ={
         'site':site.objects.get(idx=1),
        "iale":ee
    }
    return render (request, "auth/register.html",con)
def registerx(request,pk):
    user=None
    if Account.objects.filter(code=pk).exists():
        user = Account.objects.get(code=pk)
         
    ee = False
    con ={
         'site':site.objects.get(idx=1),
        "iale":ee,
        "user":user,
    }
    return render (request, "auth/register1.html",con)

def forgot(request):
    ee = False
    con ={
         'site':site.objects.get(idx=1),
        "ee":ee
    }
    return render (request, "auth/forgot.html",con)
def verify(request):
    ee = False
    con ={
         'site':site.objects.get(idx=1),
        "ee":ee
    }
    return render (request, "auth/verify.html",con)
def verified(request, pk):
    ee = False
    try:
        us = Account.objects.get(uuid=pk)
        authenticate(username=us.username, password=us.password)
        us.approved=True    
        us.save()
        print(us.approved)
    except:
        print('us.approved')
        pass
    finally:
        print('us.approveds')
        pass
    con ={
         'site':site.objects.get(idx=1),
        "ee":ee
    }
    return render (request, "auth/verified.html",con)


from .genUid  import *


# Authendpoint

def passwordApi(request):
    if request.method == "POST":
        username = request.POST['username']
        if Account.objects.filter(username=username, ).exists():
            sx = Account.objects.get(username=username )
            conx = {
                        'site':site.objects.get(idx=1),
                        'user':sx,
                        'token':f'{site.objects.get(idx=1).host}/verified/{sx.uuid}'
                    }
            email_sending(request,"./mail/password.html",conx,f"Account verification",f"{sx.user.email.replace(" ", "")}")
            return JsonResponse("an email has been  sent you  ", safe=False)
        else:
            return JsonResponse("user doesnt exist ", safe=False)


def loginApi(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        sitex=site.objects.get(idx=1),
        if Account.objects.filter(username=username, password=password).exists():
            print(username, 'password')
            sx = Account.objects.get(username=username, password=password)
            authenticate(username=username, password=password)
            login(request, sx.user)
            if not sx.approved:
                
                conx = {
                        'site':site.objects.get(idx=1),
                        'user':sx,
                        'token':f'{site.objects.get(idx=1).host}/verified/{sx.uuid}'
                    }
                email_sending(request,"./mail/verify.html",conx,f"Account verification",f"{sx.user.email.replace(" ", "")
}")
                print(username, "sending mail")
                return JsonResponse("an email was send to account , verify by clicking the link", safe=False)
            else:
                response = HttpResponse()
                if sx.user.is_superuser:
                    response["HX-Redirect"] = f"/adminx/home/{sx.uuid}/"
                    return response
                response["HX-Redirect"] = f"/dashboard/{sx.uuid}/"
                return response
        else:    
            return JsonResponse("user does not exist", safe=False)
            
                    
def profileapi(request,pk):
    userc = Account.objects.get(uuid=pk)
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        country = request.POST['country']
        photo = request.POST['imageBytes1']
        city = request.POST['city']
        zip = request.POST['zip']
        state = request.POST['state']
        if username and email and phone and country and photo and city and zip and state:
            d =  Account.objects.filter(uuid=pk).update(username=username, city=city or None,  photo=photo or None, phone=phone or None, country=country or None, zip=zip or None, state=state or None)
            User.objects.filter(username=username).update(email=email,username=username)
            return JsonResponse("profile updated", safe=False)
        return JsonResponse("error", safe=False)

        
def registerApi(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        email = request.POST['email']
        Code = request.POST['Code']
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists() or User.objects.filter(username=username, email=email).exists():
            return JsonResponse("Username and email already Taken", safe=False)
        else:
            if password1 == password:
                s= User.objects.create(username=username, email=email, password=password)
                sx= Account.objects.create(username=username,uuid =referCode(12) ,code= referCode(6),user=s, password=password)
                s.save()
                conx = {
                        'site':site.objects.get(idx=1),
                        'user':sx,
                        'token':f'{site.objects.get(idx=1).host}/verified/{sx.uuid}'

                    }
                email_sending(request,"./mail/verify.html",conx,f"Accout verified",f"{sx.user.email.replace(" ", "")
}")
                print(s)
                if Account.objects.filter(code=Code).exists():
                    c = referral.objects.create(user=s)
                    parent = Account.objects.get(code=Code)
                    parent.referral.add(c)
                    sx.referralby = parent.username
                    sx.save()
                    parent.save()
                   
                    print(parent)
                    if parent.username:
                        response = HttpResponse()
                        response["HX-Redirect"] = "/verify/"
                        return response

                elif Code and not Account.objects.filter(code=Code).exists():
                    return JsonResponse("referral Code doest exist", safe=False)
                elif s.username:
                    response = HttpResponse()
                    response["HX-Redirect"] = "/verify/"
                    return response
                return JsonResponse({'data':s})
            else:
                
                return JsonResponse("password does'nt match", safe=False)
    return JsonResponse({'error': 'method is invalid'}, status=400)


def registerApix(request,pk):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        email = request.POST['email']
        Code = request.POST['Code'] 
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists() or User.objects.filter(username=username, email=email).exists():
            return JsonResponse("Username and email already Taken", safe=False)
        else:
            if password1 == password:
                s= User.objects.create(username=username, email=email, password=password)
                sx= Account.objects.create(username=username,uuid =referCode(12) ,code= referCode(6),user=s, password=password)
                s.save()
                authenticate(username=username, password=password)
                conx = {
                        'site':site.objects.get(idx=1),
                        'user':sx,
                        'token':f'{site.objects.get(idx=1).host}/verified/{sx.uuid}'

                    }
                email_sending(request,"./mail/verify.html",conx,f"Accout verified",f"{sx.user.email.replace(" ", "")
}")
                print(s)
                if Account.objects.filter(code=Code).exists():
                    c = referral.objects.create(user=s)
                    parent = Account.objects.get(code=Code)
                    parent.referral.add(c)
                    sx.referralby = parent.username
                    sx.save()
                    parent.save()
                   
                    print(parent)
                    if parent.username:
                        response = HttpResponse()
                        response["HX-Redirect"] = "/verify/"
                        return response

                elif Code and not Account.objects.filter(code=Code).exists():
                    return JsonResponse("referral Code doest exist", safe=False)
                elif s.username:
                    response = HttpResponse()
                    response["HX-Redirect"] = "/verify/"
                    return response
                return JsonResponse({'data':s})
            else:
                
                return JsonResponse("password does'nt match", safe=False)
    return JsonResponse({'error': 'method is invalid'}, status=400)



# emil?


def email_sending(request,tempname,context,subjects,to):
    tos = render_to_string(tempname,context=context )
    tags =strip_tags(tos)
    mas = EmailMultiAlternatives(
        subject = subjects,
        body=tags,
        from_email = settings.EMAIL_HOST_USER,
        to=[to]
    )
    mas.attach_alternative(tos, 'text/html')
    mas.send()
    
    
    
    
    
    
def dashboard(request, pk):
    user =Account.objects.get(uuid=pk)
    checjkinvest(request, pk)
    ee = False
    con ={
        'user':user,
         'site':site.objects.get(idx=1),
        "ee":ee
    }
    return render (request, "user/dasboard.html",con)    
    
    
def invest(request, pk):
    user =Account.objects.get(uuid=pk)
    if request.method =="POST":
        amount = request.POST['amount']
        uuid = request.POST['uuid']
        if investmentPlan.objects.filter(uuid=uuid).exists()  :
            plan = investmentPlan.objects.get(uuid=uuid)
            if user.balance <= int(amount)  and user.balance >= 50: 
                if  int(amount) >= int(plan.min) and int(amount) <= int(plan.max):
                    w = oninvestment.objects.create(uuid=referCode(7),plan=plan, amount=amount, username=user.username )
                    user.investment.add(w)
                    w.save()
                    messages.info(request, "invesment has started counting ")  
                    return redirect('ihistory', pk=user.uuid)
                else:
                    messages.info(request, f"amount should be greater than USD{plan.min} and less that USD{plan.max} ")  
                    
            else:
                messages.info(request, f"insufficent balance")  
        else:
            messages.info(request, f"plan does not exist")  
            
    ee = False
    con ={
        'user':user,
         'site':site.objects.get(idx=1),
        "ee":ee
    }
    return render (request, "user/invest.html",con)    
    
def coinpayment(request, pk):
    user =Account.objects.get(uuid=pk)
    ee = False
    if request.method =="POST":
        amount = request.POST['amount']
        uuid = request.POST['uuid']
        if amount and uuid and int(amount) > 10:
            w = wallet.objects.get(uuid=uuid)
            s = deposite.objects.create(uuid=referCode(12),amount=amount, username=user.username,walletpaidon=w )
            s.save()
            user.deposite.add(s)
            messages.info(request, "deposit on process")
            return redirect('payment', pk=s.uuid)
        else:
            messages.info(request, "Amount is too low  ")
                
    con ={
        'user':user,
         'site':site.objects.get(idx=1),
        "ee":ee
    }
    return render (request, "user/coinpayment.html",con)    
    
def withdrwalx(request, pk):
    user =Account.objects.get(uuid=pk)
    ee = False
    if request.method =="POST":
        amount = request.POST['amount']
        method = request.POST['method']
        walletaddress = request.POST['walletaddress']
        if int(amount) > 0 and method and walletaddress and int(amount) <=int(user.balance):
            s = withdrwal.objects.create(uuid=referCode(12),amount=amount, walletaddress=walletaddress,username=user.username, name=method )
            user.balance -=int(amount)
            s.save()
            user.save()
            user.withdrwal.add(s)
            messages.info(request, "withdrawal on process ")
            return redirect('whistory', pk=user.uuid)
        else:
            messages.info(request, "Insufficent Fund deposite and try again")
                
    con ={
        'user':user,
         'site':site.objects.get(idx=1),
        "ee":ee
    }
    return render (request, "user/withdraw.html",con)    
def transferedlgs(request, pk):
    user =Account.objects.get(uuid=pk)
    ee = False
    con ={
        'user':user,
         'site':site.objects.get(idx=1),
        "ee":ee
    }
    return render (request, "user/thistory.html",con)    
def whistory(request, pk):
    user =Account.objects.get(uuid=pk)
    item =None
    if request.method == "POST":
        id = request.POST['id']
        if withdrwal.objects.filter(uuid=id).exists():
            item = withdrwal.objects.filter(uuid=id)
    ee = False
    con ={
        'user':user,
         'site':site.objects.get(idx=1),
        "item":item
    }
    return render (request, "user/whistory.html",con)    
def ihistory(request, pk):
    user =Account.objects.get(uuid=pk)
    item =None
    if request.method == "POST":
        id = request.POST['id']
        if oninvestment.objects.filter(uuid=id).exists():
            item = oninvestment.objects.filter(uuid=id)
    ee = False
    con ={
        'user':user,
         'site':site.objects.get(idx=1),
        "item":item
    }
    return render (request, "user/ihistory.html",con)    
def dhistory(request, pk):
    user =Account.objects.get(uuid=pk)
    ee = False
    
    con ={
        'user':user,
         'site':site.objects.get(idx=1),
        "ee":ee
    }
    return render (request, "user/dhistory.html",con)    
def payment(request, pk):
    user =Account.objects.get(user=request.user)
    item =deposite.objects.get(uuid=pk)
    ee = False
    con ={
        'user':user,
         'site':site.objects.get(idx=1),
        "item":item
    }
    return render (request, "user/paymentdetail.html",con)    
def support(request, pk):
    user =Account.objects.get(uuid=pk)
    ee = False
    con ={
        'user':user,
         'site':site.objects.get(idx=1),
        "ee":ee
    }
    return render (request, "user/support.html",con)    
def profile(request, pk):
    user =Account.objects.get(uuid=pk)
    ee = False
    con ={
        'user':user,
         'site':site.objects.get(idx=1),
        "ee":ee
    }
    return render (request, "user/profile.html",con)    
def referralpage(request, pk):
    user =Account.objects.get(uuid=pk)
    ee = False
    con ={
        'user':user,
         'site':site.objects.get(idx=1),
        "ee":ee
    }
    return render (request, "user/referral.html",con)    
def changepassword(request, pk):
    user =Account.objects.get(uuid=pk)
    if request.method =="POST":
        password = request.POST['password']
        newpassword = request.POST['newpassword']
        newpassword2 = request.POST['newpassword2']
        if user.password == password and newpassword == newpassword2:
            user.password = newpassword
            user.save()
            messages.info(request, "password changed")
        else:
            messages.info(request, "password does not match or incorrect password")    
    ee = False
    con ={
        'user':user,
         'site':site.objects.get(idx=1),
        "ee":ee
    }
    return render (request, "user/changepassword.html",con)    
def transfer(request, pk):
    user =Account.objects.get(uuid=pk)
    if request.method =="POST":
        email = request.POST['email']
        amount = request.POST['amount']
        if Account.objects.filter(user__email=email).exists() and email != user.user.email:
          c = Account.objects.get(user__email=email)
          if user.balance >= int(amount) and user.balance >= 50:
             user.balance -= int(amount)
             ss =deposite.objects.create(uuid=referCode(9), email=email,amount=amount)
             user.balance-=int(amount)
             user.deposite.add(ss)
             user.save()
             messages.error(request, f"An amount of {int(amount)} is pending approval for {c.username}'s account.")
             return redirect
          else:
              messages.error(request, "Insufficent Balance")
        else:
            messages.error(request, "user does not exist")
        
    
    
    ee = False
    con ={
        'user':user,
         'site':site.objects.get(idx=1),
        "ee":ee
    }
    return render (request, "user/transfer.html",con)    

from django.utils.timezone import now
from datetime import timedelta
from decimal import Decimal
def checjkinvest(request, pk):
    if Account.objects.filter(uuid=pk).exists:
        user = Account.objects.get(uuid=pk)
        if user.investment.filter(verified=False).exists():
            active_investments = user.investment.filter(verified=False)
            print('reuningjsdjhsd',active_investments)
            expired_investments = []
            print('reuning')
            # Iterate through investments to check if they have reached the target date
            for investment in active_investments:
                # Calculate the target date (start date + plan duration)
                target_date = investment.date + timedelta(days=investment.plan.days)
                 

                # Check if the current date is beyond or equal to the target date
                if now() >= target_date:
                    expired_investments.append(investment)
                    # Optionally, update the investment to mark it as verified
                    investment.verified = True
                    amount = Decimal(investment.amount)
                    percentage = Decimal(investment.plan.percentage)

                    # Perform the calculation with Decimal
                    user.balance += amount * percentage / Decimal("100") + amount  
                    investment.save()
                    user.save()
                    conx={
                              'site':site.objects.get(idx=1),
                              'user':user,
                              'item':investment,
                              "profit":amount * percentage / Decimal("100") + amount  
                              
                         }
                    email_sending(request,"./mail/takeprofite.html",conx,f"Congratulations,{user.username}! Your Investment Has Matured",f"{user.user.email.replace(" ", "")
     }")
            
def logoutuser(request):
    logout(request)
    return redirect('loginuser')            
            
def investment_details(request, pk):
    user = Account.objects.get(uuid=pk)
    
    """
    Fetch user investments and calculate remaining time for each investment.
    """
    # Fetch investments for the logged-in user (modify as needed for specific user)
    investments = oninvestment.objects.filter(username=request.user.username, verified=False)
    
    investments_with_remaining_time = []
    for investment in investments:
        # Calculate the target date (start date + plan duration)
        target_date = investment.date + timedelta(days=investment.plan.days)
        remaining_time = target_date - now()

        investments_with_remaining_time.append({
            'investment': investment,
            'remaining_time': remaining_time,
            'remaining_days': remaining_time.days
        })
    con ={
        'user':user,
         'site':site.objects.get(idx=1),
       "investments_with_remaining_time": investments_with_remaining_time
    }
    return render(request, "user/detail.html", con)            