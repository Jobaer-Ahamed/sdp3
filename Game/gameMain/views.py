from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from gameMain.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@ login_required
def index(request):
    if request.method == "GET":
        return render(request,"gameMain/gameindex.html")
    
    elif request.method == "POST":
        roomCode = request.POST.get("room_code", None)
        playerName = request.POST.get("player_name", "Unknown Player")
        print(roomCode)
        if(roomCode):
            try:
                gameroom= createNewRoom.objects.get(id=roomCode)
                return redirect(f"gameMain/{roomCode}/{playerName}/")
            
            except createNewRoom.DoesNotExist:
                messages.error(request,"There is no room exist!")
                return redirect(f"/")
                
        else:
            newRoom = createNewRoom.objects.create()
            return redirect(f"gameMain/{newRoom.id}/{playerName}/")

            
    else:
        return render(request,"gameMain/gameindex.html")
@ login_required
def gameroom(request, id=None, name=None):
    try:
        gameroom= createNewRoom.objects.get(id=id)
        return render(request,"gameMain/gamepage.html",{
            'room':gameroom,
            'name':name
        }) 
    except createNewRoom.DoesNotExist:
            messages.error(request,"There is no room exist!!!!")
            return redirect(f"/")    