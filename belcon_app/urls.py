from django.urls import path     
from . import views
from belcon import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('create_profile', views.create_profile),
    path('show', views.show),
    path('success', views.success),
    path('view/<int:id>', views.view),
    path('delete/<int:id>', views.delete),
    path('login_page', views.login_page),
    path('login', views.login),
    path('register_page', views.register_page),
    path('register', views.register),
    path('logout', views.logout)
]


# if settings.DEBUG: 
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)