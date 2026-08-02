from main.marketplaces.meesho.blouse_pattern import MEESHO_ALLOWED_BLOUSE_PATTERN
from main.marketplaces.meesho.pallu_details import MEESHO_ALLOWED_PALLU_DETAILS
from main.marketplaces.validator import validate_marketplace_mapping

from .blouse import MEESHO_ALLOWED_BLOUSE
from .blouse_fabric import (
    MEESHO_ALLOWED_BLOUSE_FABRIC,
)
from .border import MEESHO_ALLOWED_BORDER
from .color import MEESHO_ALLOWED_COLORS
from .occasion import MEESHO_ALLOWED_OCCASION
from .ornamentation import MEESHO_ALLOWED_ORNAMENTATION
from .pattern import MEESHO_ALLOWED_PATTERN
from .print_pattern import MEESHO_ALLOWED_PRINT_OR_PATTERN_TYPE
from .saree_fabric import MEESHO_ALLOWED_SAREE_FABRIC
from .technique import MEESHO_ALLOWED_TECHNIQUE


def validate_meesho_template(sku_list):

    errors = {}

    validations = [
        (
            "Color",
            "COLOR",
            lambda sku: sku.color.color if sku.color else None,
            MEESHO_ALLOWED_COLORS,
        ),
        (
            "Blouse Color",
            "COLOR",
            lambda sku: sku.get_blouse_color_display() if sku.blouse_color else None,
            MEESHO_ALLOWED_COLORS,
        ),
        (
            "Border",
            "BORDER",
            lambda sku: sku.get_border_display() if sku.border else None,
            MEESHO_ALLOWED_BORDER,
        ),
        (
            "Saree Fabric",
            "SAREE_FABRIC",
            lambda sku: sku.get_saree_fabric_display() if sku.saree_fabric else None,
            MEESHO_ALLOWED_SAREE_FABRIC,
        ),
        (
            "Blouse Fabric",
            "BLOUSE_FABRIC",
            lambda sku: sku.get_blouse_fabric_display() if sku.blouse_fabric else None,
            MEESHO_ALLOWED_BLOUSE_FABRIC,
        ),
        (
            "Blouse",
            "BLOUSE",
            lambda sku: sku.get_blouse_display() if sku.blouse else None,
            MEESHO_ALLOWED_BLOUSE,
        ),
        (
            "Blouse Pattern",
            "BLOUSE_PATTERN",
            lambda sku: (
                sku.get_blouse_pattern_display() if sku.blouse_pattern else None
            ),
            MEESHO_ALLOWED_BLOUSE_PATTERN,
        ),
        (
            "Pattern",
            "PATTERN",
            lambda sku: sku.get_pattern_display() if sku.pattern else None,
            MEESHO_ALLOWED_PATTERN,
        ),
        (
            "Print Or Pattern Type",
            "PRINT_OR_PATTERN_TYPE",
            lambda sku: (
                sku.get_print_or_pattern_type_display()
                if sku.print_or_pattern_type
                else None
            ),
            MEESHO_ALLOWED_PRINT_OR_PATTERN_TYPE,
        ),
        (
            "Ornamentation",
            "ORNAMENTATION",
            lambda sku: sku.get_ornamentation_display() if sku.ornamentation else None,
            MEESHO_ALLOWED_ORNAMENTATION,
        ),
        (
            "Occasion",
            "OCCASION",
            lambda sku: sku.get_occasion_display() if sku.occasion else None,
            MEESHO_ALLOWED_OCCASION,
        ),
        (
            "Type",
            "TECHNIQUE",
            lambda sku: sku.get_type_display() if sku.type else None,
            MEESHO_ALLOWED_TECHNIQUE,
        ),
        (
            "Pallu_details",
            "PALLU_DETAILS",
            lambda sku: sku.get_pallu_details_display() if sku.pallu_details else None,
            MEESHO_ALLOWED_PALLU_DETAILS,
        ),
    ]

    for field_name, attribute, getter, allowed_values in validations:
        field_errors = validate_marketplace_mapping(
            sku_list,
            "MEESHO",
            attribute,
            field_name,
            getter,
            allowed_values,
        )

        if field_errors:
            errors[field_name] = field_errors

    return errors
