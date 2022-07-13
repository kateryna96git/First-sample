from backend.models.screenlist import Screenlist
from rest_framework import serializers


class ScreenlistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Screenlist
        fields = ['created', 'title']