from main.marketplaces.myntra.blouse import MYNTRA_ALLOWED_BLOUSE
from main.marketplaces.myntra.blouse_fabric import MYNTRA_ALLOWED_BLOUSE_FABRIC
from main.marketplaces.myntra.blouse_pattern import MYNTRA_ALLOWED_BLOUSE_PATTERN
from main.marketplaces.myntra.border import MYNTRA_ALLOWED_BORDER
from main.marketplaces.myntra.border_length import MYNTRA_ALLOWED_BORDER_LENGTH
from main.marketplaces.myntra.color import MYNTRA_ALLOWED_COLORS
from main.marketplaces.myntra.occasion import MYNTRA_ALLOWED_OCCASION
from main.marketplaces.myntra.ornamentation import MYNTRA_ALLOWED_ORNAMENTATION
from main.marketplaces.myntra.pattern import MYNTRA_ALLOWED_PATTERN
from main.marketplaces.myntra.print_pattern import MYNTRA_ALLOWED_PRINT_OR_PATTERN_TYPE
from main.marketplaces.myntra.saree_fabric import MYNTRA_ALLOWED_SAREE_FABRIC
from main.marketplaces.myntra.technique import MYNTRA_ALLOWED_TECHNIQUE
from main.marketplaces.validator import validate_marketplace_mapping


def validate_myntra_template(sku_list):

    errors = {}

    validations = [
        (
            "Color",
            "COLOR",
            lambda sku: sku.color.color if sku.color else None,
            MYNTRA_ALLOWED_COLORS,
        ),
        (
            "Blouse Color",
            "COLOR",
            lambda sku: sku.get_blouse_color_display() if sku.blouse_color else None,
            MYNTRA_ALLOWED_COLORS,
        ),
        (
            "Border",
            "BORDER",
            lambda sku: sku.get_border_display() if sku.border else None,
            MYNTRA_ALLOWED_BORDER,
        ),
        (
            "Saree Fabric",
            "SAREE_FABRIC",
            lambda sku: sku.get_saree_fabric_display() if sku.saree_fabric else None,
            MYNTRA_ALLOWED_SAREE_FABRIC,
        ),
        (
            "Blouse Fabric",
            "BLOUSE_FABRIC",
            lambda sku: sku.get_blouse_fabric_display() if sku.blouse_fabric else None,
            MYNTRA_ALLOWED_BLOUSE_FABRIC,
        ),
        (
            "Blouse",
            "BLOUSE",
            lambda sku: sku.get_blouse_display() if sku.blouse else None,
            MYNTRA_ALLOWED_BLOUSE,
        ),
        # (
        #     "Blouse Pattern",
        #     "BLOUSE_PATTERN",
        #     lambda sku: (
        #         sku.get_blouse_pattern_display() if sku.blouse_pattern else None
        #     ),
        #     MYNTRA_ALLOWED_BLOUSE_PATTERN,
        # ),
        (
            "Pattern",
            "PATTERN",
            lambda sku: sku.get_pattern_display() if sku.pattern else None,
            MYNTRA_ALLOWED_PATTERN,
        ),
        (
            "Print Or Pattern Type",
            "PRINT_OR_PATTERN_TYPE",
            lambda sku: (
                sku.get_print_or_pattern_type_display()
                if sku.print_or_pattern_type
                else None
            ),
            MYNTRA_ALLOWED_PRINT_OR_PATTERN_TYPE,
        ),
        (
            "Ornamentation",
            "ORNAMENTATION",
            lambda sku: sku.get_ornamentation_display() if sku.ornamentation else None,
            MYNTRA_ALLOWED_ORNAMENTATION,
        ),
        (
            "Occasion",
            "OCCASION",
            lambda sku: sku.get_occasion_display() if sku.occasion else None,
            MYNTRA_ALLOWED_OCCASION,
        ),
        (
            "Type",
            "TECHNIQUE",
            lambda sku: sku.get_type_display() if sku.type else None,
            MYNTRA_ALLOWED_TECHNIQUE,
        ),
        # (
        #     "Border Width",
        #     "BORDER_WIDTH",
        #     lambda sku: sku.get_border_width_display() if sku.border_width else None,
        #     MYNTRA_ALLOWED_BORDER_LENGTH,
        # ),
    ]

    for field_name, attribute, getter, allowed_values in validations:
        field_errors = validate_marketplace_mapping(
            sku_list,
            "MYNTRA",
            attribute,
            field_name,
            getter,
            allowed_values,
        )

        if field_errors:
            errors[field_name] = field_errors

    return errors
