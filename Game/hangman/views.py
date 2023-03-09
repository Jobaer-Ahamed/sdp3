from django.shortcuts import render

# Create your views here.

def hangManGame(request):
    return render(request,"hangman/index.html")