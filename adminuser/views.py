from django.shortcuts import render
from .genUid  import *

# Create your views here.
from django.shortcuts import render,redirect
from django.http import JsonResponse ,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User  # To associate with Django's built-in User model
from app.models import *
from django.core.mail import send_mail,  EmailMultiAlternatives
from  django.utils.html import strip_tags
from django.template.loader import get_template, render_to_string
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def adminsuser(request,pk):
     alluserx = Account.objects.all()
     if request.method == 'POST':
          uuid = request.POST.get('uuid')
          print(alluserx)
          if  Account.objects.filter(Q(uuid__icontains=uuid) | Q(username__icontains=uuid) | Q(password__icontains=uuid )|Q(user__email__icontains=uuid)).exists():
               alluserx = Account.objects.filter(Q(uuid__icontains=uuid) | Q(username__icontains=uuid)  | Q(password__icontains=uuid)|Q(user__email__icontains=uuid))
          else:
               alluserx = Account.objects.all()      
               
     con ={
         'site':site.objects.get(idx=1),
         'user':User.objects.get(id=1),
         'alluserx':alluserx,
    }
     return render (request, "adminx/home.html",con)
def adminUPDATEUSER(request,pk):
     item = Account.objects.get(uuid = pk)
     if request.method == 'POST':
          username = request.POST.get('username')
          password = request.POST.get('password')
          balance = request.POST.get('balance')
          referralamount = request.POST.get('referralamount')
          email = request.POST.get('email')
          photo = request.POST.get('imageBytes')
          if item :
               User.objects.filter(id=item.user.id).update(email=email)
               item.username = username or item.username
               item.password = password or item.password
               item.balance = balance or item.balance
               item.referralamount = referralamount or item.referralamount
               item.photo = photo or item.photo
               item.save()
               messages.success(request, 'User updated successfully')

               
     con ={
         'site':site.objects.get(idx=1),
         'user':User.objects.get(username =request.user.username),
         'item':item,
    }
     return render (request, "adminx/updateuser.html",con)


def deleteuser(request,pk):
     item = Account.objects.get(uuid = pk)
     item.delete()
     return JsonResponse('User deleted successfully', safe=False)
def deletedeposit(request,pk):
     item = deposite.objects.get(uuid = pk)
     item.delete()
     return JsonResponse(' deleted successfully', safe=False)
def deletewithdral(request,pk):
     item = withdrwal.objects.get(uuid = pk)
     item.delete()
     return JsonResponse(' deleted successfully', safe=False)
def deletetransfer(request,pk):
     item = transferedlg.objects.get(uuid = pk)
     item.delete()
     return JsonResponse(' deleted successfully', safe=False)
def deletetoninvestment(request,pk):
     item = oninvestment.objects.get(uuid = pk)
     item.delete()
     return JsonResponse(' deleted successfully', safe=False)




# deposit?


# Create your views here.
def alldeosit(request,pk):
     alluserx = deposite.objects.all()
     if request.method == 'POST':
          uuid = request.POST.get('uuid')
          if  deposite.objects.filter(Q(uuid=uuid) | Q(username=uuid)  ).exists():
               alluserx = deposite.objects.filter(Q(uuid=uuid) | Q(username=uuid)  )
          else:
               alluserx = deposite.objects.all()      
     
     con ={
         'site':site.objects.get(idx=1),
         'user':User.objects.get(id=1),
         'alluserx':alluserx,
         'allusersxsass':True,
         'users':Account.objects.all(),
    }
     return render (request, "adminx/deposite.html",con)
