from django.shortcuts import render

# Create your views here.
def winner(request):
    return render(request,'winner.html')
