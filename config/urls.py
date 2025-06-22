from django.contrib import admin
from django.template.context_processors import static
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings

import course

schema_view = get_schema_view(
    openapi.Info(
        title="Exam",
        default_version="v1",
        description="API for CRM system",
        terms_of_service="",
        contact = openapi.Contact(email="nurb8197@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("blog.urls")),
    path("",include("course.urls")),

]


urlpatterns += [
        re_path(
            r"^swagger(?P<format>\.json|\.yaml)$",
            schema_view.without_ui(cache_timeout=0),
            name="schema-json",
        ),
        re_path(
            r"^swagger/$",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        re_path(
            r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
        )
    ]
urlpatterns += static(settings.MEDIA_URL,serve, document_root=settings.MEDIA_ROOT)
