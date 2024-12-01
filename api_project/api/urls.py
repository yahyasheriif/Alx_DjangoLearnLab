from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import include, path
from api.views import BookViewSet
"DefaultRouter()", "router.urls"
# Initialize DefaultRouter
router = DefaultRouter()
router.register(r'books', BookViewSet)

# Define urlpatterns
urlpatterns = [
    path('api/', include(router.urls)),  # Includes all router-defined routes under 'api/'
    path('admin/', admin.site.urls),    # Admin site
]
