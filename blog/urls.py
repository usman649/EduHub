from django.urls import path
from config.urls import schema_view
from .views import register_view,login_view,me_view

urlpatterns = [
    path("register/",register_view),
    path("login/",login_view),
    path("me/",me_view),


    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


]