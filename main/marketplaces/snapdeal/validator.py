from main.marketplaces.snapdeal.blouse import SNAPDEAL_ALLOWED_BLOUSE
from main.marketplaces.snapdeal.blouse_fabric import SNAPDEAL_ALLOWED_BLOUSE_FABRIC
from main.marketplaces.snapdeal.blouse_pattern import SNAPDEAL_ALLOWED_BLOUSE_PATTERN
from main.marketplaces.snapdeal.border import SNAPDEAL_ALLOWED_BORDER
from main.marketplaces.snapdeal.border_length import SNAPDEAL_ALLOWED_BORDER_LENGTH
from main.marketplaces.snapdeal.color import SNAPDEAL_ALLOWED_COLORS
from main.marketplaces.snapdeal.occasion import SNAPDEAL_ALLOWED_OCCASION
from main.marketplaces.snapdeal.ornamentation import SNAPDEAL_ALLOWED_ORNAMENTATION
from main.marketplaces.snapdeal.pattern import SNAPDEAL_ALLOWED_PATTERN
from main.marketplaces.snapdeal.print_pattern import (
    SNAPDEAL_ALLOWED_PRINT_OR_PATTERN_TYPE,
)
from main.marketplaces.snapdeal.saree_fabric import SNAPDEAL_ALLOWED_SAREE_FABRIC
from main.marketplaces.snapdeal.technique import SNAPDEAL_ALLOWED_TECHNIQUE
from main.marketplaces.validator import validate_marketplace_mapping


def validate_snapdeal_template(sku_list):

    errors = {}

    validations = [
        (
            "Color",
            "COLOR",
            lambda sku: sku.color.color if sku.color else None,
            SNAPDEAL_ALLOWED_COLORS,
        ),
        (
            "Blouse Color",
            "COLOR",
            lambda sku: sku.get_blouse_color_display() if sku.blouse_color else None,
            SNAPDEAL_ALLOWED_COLORS,
        ),
        (
            "Border",
            "BORDER",
            lambda sku: sku.get_border_display() if sku.border else None,
            SNAPDEAL_ALLOWED_BORDER,
        ),
        (
            "Saree Fabric",
            "SAREE_FABRIC",
            lambda sku: sku.get_saree_fabric_display() if sku.saree_fabric else None,
            SNAPDEAL_ALLOWED_SAREE_FABRIC,
        ),
        (
            "Blouse Fabric",
            "BLOUSE_FABRIC",
            lambda sku: sku.get_blouse_fabric_display() if sku.blouse_fabric else None,
            SNAPDEAL_ALLOWED_BLOUSE_FABRIC,
        ),
        (
            "Blouse",
            "BLOUSE",
            lambda sku: sku.get_blouse_display() if sku.blouse else None,
            SNAPDEAL_ALLOWED_BLOUSE,
        ),
        (
            "Blouse Pattern",
            "BLOUSE_PATTERN",
            lambda sku: (
                sku.get_blouse_pattern_display() if sku.blouse_pattern else None
            ),
            SNAPDEAL_ALLOWED_BLOUSE_PATTERN,
        ),
        (
            "Pattern",
            "PATTERN",
            lambda sku: sku.get_pattern_display() if sku.pattern else None,
            SNAPDEAL_ALLOWED_PATTERN,
        ),
        (
            "Print Or Pattern Type",
            "PRINT_OR_PATTERN_TYPE",
            lambda sku: (
                sku.get_print_or_pattern_type_display()
                if sku.print_or_pattern_type
                else None
            ),
            SNAPDEAL_ALLOWED_PRINT_OR_PATTERN_TYPE,
        ),
        
        (
            "Occasion",
            "OCCASION",
            lambda sku: sku.get_occasion_display() if sku.occasion else None,
            SNAPDEAL_ALLOWED_OCCASION,
        ),
        (
            "Type",
            "TECHNIQUE",
            lambda sku: sku.get_type_display() if sku.type else None,
            SNAPDEAL_ALLOWED_TECHNIQUE,
        ),
        
    ]

    for field_name, attribute, getter, allowed_values in validations:
        field_errors = validate_marketplace_mapping(
            sku_list,
            "SNAPDEAL",
            attribute,
            field_name,
            getter,
            allowed_values,
        )

        if field_errors:
            errors[field_name] = field_errors

    return errors
