from sku.main.template.mappings import get_myntra_color


def validate_myntra_skus(sku_list):

    validation_errors = []

    for sku in sku_list:

        errors = []

        if not sku.color:
            errors.append(
                "Color is missing. Please ask admin to add the proper color name for Myntra template"
            )

        else:
            myntra_color = get_myntra_color(
                sku.color.color
            )

            if not myntra_color:
                errors.append(
                    f"Color '{sku.color.color}' is not supported by Myntra"
                )

        if errors:
            validation_errors.append({
                "sku": sku.sku,
                "errors": errors
            })

    return validation_errors