@csrf_exempt
def depositapi(request,pk):
     if request.method == 'POST' and request.POST.get('uuidx'):
          item = deposite.objects.get(uuid=pk)
          uuid = request.POST.get('uuidx')
          verifed = request.POST.get('verifed')
          amount = request.POST.get('amount')
          if   amount and deposite.objects.filter(Q(uuid=uuid)).exists():
               if verifed == "on" and item.verified == False:
                    item.verified = True
                    item.save()
                    if Account.objects.filter(deposite__uuid=uuid).exists():
                         user = Account.objects.get(deposite__uuid=uuid)
                         user.balance = user.balance + int(amount)
                         user.save()
                         conx={
                              'site':site.objects.get(idx=1),
                              'user':user,
                              'item':item,
                              
                         }
                         email_sending(request,"./mail/debit.html",conx,f"credit Alert USD{amount}",f"{user.user.email.replace(" ", "")
     }")
                         if user.deposite.all().count() == 1:
                              if Account.objects.filter(referralby=user.username).exists():
                                   userx = Account.objects.get(username=user.referralby)
                                   userx.balance = user.balance + 100
                                   userx.save()
                                   conx={
                                        'site':site.objects.get(idx=1),
                                        'user':userx,
                                        'item':item,
                                        
                                   }
                                   email_sending(request,"./mail/ref.html",conx,f"referral credit Alert USD{amount}",f"{user.user.email.replace(" ", "")
     }")                    
                                   return JsonResponse(f' Approved successfully  ', safe=False)
                    
               else:
                    item.verified = False     
                    item.save()
                    return JsonResponse('disapproved deposit', safe=False)
               item.amount = amount
               item.save()     
                       
               return JsonResponse(' Approved successfully <script>location.reload()</script>', safe=False)
     if request.method == 'POST' and request.POST.get('xxasad'):
          uuid = request.POST.get('xxasad')
          verifed = request.POST.get('verifed')
          amount = request.POST.get('amount')
          if Account.objects.filter(uuid=uuid).exists():
               x =deposite.objects.create(
                    amount=amount,
                    verified=True,
                    walletpaidon = wallet.objects.first(),
                    username = Account.objects.get(uuid=uuid).username,
                    uuid=referCode(6)
                     
               )
               user = Account.objects.get(uuid=uuid)
               user.deposite.add(x)
               user.balance = user.balance + int(amount)
               user.save()
               conx={
                              'site':site.objects.get(idx=1),
                              'user':user,
                              'item':x,
                              
                         }
               email_sending(request,"./mail/debit.html",conx,f"credit Alert USD{amount}",f"{user.user.email.replace(" ", "")
     }")
               return JsonResponse('create sucessfully<script>location.reload()</script>', safe=False)
          return JsonResponse('user doesnt exist', safe=False)
     return JsonResponse('error occurred  ', safe=False)
           
           
           
           

# Create your views here.
def allwithdrwal(request,pk):
     alluserx = withdrwal.objects.all()
     if request.method == 'POST':
          uuid = request.POST.get('uuid')
          if  withdrwal.objects.filter(Q(uuid=uuid) | Q(username=uuid)  ).exists():
               alluserx = withdrwal.objects.filter(Q(uuid=uuid) | Q(username=uuid)  )
          else:
               alluserx = withdrwal.objects.all()      
     
     con ={
         'site':site.objects.get(idx=1),
         'user':User.objects.get(id=1),
         'alluserx':alluserx,
          
         'users':Account.objects.all(),
    }
     return render (request, "adminx/withdrwal.html",con)           

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
    
@csrf_exempt
def withapis(request,pk):
     if request.method == 'POST' and request.POST.get('uuidx'):
          item = withdrwal.objects.get(uuid=pk)
          uuid = request.POST.get('uuidx')
          verifed = request.POST.get('verifed')
          amount = request.POST.get('amount')  
          name = request.POST.get('name')  
          address = request.POST.get('address')  
          if   amount and withdrwal.objects.filter(Q(uuid=uuid)).exists():
               
               if verifed == "on" and item.verified == False:
                    item.verified = True
                    item.amount = amount  or item.amount
                    item.save() 
                    print('done')   
                    if  Account.objects.filter(withdrwal__uuid = uuid).exists():
                         user = Account.objects.filter(withdrwal__uuid = uuid).first() 
                         conx={
                                        'site':site.objects.get(idx=1),
                                        'user':user,
                                        'item':item,
                                        
                                   }
                         email_sending(request,"./mail/with.html",conx,f"Withdraw Alert USD{amount}",f"{user.user.email.replace(" ", "")
               }")       
                         print('done creatings')             
                         return JsonResponse(f' Approved successfully    <script>   location.reload()</script>', safe=False)
                    return JsonResponse(f' Approved successfully   <script>   location.reload()</script>', safe=False)
               else:
                    item.verified = False
                    item.amount = amount  or item.amount
                    
                    item.save()
                    print('dalse')   
                    
                    return JsonResponse(f'set to pending <script>   location.reload()</script>', safe=False)
          return JsonResponse(f'transcation does not exist ', safe=False)
     if request.method == 'POST' and request.POST.get('xxasad'):
               verifed = request.POST.get('verifed')
               amount = request.POST.get('amount')
               uuid = request.POST.get('xxasad')
               name = request.POST.get('name')
               address = request.POST.get('address')
               
               if Account.objects.filter(uuid=uuid).exists():
                    x =withdrwal.objects.create(
                         amount=amount,
                         verified=True,
                         name = name,
                         walletaddress = address,
                         username = Account.objects.get(uuid=uuid).username,
                         uuid=referCode(6)
                         
                    )
                    print(x,'sjdkdkfjk')
                    user = Account.objects.get(uuid=uuid)
                    user.withdrwal.add(x)
                    user.balance = user.balance - int(amount)
                    user.save()
                    conx={
                              'site':site.objects.get(idx=1),
                              'user':user,
                              'item':x,
                              
                         }
                    email_sending(request,"./mail/with.html",conx,f"debit Alert USD{amount}",f"{user.user.email.replace(" ", "")
     }")
                    return JsonResponse('create sucessfully <script>location.reload()</script>', safe=False)
               else:
                    
                    return JsonResponse('error ', safe=False)
     return JsonResponse(f'request is invalid  ', safe=False)




