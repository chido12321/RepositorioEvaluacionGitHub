from django.shortcuts import render

# Create your views here.

def cosas(request):
   return render(request, "Casa/casa.html")
