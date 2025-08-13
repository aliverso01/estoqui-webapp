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
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('acesso/', include("acesso.urls")),

    path(
        "account/password/change/",
        login_required(MyPasswordChangeView.as_view()), name="account_change_password", ),
    path(
        "account/password/set/",
        login_required(MyPasswordSetView.as_view()), name="account_set_password", ),

    # auth-allath
    path('account/', include('allauth.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
