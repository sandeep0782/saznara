from typing import ClassVar

from django.contrib import admin

from main.models import SKU, VMS, Brand, Gender, MarketplaceMapping

admin.site.register(Brand)
admin.site.register(Gender)
admin.site.register(SKU)
admin.site.register(VMS)


@admin.register(MarketplaceMapping)
class MarketplaceMappingAdmin(admin.ModelAdmin):
    search_fields: ClassVar[list[str]] = [
        "marketplace",
        "attribute",
        "source_value",
        "mapped_value",
    ]

    list_display: ClassVar[list[str]] = [
        "marketplace",
        "attribute",
        "source_value",
        "mapped_value",
        "is_active",
        "created_at",
    ]

    list_filter: ClassVar[list[str]] = [
        "marketplace",
        "attribute",
        "is_active",
    ]
