"""
ASGI config for tictactoe project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from django.urls import path 
from gameMain.consumers import *
from attrs import define

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tictactoe.settings")

application = get_asgi_application()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
     "websocket": URLRouter([
      
      path("ws/gameMain/<int:id>/",gameConsumer.as_asgi())

     ])
    
})