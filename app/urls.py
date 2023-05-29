from django.urls import include, path
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Nicasource Challenge",
        default_version='v1',
        description="Builded by Emerson Guedes",
        contact=openapi.Contact(email="guedes.emerson@hotmail.com"),
        license=openapi.License(name="Todos os direitos reservados: Emerson Guedes de Oliveira"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("v1/movie/", include("movie.urls", namespace='api-movie')),
    path("v1/user/", include("user.urls", namespace='api-user')),
    path("v1/rating/", include("rating.urls", namespace='api-rating')),
    path("admin/", admin.site.urls),
    path("", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]