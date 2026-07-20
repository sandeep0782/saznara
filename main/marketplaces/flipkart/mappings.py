# FLIPKART COLOR MAPPING
FLIPKART_COLOR_MAPPING = {
"Mehendi": "Green",
"Yellow": "Yellow",
"Red": "Red",
"Green": "Green",
"Lavender": "Purple",
"Black": "Black",
"White": "White",
"Cream": "Cream",
"Blue": "Blue",
"Maroon": "Maroon",
"Orange": "Orange",
"Pink": "Pink",
"Peach": "Pink",
"Purple": "Purple",
"Teal": "Dark Green",

}


def get_flipkart_color(color_name):
    if not color_name:
        return None

    return FLIPKART_COLOR_MAPPING.get(
        color_name.strip()
    )


# FLIPKART TECHNIQUE MAPPING
FLIPKART_TECHNIQUE_MAPPING = {
    "bollywood": "Graphic",

}


def get_flipkart_technique(type):
    if not type:
        return None

    return FLIPKART_TECHNIQUE_MAPPING.get(
        type.strip()
    )


# FLIPKART OCCASION MAPPING
FLIPKART_OCCASION_MAPPING = {
    "party": "Party",
    "bridal_saree": "Wedding",

}


def get_flipkart_occasion(occasion):
    if not occasion:
        return None

    return FLIPKART_OCCASION_MAPPING.get(
        occasion.strip()
    )


# FLIPKART SAREE FABRIC
FLIPKART_SAREE_FABRIC_MAPPING = {
    "georgette": "Georgette",
    "simmer": "Polyester",
    "linen_blend": "Cotton Linen",


}


def get_flipkart_saree_fabric(saree_fabric):
    if not saree_fabric:
        return None

    return FLIPKART_SAREE_FABRIC_MAPPING.get(
        saree_fabric.strip()
    )


# FLIPKART BLOUSE FABRIC
FLIPKART_BLOUSE_FABRIC_MAPPING = {
    "linen_blend": "Cotton Linen Blend",
    "georgette": "Georgette",
    "chiffon": "Chiffon",

}


def get_flipkart_blouse_fabric(blouse_fabric):
    if not blouse_fabric:
        return None

    return FLIPKART_BLOUSE_FABRIC_MAPPING.get(
        blouse_fabric.strip()
    )


# FLIPKART BLOUSE
FLIPKART_BLOUSE_MAPPING = {
    "separate_blouse_piece": "Unstitched",

}


def get_flipkart_blouse(blouse):
    if not blouse:
        return None

    return FLIPKART_BLOUSE_MAPPING.get(
        blouse.strip()
    )


# FLIPKART PATTERN
FLIPKART_PATTERN_MAPPING = {
    "EMBROIDERED": "Embroidered",
    "SELF_DESIGN": "Self Design",
    "DIGITAL_PRINT": "Digital Print",
}


def get_flipkart_pattern(pattern):
    if not pattern:
        return None

    return FLIPKART_PATTERN_MAPPING.get(
        pattern.strip()
    )


# FLIPKART PRINT/PATTERN TYPE
FLIPKART_PRINT_OR_PATTERN_TYPE_MAPPING = {
    "floral": "Floral",
    "botanical": "Botanical Prints",
    "zari_butta": "Ethnic Motifs",
    "woven_design": "Woven Design",
    "solid": "Solid",

}


def get_flipkart_print_or_pattern_type(print_or_pattern_type):
    if not print_or_pattern_type:
        return None

    return FLIPKART_PRINT_OR_PATTERN_TYPE_MAPPING.get(
        print_or_pattern_type.strip()
    )


# FLIPKART ORNAMENTATION
FLIPKART_ORNAMENTATION = {
    "cutwork": "Lace",
    "tassels_latkans": "Tassel",
    "embroidered": "Resham/ Silk Thread",

}


def get_flipkart_ornamentation(ornamentation):
    if not ornamentation:
        return None

    return FLIPKART_ORNAMENTATION.get(
        ornamentation.strip()
    )


# FLIPKART BORDER
FLIPKART_BORDER = {
"printed": "Printed",
"embroidered": "Embroidered",
}


def get_flipkart_border(border):
    if not border:
        return None

    return FLIPKART_BORDER.get(
        border.strip()
    )