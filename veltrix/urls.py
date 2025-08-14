from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import MyPasswordChangeView, MyPasswordSetView
from django.conf.urls.static import static
from django.conf import settings
from veltrix import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Dashboards View
    path('', views.Dashboard, name='dashboard'),
    path('acesso/', include("acesso.urls")),

    path(
        "account/password/change/",
        login_required(MyPasswordChangeView.as_view()), name="account_change_password", ),
    path(
        "account/password/set/",
        login_required(MyPasswordSetView.as_view()), name="account_set_password", ),

    # auth-allath
    path('account/', include('allauth.urls')),

    # Urls dos modulos criados
    path('produtos/', include('modulos.produto.urls')),
    path('categorias/', include('modulos.categoria.urls')),
    path('ficha-tecnica/', include('modulos.ficha_tecnica.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
