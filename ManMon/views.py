from django.shortcuts import render
from django.http import HttpResponse
from .models import Account, TypeIncome, TypePayment
# Create your views here.

def callMainPage(request):
    account_list = Account.objects.order_by('-pub_date')

    #calulation the rest of money
    remain_money = 0
    for account in account_list :
        remain_money += account.money

    account_list = Account.objects.order_by('-pub_date')[:5]
    return render(request, 'ManMon/main.html',{'remain_money':remain_money,         
                  'account_list':account_list})
