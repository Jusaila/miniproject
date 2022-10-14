from django.shortcuts import render
from college.models import College
# Create your views here.
def colg(request):
    if request.method == "POST":
        obj=College()
        obj.college_name=request.POST.get('collegename')
        obj.college_location=request.POST.get('collegelocation')
        obj.phone=request.POST.get('phone')
        obj.e_mail=request.POST.get('email')
        obj.departments=request.POST.get('departments')
        obj.save()
    return render(request,'college/college-post.html')


def viewclg(request):
    obj=College.objects.all()
    context={
        'x':obj
    }
    return render(request,'college/college_viewandupdates.html',context)