from django.contrib import admin

from .models import Payment

admin.site.site_header = "Раздел администратора"


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass
