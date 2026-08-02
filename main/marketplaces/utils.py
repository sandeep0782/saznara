from main.models import MarketplaceMapping


def get_marketplace_value(marketplace, attribute, value):

    if not value:
        return ""

    return (
        MarketplaceMapping.objects.filter(
            marketplace=marketplace,
            attribute=attribute,
            source_value__iexact=value.strip(),
            is_active=True,
        )
        .values_list("mapped_value", flat=True)
        .first()
        or ""
    )
