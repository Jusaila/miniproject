from django.shortcuts import render
from courses.models import Courses
# Create your views here.
def view(request):
    obj = Courses.objects.all()
    context = {
        'x': obj
    }
    return render(request,'courses/course-view.html')


def post(request):
    if request.method == "POST":
        obj=Courses()
        obj.c_id='1'
        obj.courses=request.POST.get("courses")
        obj.college=request.POST.get("collegename")
        obj.save()
    return render(request,'courses/courses-post.html')