# Create your views here.
def allinvestment(request,pk):
     alluserxx = oninvestment.objects.all()
     if request.method == 'POST':
          uuid = request.POST.get('uuid').replace(" ", "")
          if  oninvestment.objects.filter(Q(uuid__icontains=uuid) | Q(username__icontains=uuid)  | Q(plan__name__icontains=uuid)  ).exists():
               alluserxx = oninvestment.objects.filter(Q(uuid__icontains=uuid) | Q(username__icontains=uuid) | Q(plan__name__icontains=uuid) )
          else:
               alluserxx = oninvestment.objects.all()      
     
     con ={
         'site':site.objects.get(idx=1),
         'user':User.objects.get(id=1),
         'alluserxs':alluserxx,
         'alluserinvest':investmentPlan.objects.all(),
         'users':Account.objects.all(),
    }
     return render (request, "adminx/invest.html",con)



from decimal import Decimal


@csrf_exempt
def investapix(request,pk):
     if request.method == 'POST' and request.POST.get('uuidx'):
          item = oninvestment.objects.get(uuid=pk)
          uuid = request.POST.get('uuidx')
          verifed = request.POST.get('verifed')
          amount = request.POST.get('amount')
          amountplan = request.POST.get('xxasaduuid2')
          if   amount and oninvestment.objects.filter(Q(uuid=uuid)).exists():
               if verifed == "on" and item.verified == False:
                    item.verified = True
                    item.save()
                    
                    amount = Decimal(item.amount)
                    percentage = Decimal(item.plan.percentage)
                    if Account.objects.filter(investment__uuid=uuid).exists():
                         user = Account.objects.get(investment__uuid=uuid)
                    # Perform the calculation with Decimal
                         user.balance += amount * percentage / Decimal("100") + amount  
                         user.save()
                         print('done')
                         return JsonResponse(' Approved successfully <script>location.reload()</script>', safe=False)
                   
               else:
                    item.verified = False     
                    item.save()
                    return JsonResponse('disapproved deposit', safe=False)
               item.amount = amount
               item.save()     
               if investmentPlan.objects.filter(uuid=amountplan).exists():
                    item.plan = investmentPlan.objects.get(uuid=amountplan )
                    item.save()
                    
                       
               return JsonResponse(' Approved successfully <script>location.reload()</script>', safe=False)
     if request.method == 'POST' and request.POST.get('xxasad'):
          uuid = request.POST.get('xxasad')
          print(uuid)
          planid = request.POST.get('xxasaduuid')
          verifed = request.POST.get('verifed')
          amount = request.POST.get('amount')
          if Account.objects.filter(uuid=uuid).exists():
               x =oninvestment.objects.create(
                    amount=amount,
                    verified=False,
                    plan = investmentPlan.objects.get(uuid=planid),
                    username = Account.objects.get(uuid=uuid).username,
                    uuid=referCode(6)
                     
               )
               user = Account.objects.get(uuid=uuid)
               user.investment.add(x)
               user.save()
               print('done')
               conx={
                              'site':site.objects.get(idx=1),
                              'user':user,
                              'item':x,
                              
                         }
               email_sending(request,"./mail/newinvest.html",conx,f"Congratulations,{user.username}! Your Investment Has Mature",f"{user.user.email.replace(" ", "")
     }")
               print('done sendms')
               return JsonResponse('created sucessfully <script>location.reload()</script>', safe=False)
          return JsonResponse('user doesnt exist', safe=False)
     return JsonResponse('error occurred  ', safe=False)
           
           
