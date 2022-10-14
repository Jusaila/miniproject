from django.shortcuts import render
from register.models import Register
# Create your views here.
def register(request):
    if request.method == 'POST':
        obj=Register()
        obj.s_id='1'
        obj.username=request.POST.get('username')
        obj.password=request.POST.get('password')
        obj.phone=request.POST.get('phone')
        obj.e_mail=request.POST.get('email')
        obj.gender=request.POST.get('gender')
        obj.save()

    return render(request,'register/Register.html')