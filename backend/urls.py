from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from backend.views import user,screenlist

router = routers.DefaultRouter()
router.register(r'users', user.UserViewSet)
router.register(r'screenlist', screenlist.ScreenlistViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='api-auth')),
    path('screenlist/', include('rest_framework.urls', namespace='screenlist'))
]