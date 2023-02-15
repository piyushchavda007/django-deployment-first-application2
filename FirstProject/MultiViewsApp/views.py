from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def f1(request):
    return HttpResponse("<center> <h2> Good Morning Django User..! Have a Nice Day..</h2> <hr/></center>")
    
def f2(request):
    return HttpResponse("<h2> Good Afternoon Django User..! Hope you are doing good..</h2> <hr/>")
    
def f3(request):
    return HttpResponse("<h2> Good Evening Django User..! How was ur day..</h2> <hr/>")

