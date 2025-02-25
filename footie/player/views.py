from rest_framework.response import Response

from rest_framework.decorators import api_view
from player.models import Player
from .serializers import PlayerSerializer
from auth.jwt import validate_jwt

@api_view(['GET'])
@validate_jwt
def getAllPlayer(request):
    players = Player.objects.all()
    serializer = PlayerSerializer(players, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createPlayer(request):
    serializer = PlayerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)