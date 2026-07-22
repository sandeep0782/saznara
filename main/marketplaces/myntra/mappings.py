MYNTRA_COLOR_MAPPING = {
    # Direct matches
    "Black": "Black",
    "Blue": "Blue",
    "Brown": "Brown",
    "Cream": "Cream",
    "Gold": "Gold",
    "Mehendi":"Olive",
    "Red":"Red",
    "Teal":"Teal",
    "Peach":"Peach",
    "Lavender":"Lavender",
    "Yellow":"Yellow",
    "Purple":"Purple",
    "Green":"Green",
    "White":"White",
    "Maroon":"Maroon",
    "Orange":"Orange",
    "Pink":"Pink"
}

def get_myntra_color(color_name):
    if not color_name:
        return None

    return MYNTRA_COLOR_MAPPING.get(
        color_name.strip()
    )

# MYNTRA TECHNIQUE
MYNTRA_TECHNIQUE_MAPPING = {
    # Direct matches
   "bollywood":"NA",
   "assam_silk":"NA",
   "bagh":"Bagh",
   "balaton_silk":"NA",
   "baluchari":"Baluchari",
   "banarasi":"Banarasi",
   "bandhani":"Bandhani",
   "bangalori_silk":"NA",
   "begumpuri":"NA",
   "belt_saree":"NA",
   "bhagalpuri":"Bhagalpuri",
   "bishnupuri":"NA",
   "bomkai_sonepuri":"Bomkai silk",
   "brasso":"NA",
   "cape_saree":"NA",
   "chanderi":"Chanderi",
   "chettinad":"Chettinad",
   "chikankari":"NA",
   "christian_bride":"NA",
   "cowdial_sarees":"NA",
}

def get_myntra_technique(type):
    if not type:
        return None

    return MYNTRA_TECHNIQUE_MAPPING.get(
        type.strip()
    )

# MYNTRA OCCATION
MYNTRA_OCCASION_MAPPING = {
    # Direct matches
    "party_and_festive": "Party",
    "party":"Party",
    "celebrity_inspired":"Party",
    "bridal_saree":"Traditional",
    "wedding":"Traditional",
    "daily":"Daily",
    "farewell":"Party",
    "traditional":"Traditional"
}


def get_myntra_occasion(occasion):
    if not occasion:
        return None

    return MYNTRA_OCCASION_MAPPING.get(
        occasion.strip()
    )



# MYNTRA SAREE FABRIC
MYNTRA_SAREE_FABRIC_MAPPING = {
    # Direct matches
    "georgette": "Poly Georgette",
    "simmer": "Polyester",
    "linen_blend": "Linen Blend",
}


def get_myntra_saree_fabric(saree_fabric):
    if not saree_fabric:
        return None

    return MYNTRA_SAREE_FABRIC_MAPPING.get(
        saree_fabric.strip()
    )
# MYNTRA BLOUSE FABRIC
MYNTRA_BLOUSE_FABRIC_MAPPING = {
    # Direct matches
    "georgette":"Poly Georgette",
    "linen_blend":"Linen Blend",
    "chiffon":"Poly Chiffon",

}


def get_myntra_blouse_fabric(blouse_fabric):
    if not blouse_fabric:
        return None

    return MYNTRA_BLOUSE_FABRIC_MAPPING.get(
        blouse_fabric.strip()
    )



# MYNTRA BLOUSE 
MYNTRA_BLOUSE_MAPPING = {
    # Direct matches
    "separate_blouse_piece":"Blouse Piece",
    "saree_with_multiple_blouse":"Blouse Piece",
    "running_blouse":"Blouse Piece",
    "without_blouse":"NA",
    "stitched_blouse":"Stitched Blouse",
    "semi_stitched_blouse": "Blouse Piece"
}


def get_myntra_blouse(blouse):
    if not blouse:
        return None

    return MYNTRA_BLOUSE_MAPPING.get(
        blouse.strip()
    )

# MYNTRA PATTERN 
MYNTRA_PATTERN_MAPPING = {
    # Direct matches
   "SELF_DESIGN": "Woven Design",
   "EMBROIDERED": "Embroidered",
   "DIGITAL_PRINT": "Printed"
}


def get_myntra_pattern(pattern):
    if not pattern:
        return None

    return MYNTRA_PATTERN_MAPPING.get(
        pattern.strip()
    )
# MYNTRA PRINT_OR_PATTERN_TYPE_MAPPING
MYNTRA_PRINT_OR_PATTERN_TYPE_MAPPING = {
    # Direct matches
    "solid":"Solid",
    "zari_butta": "Ethnic Motifs",
    "woven_design": "Woven Design",
    "botanical": "Floral",
    "floral": "Floral",
}


def get_myntra_print_or_pattern_type(print_or_pattern_type):
    if not print_or_pattern_type:
        return None

    return MYNTRA_PRINT_OR_PATTERN_TYPE_MAPPING.get(
        print_or_pattern_type.strip()
    )
# MYNTRA ORNAMENTATION 
MYNTRA_ORNAMENTATION = {
    # Direct matches
    "cutwork": "Jaali",
    "embroidered": "Embroidered",
    "tassels_latkans": "NA"

}


def get_myntra_ornamentation(ornamentation):
    if not ornamentation:
        return None

    return MYNTRA_ORNAMENTATION.get(
        ornamentation.strip()
    )


# MYNTRA BORDER 
MYNTRA_BORDER = {
    # Direct matches
    "embroidered": "Embroidered",
    "printed": "Printed",

}


def get_myntra_border(border):
    if not border:
        return None

    return MYNTRA_BORDER.get(
        border.strip()
    )