from django.urls import path, include

# include api urls of each app here
urlpatterns = [
    path('core/', include('apps.core.api.v1.urls')),
    path('careers/', include('apps.careers.api.v1.urls')),
]
