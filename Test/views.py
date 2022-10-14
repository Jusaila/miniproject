from django.shortcuts import render
from Test.models import Test
# Create your views here.
def ptest(request):
    if request.method=='POST':
        ob = Test()
        ob.questions=request.POST.get('questions')
