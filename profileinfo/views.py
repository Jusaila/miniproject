from django.shortcuts import render
from profileinfo.models import Profileinfo

# Create your views here.
def profileinfo(request):
    if request.method == "POST":
        obj=Profileinfo()
        obj.s_id='1'
        obj.student_name=request.POST.get('fullname')
        obj.student_phone=request.POST.get('phone')
        obj.parent_name=request.POST.get('parentname')
        obj.student_phone=request.POST.get('parentphone')
        obj.e_mail=request.POST.get('email')
        obj.stream=request.POST.get('Stream')
        obj.save()
    return render(request,'profileinfo/Profile Info.html')