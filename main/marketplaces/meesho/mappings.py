MEESHO_COLOR_MAPPING = {
    "Aqua Blue": "Aqua Blue",
    "Baby Blue": "Baby Blue",
    "Beige": "Beige",
    "Black": "Black",
    "Blue": "Blue",
    "Bronze": "Bronze",
    "Brown": "Brown",
    "Copper": "Copper",
    "Coral": "Coral",
    "Cream": "Cream",
    "Dark Pink": "Dark Pink",
    "Gajari": "Gajari",
    "Gold": "Gold",
    "Green": "Green",
    "Grey": "Grey",
    "Grey Melange": "Grey Melange",
    "Indigo": "Indigo",
    "Khaki": "Khaki",
    "Lavender": "Lavender",
    "Lemon Yellow": "Lemon Yellow",
    "Maroon": "Maroon",
    "Mehendi": "Mehendi",
    "Metallic": "Metallic",
    "Mint Green": "Mint Green",
    "Multicolor": "Multicolor",
    "Mustard": "Mustard",
    "Navy Blue": "Navy Blue",
    "Nude": "Nude",
    "Olive": "Olive",
    "Orange": "Orange",
    "Pastel Blue": "Pastel Blue",
    "Pastel Brown": "Pastel Brown",
    "Pastel Orange": "Pastel Orange",
    "Pastel Pink": "Pastel Pink",
    "Pastel Red": "Pastel Red",
    "Pastel Yellow": "Pastel Yellow",
    "Peach": "Peach",
    "Pink": "Pink",
    "Purple": "Purple",
    "Rama": "Rama",
    "Rani": "Rani",
    "Red": "Red",
    "Rust": "Rust",
    "Sage": "Sage",
    "Silver": "Silver",
    "Sky Blue": "Sky Blue",
    "Teal": "Teal",
    "Tricolor": "Tricolor",
    "Turquoise": "Turquoise",
    "White": "White",
    "Yellow": "Yellow",
}

def get_meesho_color(color_name):
    if not color_name:
        return None

    return MEESHO_COLOR_MAPPING.get(
        color_name.strip()
    )

# MEESHO TECHNIQUE
MEESHO_TECHNIQUE_MAPPING = {
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

def get_meesho_technique(type):
    if not type:
        return None

    return MEESHO_TECHNIQUE_MAPPING.get(
        type.strip()
    )

# MEESHO OCCATION
MEESHO_OCCASION_MAPPING = {
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


def get_meesho_occasion(occasion):
    if not occasion:
        return None

    return MEESHO_OCCASION_MAPPING.get(
        occasion.strip()
    )


# MEESHO SAREE FABRIC
MEESHO_SAREE_FABRIC_MAPPING = {
    # Direct matches
    "georgette": "Poly Georgette",
    "simmer": "Polyester",
    "linen_blend": "Linen Blend",
}


def get_meesho_saree_fabric(saree_fabric):
    if not saree_fabric:
        return None

    return MEESHO_SAREE_FABRIC_MAPPING.get(
        saree_fabric.strip()
    )
# MEESHO BLOUSE FABRIC
MEESHO_BLOUSE_FABRIC_MAPPING = {
    # Direct matches
    "georgette":"Poly Georgette",
    "linen_blend":"Linen Blend",
    "chiffon":"Poly Chiffon",

}


def get_meesho_blouse_fabric(blouse_fabric):
    if not blouse_fabric:
        return None

    return MEESHO_BLOUSE_FABRIC_MAPPING.get(
        blouse_fabric.strip()
    )



# MEESHO BLOUSE 
MEESHO_BLOUSE_MAPPING = {
    # Direct matches
    "separate_blouse_piece":"Blouse Piece",
    "saree_with_multiple_blouse":"Blouse Piece",
    "running_blouse":"Blouse Piece",
    "without_blouse":"NA",
    "stitched_blouse":"Stitched Blouse",
    "semi_stitched_blouse": "Blouse Piece"
}


def get_meesho_blouse(blouse):
    if not blouse:
        return None

    return MEESHO_BLOUSE_MAPPING.get(
        blouse.strip()
    )

# MEESHO PATTERN 
MEESHO_PATTERN_MAPPING = {
    # Direct matches
   "SELF_DESIGN": "Woven Design",
   "EMBROIDERED": "Embroidered",
   "DIGITAL_PRINT": "Printed",
   "ZARI_EMBROIDERED":"ZARI_EMBROIDERED"
}


def get_meesho_pattern(pattern):
    if not pattern:
        return None

    return MEESHO_PATTERN_MAPPING.get(
        pattern.strip()
    )
# MEESHO PRINT_OR_PATTERN_TYPE_MAPPING
MEESHO_PRINT_OR_PATTERN_TYPE_MAPPING = {
    # Direct matches
    "solid":"Solid",
    "zari_butta": "Ethnic Motifs",
    "woven_design": "Woven Design",
    "botanical": "Floral",
    "floral": "Floral",
}


def get_meesho_print_or_pattern_type(print_or_pattern_type):
    if not print_or_pattern_type:
        return None

    return MEESHO_PRINT_OR_PATTERN_TYPE_MAPPING.get(
        print_or_pattern_type.strip()
    )
# MEESHO ORNAMENTATION 
MEESHO_ORNAMENTATION = {
    # Direct matches
    "cutwork": "Jaali",
    "embroidered": "Embroidered",
    "tassels_latkans": "NA"

}


def get_meesho_ornamentation(ornamentation):
    if not ornamentation:
        return None

    return MEESHO_ORNAMENTATION.get(
        ornamentation.strip()
    )


# MEESHO BORDER 
MEESHO_BORDER = {
    # Direct matches
    "embroidered": "Embroidered",
    "printed": "Printed",
}


def get_meesho_border(border):
    if not border:
        return None

    return MEESHO_BORDER.get(
        border.strip()
    )