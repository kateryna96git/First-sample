from backend.models.screenlist import Screenlist
from rest_framework import viewsets
# from rest_framework import permissions
from backend.serializers.screenlist import ScreenlistSerializer

class ScreenlistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Screenlist.objects.all()
    serializer_class = ScreenlistSerializer
    # permission_classes = [permissions.IsAuthenticated]