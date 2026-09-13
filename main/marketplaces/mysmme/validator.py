from main.marketplaces.mysmme.blouse import MYSMME_ALLOWED_BLOUSE
from main.marketplaces.mysmme.blouse_fabric import MYSMME_ALLOWED_BLOUSE_FABRIC
from main.marketplaces.mysmme.border import MYSMME_ALLOWED_BORDER
from main.marketplaces.mysmme.border_length import MYSMME_ALLOWED_BORDER_LENGTH
from main.marketplaces.mysmme.color import MYSMME_ALLOWED_COLORS
from main.marketplaces.mysmme.occasion import MYSMME_ALLOWED_OCCASION
from main.marketplaces.mysmme.ornamentation import MYSMME_ALLOWED_ORNAMENTATION
from main.marketplaces.mysmme.pattern import MYSMME_ALLOWED_PATTERN
from main.marketplaces.mysmme.print_pattern import MYSMME_ALLOWED_PRINT_OR_PATTERN_TYPE
from main.marketplaces.mysmme.saree_fabric import MYSMME_ALLOWED_SAREE_FABRIC
from main.marketplaces.mysmme.technique import MYSMME_ALLOWED_TECHNIQUE
from main.marketplaces.validator import validate_marketplace_mapping


def validate_mysmme_template(sku_list):

    errors = {}

    validations = [
        (
            "Color",
            "COLOR",
            lambda sku: sku.color.color if sku.color else None,
            MYSMME_ALLOWED_COLORS,
        ),
        (
            "Blouse Color",
            "COLOR",
            lambda sku: sku.get_blouse_color_display() if sku.blouse_color else None,
            MYSMME_ALLOWED_COLORS,
        ),
        (
            "Border",
            "BORDER",
            lambda sku: sku.get_border_display() if sku.border else None,
            MYSMME_ALLOWED_BORDER,
        ),
        (
            "Saree Fabric",
            "SAREE_FABRIC",
            lambda sku: sku.get_saree_fabric_display() if sku.saree_fabric else None,
            MYSMME_ALLOWED_SAREE_FABRIC,
        ),
        (
            "Blouse Fabric",
            "BLOUSE_FABRIC",
            lambda sku: sku.get_blouse_fabric_display() if sku.blouse_fabric else None,
            MYSMME_ALLOWED_BLOUSE_FABRIC,
        ),
        (
            "Blouse",
            "BLOUSE",
            lambda sku: sku.get_blouse_display() if sku.blouse else None,
            MYSMME_ALLOWED_BLOUSE,
        ),
        # (
        #     "Blouse Pattern",
        #     "BLOUSE_PATTERN",
        #     lambda sku: (
        #         sku.get_blouse_pattern_display() if sku.blouse_pattern else None
        #     ),
        #     MYSMME_ALLOWED_BLOUSE_PATTERN,
        # ),
        (
            "Pattern",
            "PATTERN",
            lambda sku: sku.get_pattern_display() if sku.pattern else None,
            MYSMME_ALLOWED_PATTERN,
        ),
        (
            "Print Or Pattern Type",
            "PRINT_OR_PATTERN_TYPE",
            lambda sku: (
                sku.get_print_or_pattern_type_display()
                if sku.print_or_pattern_type
                else None
            ),
            MYSMME_ALLOWED_PRINT_OR_PATTERN_TYPE,
        ),
        (
            "Ornamentation",
            "ORNAMENTATION",
            lambda sku: sku.get_ornamentation_display() if sku.ornamentation else None,
            MYSMME_ALLOWED_ORNAMENTATION,
        ),
        (
            "Occasion",
            "OCCASION",
            lambda sku: sku.get_occasion_display() if sku.occasion else None,
            MYSMME_ALLOWED_OCCASION,
        ),
        (
            "Type",
            "TECHNIQUE",
            lambda sku: sku.get_type_display() if sku.type else None,
            MYSMME_ALLOWED_TECHNIQUE,
        ),
        (
            "Border Width",
            "BORDER_WIDTH",
            lambda sku: sku.get_border_width_display() if sku.border_width else None,
            MYSMME_ALLOWED_BORDER_LENGTH,
        ),
    ]

    for field_name, attribute, getter, allowed_values in validations:
        field_errors = validate_marketplace_mapping(
            sku_list,
            "MYSMME",
            attribute,
            field_name,
            getter,
            allowed_values,
        )

        if field_errors:
            errors[field_name] = field_errors

    return errors
