from main.marketplaces.nykaa.blouse import NYKAA_ALLOWED_BLOUSE
from main.marketplaces.nykaa.color import NYKAA_ALLOWED_COLORS
from main.marketplaces.nykaa.occasion import NYKAA_ALLOWED_OCCASION
from main.marketplaces.nykaa.pattern import NYKAA_ALLOWED_PATTERN
from main.marketplaces.nykaa.print_pattern import NYKAA_ALLOWED_PRINT_OR_PATTERN_TYPE
from main.marketplaces.nykaa.saree_fabric import NYKAA_ALLOWED_SAREE_FABRIC
from main.marketplaces.nykaa.technique import NYKAA_ALLOWED_TECHNIQUE
from main.marketplaces.validator import validate_marketplace_mapping


def validate_nykaa_template(sku_list):

    errors = {}

    validations = [
        (
            "Color",
            "COLOR",
            lambda sku: sku.color.color if sku.color else None,
            NYKAA_ALLOWED_COLORS,
        ),
        (
            "Print or Pattern Type",
            "PRINT_OR_PATTERN_TYPE",
            lambda sku: (
                sku.get_print_or_pattern_type_display()
                if sku.print_or_pattern_type
                else None
            ),
            NYKAA_ALLOWED_PRINT_OR_PATTERN_TYPE,
        ),
        (
            "Blouse Color",
            "COLOR",
            lambda sku: sku.get_blouse_color_display() if sku.blouse_color else None,
            NYKAA_ALLOWED_COLORS,
        ),
        (
            "Saree Fabric",
            "SAREE_FABRIC",
            lambda sku: sku.get_saree_fabric_display() if sku.saree_fabric else None,
            NYKAA_ALLOWED_SAREE_FABRIC,
        ),
        (
            "Blouse",
            "BLOUSE",
            lambda sku: sku.get_blouse_display() if sku.blouse else None,
            NYKAA_ALLOWED_BLOUSE,
        ),
        (
            "Pattern",
            "PATTERN",
            lambda sku: sku.get_pattern_display() if sku.pattern else None,
            NYKAA_ALLOWED_PATTERN,
        ),
        (
            "Occasion",
            "OCCASION",
            lambda sku: sku.get_occasion_display() if sku.occasion else None,
            NYKAA_ALLOWED_OCCASION,
        ),
        (
            "Type",
            "TECHNIQUE",
            lambda sku: sku.get_type_display() if sku.type else None,
            NYKAA_ALLOWED_TECHNIQUE,
        ),
        (
            "Type",
            "TECHNIQUE",
            lambda sku: sku.get_type_display() if sku.type else None,
            NYKAA_ALLOWED_TECHNIQUE,
        ),
    ]

    for field_name, attribute, getter, allowed_values in validations:
        field_errors = validate_marketplace_mapping(
            sku_list,
            "NYKAA",
            attribute,
            field_name,
            getter,
            allowed_values,
        )

        if field_errors:
            errors[field_name] = field_errors

    return errors
