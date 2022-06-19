from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('main.urls', 'main'), namespace='main')),
    path('payment/', include(('payments.urls', 'payments'), namespace='payments')),
    path('reservations/', include(('reservations.urls', 'reservations'), namespace='reservations')),
    path('userinfo/', include(('userinfo.urls', 'userinfo'), namespace='userinfo')),
]
