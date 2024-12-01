from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin route
    path('admin/', admin.site.urls),
    
    # Include routes from the 'api' app
    path('api/', include('api.urls')),

    # Token authentication route
    path('api-token-auth/', include('rest_framework.authtoken')),
]
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns += [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]