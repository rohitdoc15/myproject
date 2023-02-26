from rest_framework import serializers
from base.models import Item,Channel,Title,tag

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        
class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'        
        
class TitleSerializer(serializers.ModelSerializer):
    channel = serializers.StringRelatedField()
    tags = serializers.StringRelatedField(many=True)
    date = serializers.DateField(format="%Y-%m-%d",input_formats=['%Y-%m-%d'])

    class Meta:
        model = Title
        fields = ('__all__')     
        
class tagSerializer(serializers.ModelSerializer):
    class Meta:
        model = tag
        fields = '__all__'                     