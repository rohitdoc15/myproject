from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import *
from .serializers import ItemSerializer,ChannelSerializer,TitleSerializer
from datetime import datetime

@api_view(['GET'])
def getData(request):
    title = Title.objects.all()
    serializer = TitleSerializer(title, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = ChannelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getChannel(request):
    channel = Channel.objects.all()
    serializer = ChannelSerializer(channel, many=True)
    return Response(serializer.data)

@api_view(['GET'])
# get titles of specific channel
def getTitles(request,channel):
    channel = Channel.objects.get(name=channel)
    title = Title.objects.filter(channel=channel)
    serializer = TitleSerializer(title, many=True)
    return Response(serializer.data)
@api_view(['GET'])
# get titles of specific channel of today's date
def getTitlesDate(request,channel,date):
    date = datetime.strptime(date, '%Y-%m-%d').date()
    channel = Channel.objects.get(name=channel)
    title = Title.objects.filter(channel=channel,date=date)
    serializer = TitleSerializer(title, many=True)
    return Response(serializer.data)

@api_view(['GET'])
# get titles of specific channel of date range
def getTitlesDateRange(request,channel,start_date,end_date):
    start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
    end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
    channel = Channel.objects.get(name=channel)
    title = Title.objects.filter(channel=channel,date__range=[start_date,end_date])
    serializer = TitleSerializer(title, many=True)
    return Response(serializer.data)
