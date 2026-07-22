# SNAPDEAL COLOR MAPPING
SNAPDEAL_COLOR_MAPPING = {
    "Maroon": "Maroon",
    "Peach": "Peach",
    "Orange": "Orange",
    "Blue": "Blue",
    "Green": "Green",
    "Black": "Black",
    "Teal": "Teal",
    "Pink": "Pink",
    "White": "White",
    "Mehendi": "Green",
    "Yellow": "Yellow",
    "Lavender": "Lavender",
    "Red": "Red",
    "Cream": "Cream",
    "Purple": "Purple",
}


def get_snapdeal_color(color_name):
    if not color_name:
        return None
    return SNAPDEAL_COLOR_MAPPING.get(
        color_name.strip()
    )

SNAPDEAL_BLOUSE_COLOR_MAPPING = {
    "pink": "Pink",
    "yellow": "Yellow",
    "peach": "Peach",
    "purple": "Purple",
    "maroon": "Maroon",
    "mehendi": "Olive",
    "blue": "Blue",
}


def get_snapdeal_blouse_color(blouse_color_name):
    if not blouse_color_name:
        return None
    return SNAPDEAL_BLOUSE_COLOR_MAPPING.get(
        blouse_color_name.strip()
    )

# SNAPDEAL TECHNIQUE MAPPING
SNAPDEAL_TECHNIQUE_MAPPING = {
    "bollywood":"Regular Saree",
}

def get_snapdeal_technique(type):
    if not type:
        return None
    return SNAPDEAL_TECHNIQUE_MAPPING.get(
        type.strip()
    )

# SNAPDEAL SAREE FABRIC
SNAPDEAL_SAREE_FABRIC_MAPPING = {
"simmer": "Shimmer",
"georgette": "Georgette",
"linen_blend": "Linen",
}


def get_snapdeal_saree_fabric(saree_fabric):
    if not saree_fabric:
        return None
    return SNAPDEAL_SAREE_FABRIC_MAPPING.get(
        saree_fabric.strip()
    )

# SNAPDEAL BLOUSE FABRIC
SNAPDEAL_BLOUSE_FABRIC_MAPPING = {
"linen_blend": "Linen",
"georgette": "Georgette",
"chiffon": "Chiffon",
}

def get_snapdeal_blouse_fabric(blouse_fabric):
    if not blouse_fabric:
        return None
    return SNAPDEAL_BLOUSE_FABRIC_MAPPING.get(
        blouse_fabric.strip()
    )

# SNAPDEAL BLOUSE
SNAPDEAL_BLOUSE_MAPPING = {
"separate_blouse_piece": "With Unstitched Blouse Piece"
}

def get_snapdeal_blouse(blouse):
    if not blouse:
        return None
    return SNAPDEAL_BLOUSE_MAPPING.get(
        blouse.strip()
    )

# SNAPDEAL PATTERN
SNAPDEAL_PATTERN_MAPPING = {
"SELF_DESIGN": "Self Design",
"DIGITAL_PRINT": "Printed",
"EMBROIDERED": "Embroidered",
}

def get_snapdeal_pattern(pattern):
    if not pattern:
        return None
    return SNAPDEAL_PATTERN_MAPPING.get(
        pattern.strip()
    )


# SNAPDEAL BLOUSE PATTERN
SNAPDEAL_BLOUSE_PATTERN_MAPPING = {
"same_as_saree": "Self Design",
}

def get_snapdeal_blouse_pattern(blouse_pattern):
    if not blouse_pattern:
        return None
    return SNAPDEAL_BLOUSE_PATTERN_MAPPING.get(
        blouse_pattern.strip()
    )

# SNAPDEAL PRINT/PATTERN TYPE
SNAPDEAL_PRINT_OR_PATTERN_TYPE_MAPPING = {
    "solid": "Solid",
    "zari_butta": "Zari Work",
    "woven_design": "Buta",
    "floral": "Floral",
    "botanical": "Floral",
}

def get_snapdeal_print_or_pattern_type(print_or_pattern_type):
    if not print_or_pattern_type:
        return None
    return SNAPDEAL_PRINT_OR_PATTERN_TYPE_MAPPING.get(
        print_or_pattern_type.strip()
    )

# SNAPDEAL ORNAMENTATION
SNAPDEAL_ORNAMENTATION_MAPPING = {
}


def get_snapdeal_ornamentation(ornamentation):
    if not ornamentation:
        return None
    return SNAPDEAL_ORNAMENTATION_MAPPING.get(
        ornamentation.strip()
    )

# SNAPDEAL BORDER
SNAPDEAL_BORDER_MAPPING = {
"embroidered": "Embroidered",
"printed": "Printed",
}

def get_snapdeal_border(border):
    if not border:
        return None
    return SNAPDEAL_BORDER_MAPPING.get(
        border.strip()
    )