from django.db import models
from django.db import models
import uuid
# Create your models here.
from django.db import models
from django.contrib.auth.models import User  # To associate with Django's built-in User model
from django.utils import timezone
# Create your models here.

class referral(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date =  models.DateTimeField(auto_now_add=True,blank=True, null =False)
    reward_given = models.BooleanField(default=False)
    reward_amount = models.CharField(max_length=40000,  blank=True, null=True)

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    investment = models.ManyToManyField("oninvestment", blank=True)
    # Link to Django's user authentication system
    uuid = models.CharField(max_length=40,  blank=True, null=True)
    code = models.CharField(max_length=40,  blank=True, null=True)
    country = models.CharField(max_length=40,  blank=True, null=True)
    phone = models.CharField(max_length=15,  blank=True, null=True)
    referralby = models.CharField(max_length=15,  blank=True, null=True)
    zip = models.CharField(max_length=40 ,blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    balance = models.DecimalField(max_digits=12, default=0, decimal_places=2)
    deposite = models.ManyToManyField("deposite", blank=True)
    withdrwal = models.ManyToManyField("withdrwal", blank=True)
    referral = models.ManyToManyField("referral", blank=True)
    referralamount = models.DecimalField(max_digits=12, default=0, decimal_places=2)
    transferedlg = models.ManyToManyField("transferedlg", blank=True)
    approved = models.BooleanField(default=False)
    canInvest = models.BooleanField(default=True)
    username = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=40,blank=True, null=True)
    
    def __str__(self):  
        return f'client {str(self.username)}'
    
    def getfrer(self):
        ws = self.withdrwal.all()
       
         
        return total
    
    def totalwithdrwal(self):
        ws = self.withdrwal.all()
        total = 0   
        for i in ws:
            total += i.amount  
        return total
    def totaldeposit(self):
        ws = self.deposite.all()
        total = 0   
        for i in ws:
            total += i.amount  
        print('dhdj', total)
        return str(total)
    def totalinvestment(self):
        ws = self.investment.all()
        total = 0   
        for i in ws:
            total += i.amount  
        return total
    def totalpendinginvestment(self):
        ws = self.investment.filter(verified=False)
        total = 0   
        for i in ws:
            total += i.amount  
        return total
    def totalpendingwith(self):
        ws = self.withdrwal.filter(verified=False)
        total = 0   
        for i in ws:
            total += i.amount  
        return total
    def lastinvest(self):
        ws = self.investment.last()
         
        return ws or 0
    # pending?
    def pendinginvest(self):
        ws = self.investment.filter(verified=False).last()
        return ws.amount or 0
    def pendingdeposite(self):
        ws = self.deposite.filter(verified=False).last()
        return ws.amount or None
    def pendingwithdrwal(self):
        ws = self.withdrwal.filter(verified=False).last()
        return ws   
    def getwallet(self):
        ws = wallet.objects.filter(verified=True)
        return ws or None
    def plan(self):
        ws = investmentPlan.objects.all()
        return ws or None
 
    
class investmentPlan(models.Model):
    uuid = models.CharField(max_length=3000, blank=True , null=False)
    name = models.CharField(max_length=3000, blank=True , null=False)
    min = models.CharField(max_length=300000,  blank=True , null=False)
    max = models.CharField(max_length=300000,  blank=True , null=False)
    forday = models.CharField(max_length=300000,  blank=True , null=False)
    percentage = models.CharField(max_length=300000,  blank=True , null=False)
    days = models.IntegerField(blank=True)    
    def __str__(self):  
        return f'investment plan: {str(self.name)}'
   
class transferedlg(models.Model):
    uuid = models.CharField(max_length=3000, blank=True , null=False)
    email = models.CharField(max_length=4000,blank=True)
    amount = models.IntegerField( blank=True, null=True)
    tyx = models.CharField(max_length=4000, default="credit", blank=True, null=True)
    verified = models.BooleanField(default=False)
    
    def __str__(self):  
        return f'on invetment, Plan:{self.plan.name} {str(self.username)}'
class oninvestment(models.Model):
    uuid = models.CharField(max_length=3000, blank=True , null=False)
    plan = models.ForeignKey(investmentPlan, on_delete=models.CASCADE)
    date =  models.DateTimeField(auto_now_add=True,blank=True, null =False)
    username = models.CharField(max_length=4000,blank=True)
    amount = models.IntegerField( blank=True, null=True)
    verified = models.BooleanField(default=False)
    
    def __str__(self):  
        return f'on invetment, Plan:{self.plan.name} {str(self.username)}'
class wallet(models.Model):
    uuid = models.CharField(max_length=3000, blank=True , null=False)
    name = models.CharField(max_length=3000, blank=True , null=False)
    address = models.CharField(max_length=300000, blank=True , null=False)
    image = models.TextField( blank=True , null=False)
    verified = models.BooleanField(default=False)
    def __str__(self):  
        return f'wallet {str(self.name)}'
class deposite(models.Model):
    uuid = models.CharField(max_length=3000, blank=True , null=False)
    username = models.CharField(max_length=3000, blank=True , null=False)
    date = models.DateTimeField(auto_now_add=True, blank=True , null=False)
    amount = models.IntegerField(max_length=3000, blank=True , null=False)
    walletpaidon = models.ForeignKey(wallet, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)
    def __str__(self):  
        return f'deposit {str(self.username)}, {self.amount}'
class withdrwal(models.Model):
    uuid = models.CharField(max_length=3000, blank=True , null=False)
    username = models.CharField(max_length=3000, blank=True , null=False)
    walletaddress = models.CharField(max_length=3000, blank=True , null=False)
    name = models.CharField(max_length=3000, blank=True , null=False)
    date = models.DateTimeField(auto_now_add=True, blank=True , null=False)
    amount = models.IntegerField(  blank=True , null=False)
    verified = models.BooleanField(default=False)
    def __str__(self):  
        return f'with {str(self.username)}, {self.amount}'
class site(models.Model):
    idx = models.CharField(max_length=3000, default=1, blank=True , null=False)
    name = models.CharField(max_length=3000, blank=True , null=False)
    email = models.CharField(max_length=3000,default='nwabuezedavid333@gmail.com', blank=True , null=False)
    logo = models.TextField(  blank=True , null=False)
    country = models.CharField(max_length=3000, blank=True , null=False)
    host = models.CharField(max_length=3000,default='http://127.0.0.1:8000', blank=True , null=False)
    dis = models.CharField(max_length=3000, blank=True , null=False)
    keyword = models.CharField(max_length=3000, blank=True , null=False)
    date = models.DateTimeField(auto_now_add=True, blank=True , null=False)
    interest = models.IntegerField(  blank=True , null=False)
    def __str__(self):  
        return f'client {str(self.name)},'