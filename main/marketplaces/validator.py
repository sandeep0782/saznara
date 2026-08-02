from main.models import MarketplaceMapping


def validate_marketplace_mapping(
    sku_list,
    marketplace,
    attribute,
    field_name,
    getter,
    allowed_values=None,
):
    errors = []

    for sku in sku_list:
        source_value = getter(sku)

        # Missing value validation
        if not source_value or not str(source_value).strip():
            errors.append(f"{field_name}: Missing value for SKU '{sku.sku}'")
            continue

        source_value = source_value.strip()

        # print("DEBUG LOOKUP:")
        # print("Marketplace:", repr(marketplace))
        # print("Attribute:", repr(attribute))
        # print("Source Value:", repr(source_value))

        mapped_value = (
            MarketplaceMapping.objects.filter(
                marketplace=marketplace,
                attribute=attribute,
                source_value__iexact=source_value,
                is_active=True,
            )
            .values_list("mapped_value", flat=True)
            .first()
        )
        print("Mapped Value Found:", repr(mapped_value))

        # Missing mapping
        if not mapped_value:
            errors.append(
                f"{field_name}: '{source_value}' - Missing {marketplace} mapping"
            )
            continue

        # Invalid marketplace value
        if allowed_values and mapped_value not in allowed_values:
            errors.append(
                f"{field_name}: '{source_value}' → '{mapped_value}' - Invalid {marketplace} value"
            )
        

    return list(set(errors))


