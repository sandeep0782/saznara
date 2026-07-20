
from main.marketplaces.flipkart.mappings import get_flipkart_blouse, get_flipkart_blouse_fabric, get_flipkart_border, get_flipkart_color, get_flipkart_occasion, get_flipkart_ornamentation, get_flipkart_pattern, get_flipkart_print_or_pattern_type, get_flipkart_saree_fabric, get_flipkart_technique 

FLIPKART_ALLOWED_COLORS = {
"Beige",
"Black",
"Blue",
"Brown",
"Cream",
"Dark Blue",
"Dark Green",
"Gold",
"Green",
"Grey",
"Light Blue",
"Light Green",
"Magenta",
"Maroon",
"Multicolor",
"Mustard",
"Orange",
"Pink",
"Purple",
"Red",
"Silver",
"White",
"Yellow",
}

def validate_flipkart_colors(sku_list):

    invalid_colors = []

    for sku in sku_list:

        if not sku.color:
            continue

        original_color = sku.color.color

        mapped_color = get_flipkart_color(original_color)

        if not mapped_color:
            invalid_colors.append(
                f"{original_color} - Missing mapping"
            )
            continue

        if mapped_color not in FLIPKART_ALLOWED_COLORS:
            invalid_colors.append(
                f"{original_color} -> {mapped_color} - Not a valid Myntra color"
            )

    return list(set(invalid_colors))


# MYNTRA TECHNIQUE
FLIPKART_ALLOWED_TECHNIQUE = {
    "Abstract",
    "Ajrakh",
    "Animal Print",
    "Applique",
    "Aztec Print",
    "Bandhni",
    "Batik",
    "Block Print",
    "Botanical Prints",
    "Checkered",
    "Chevron/Zig Zag",
    "Colorblock",
    "Conversational",
    "Digital Prints",
    "Embellished",
    "Embroidered",
    "Ethnic Motifs",
    "Floral",
    "Foil Print",
    "Geometric",
    "Graphic",
    "Hand Paint",
    "Herringbone",
    "Human Figures",
    "Ikkat",
    "Kalamkari",
    "Leheriya",
    "Mirror Work",
    "Ombre",
    "Paisley",
    "Polka",
    "Quirky",
    "Sanganeri",
    "Self Design",
    "Sequin",
    "Shibori",
    "Solid",
    "Striped",
    "Temple Border Prints",
    "Tie & Dye",
    "Tribal",
    "Typography",
    "Warli",
    "Woven Design",
}

def validate_flipkart_technique(sku_list):

    invalid_technique = []

    for sku in sku_list:

        if not sku.type:
            continue

        original_type = sku.type

        mapped_technique = get_flipkart_technique(original_type)

        if not mapped_technique:
            invalid_technique.append(
                f"{original_type} - Missing mapping"
            )
            continue

        if mapped_technique not in FLIPKART_ALLOWED_TECHNIQUE:
            invalid_technique.append(
                f"{original_type} -> {mapped_technique} - Not a valid Myntra Type/ Technique"
            )

    return list(set(invalid_technique))


# MYNTRA OCCATION
FLIPKART_ALLOWED_OCCASION = {
"Casual",
"Festive",
"Party",
"Party & Festive",
"Wedding",
"Wedding & Festive",
}

def validate_flipkart_occasion(sku_list):

    invalid_occasion = []

    for sku in sku_list:

        if not sku.occasion:
            continue

        original_saree_fabric = sku.occasion

        mapped_occasion = get_flipkart_occasion(original_saree_fabric)

        if not mapped_occasion:
            invalid_occasion.append(
                f"{original_saree_fabric} - Missing mapping"
            )
            continue

        if mapped_occasion not in FLIPKART_ALLOWED_OCCASION:
            invalid_occasion.append(
                f"{original_saree_fabric} -> {mapped_occasion} - Not a valid Flipkart Occation"
            )

    return list(set(invalid_occasion))


# MYNTRA SAREE FABRIC
FLIPKART_ALLOWED_SAREE_FABRIC = {
    "Art Silk",
    "Brasso",
    "Brocade",
    "Chanderi",
    "Chiffon",
    "Cotton Blend",
    "Cotton Jute",
    "Cotton Linen",
    "Cotton Silk",
    "Crepe",
    "Dupion Silk",
    "Georgette",
    "Jacquard",
    "Jimmy Jimmy",
    "Jute Silk",
    "Khadi",
    "Lace",
    "Linen",
    "Lycra",
    "Lycra Blend",
    "Mulmul",
    "Muslin",
    "Net",
    "Nylon",
    "Organza",
    "Polyester",
    "Pure Cotton",
    "Pure Silk",
    "Raw Silk",
    "Satin",
    "Semi-Pashmina",
    "Silk Blend",
    "Supernet",
    "Tissue",
    "Tussar Silk",
    "Velvet",
    "Viscose Rayon",
}

def validate_flipkart_saree_fabric(sku_list):

    invalid_saree_fabric = []

    for sku in sku_list:

        if not sku.saree_fabric:
            continue

        original_saree_fabric = sku.saree_fabric

        mapped_saree_fabric = get_flipkart_saree_fabric(original_saree_fabric)

        if not mapped_saree_fabric:
            invalid_saree_fabric.append(
                f"{original_saree_fabric} - Missing mapping"
            )
            continue

        if mapped_saree_fabric not in FLIPKART_ALLOWED_SAREE_FABRIC:
            invalid_saree_fabric.append(
                f"{original_saree_fabric} -> {mapped_saree_fabric} - Not a valid Flipkart Saree Fabric"
            )

    return list(set(invalid_saree_fabric))


# MYNTRA BLOUSE FABRIC
FLIPKART_ALLOWED_BLOUSE_FABRIC = {
    "Acrylic Wool",
    "Art Silk",
    "Banarasi Silk",
    "Brasso",
    "Brocade",
    "Cambric",
    "Cashmere",
    "Chanderi",
    "Chenille",
    "Chiffon",
    "Corduroy",
    "Cotton",
    "Cotton Linen Blend",
    "Cotton Lycra Blend",
    "Cotton Slub",
    "Crepe",
    "Damask",
    "Denim",
    "Dupion Silk",
    "Flannel",
    "Georgette",
    "Glass Tissue",
    "Hoisery",
    "Jacquard",
    "Jute",
    "Khadi",
    "Kota Cotton",
    "Lace",
    "Linen",
    "Lycra",
    "Merino Wool",
    "Mettalic Yarn",
    "Modal",
    "Muslin",
    "NA",
    "Net",
    "Nylon",
    "Nylon Wool Blend",
    "Organza",
    "PU",
    "Poly Silk",
    "Polycotton",
    "Polyester",
    "Printed Silk",
    "Pure Chiffon",
    "Pure Crepe",
    "Pure Georgette",
    "Pure Silk",
    "Raw Silk",
    "Rayon",
    "Satin",
    "Sequined Fabric",
    "Shantung",
    "Shimmer Fabric",
    "Silk",
    "Silk Cotton Blend",
    "Silk Linen Blend",
    "Silk Wool Blend",
    "Suede",
    "Swiss Dot",
    "Synthetic",
    "Synthetic Chiffon",
    "Synthetic Crepe",
    "Synthetic Fabric",
    "Synthetic Georgette",
    "Taffeta",
    "Tissue",
    "Tissue Silk",
    "Tulle",
    "Tussar Silk",
    "Tweed",
    "Velvet",
    "Viscose",
    "Voile",
    "Wool",
    "Worsted Wool",
}


def validate_flipkart_blouse_fabric(sku_list):

    invalid_blouse_fabric = []

    for sku in sku_list:

        if not sku.blouse_fabric:
            continue

        original_blouse_fabric = sku.blouse_fabric

        mapped_blouse_fabric = get_flipkart_blouse_fabric(original_blouse_fabric)

        if not mapped_blouse_fabric:
            invalid_blouse_fabric.append(
                f"{original_blouse_fabric} - Missing mapping"
            )
            continue

        if mapped_blouse_fabric not in FLIPKART_ALLOWED_BLOUSE_FABRIC:
            invalid_blouse_fabric.append(
                f"{original_blouse_fabric} -> {mapped_blouse_fabric} - Not a valid Flipkart Blouse Fabric"
            )

    return list(set(invalid_blouse_fabric))



# MYNTRA BLOUSE FABRIC
FLIPKART_ALLOWED_BLOUSE = {
    "No Blouse",
    "Semi-Stitched",
    "Stitched",
    "Unstitched",
    "Attached",

}

def validate_flipkart_blouse(sku_list):

    invalid_blouse = []

    for sku in sku_list:

        if not sku.blouse:
            continue

        original_blouse = sku.blouse

        mapped_blouse = get_flipkart_blouse(original_blouse)

        if not mapped_blouse:
            invalid_blouse.append(
                f"{original_blouse} - Missing mapping"
            )
            continue

        if mapped_blouse not in FLIPKART_ALLOWED_BLOUSE:
            invalid_blouse.append(
                f"{original_blouse} -> {mapped_blouse} - Not a valid Myntra Blouse"
            )

    return list(set(invalid_blouse))


# MYNTRA BLOUSE FABRIC
FLIPKART_ALLOWED_PATTERN = {
 "Animal Print",
    "Applique",
    "Blocked Printed",
    "Checkered",
    "Color Block",
    "Digital Print",
    "Dyed",
    "Embellished",
    "Embroidered",
    "Floral Print",
    "Geometric Print",
    "Graphic Print",
    "Hand Painted",
    "Ombre",
    "Paisley",
    "Polka Print",
    "Printed",
    "Self Design",
    "Solid/Plain",
    "Striped",
    "Temple Border",
    "Tie-Dye",
    "Woven",
}

def validate_flipkart_pattern(sku_list):

    invalid_pttern = []

    for sku in sku_list:

        if not sku.pattern:
            continue

        original_pattern = sku.pattern

        mapped_pattern = get_flipkart_pattern(original_pattern)

        if not mapped_pattern:
            invalid_pttern.append(
                f"{original_pattern} - Missing mapping"
            )
            continue

        if mapped_pattern not in FLIPKART_ALLOWED_PATTERN:
            invalid_pttern.append(
                f"{original_pattern} -> {mapped_pattern} - Not a valid Flipkart Pattern"
            )

    return list(set(invalid_pttern))

# MYNTRA PRINT_OR_PATTERN_TYPE 
FLIPKART_ALLOWED_PRINT_OR_PATTERN_TYPE = {
    "Abstract",
    "Ajrakh",
    "Animal Print",
    "Applique",
    "Aztec Print",
    "Bandhni",
    "Batik",
    "Block Print",
    "Botanical Prints",
    "Checkered",
    "Chevron/Zig Zag",
    "Colorblock",
    "Conversational",
    "Digital Prints",
    "Embellished",
    "Embroidered",
    "Ethnic Motifs",
    "Floral",
    "Foil Print",
    "Geometric",
    "Graphic",
    "Hand Paint",
    "Herringbone",
    "Human Figures",
    "Ikkat",
    "Kalamkari",
    "Leheriya",
    "Mirror work",
    "Ombre",
    "Paisley",
    "Polka",
    "Quirky",
    "Sanganeri",
    "Self Design",
    "Sequin",
    "Shibori",
    "Solid",
    "Striped",
    "Temple Border Prints",
    "Tie & Dye",
    "Tribal",
    "Typography",
    "Warli",
    "Woven Design",
}

def validate_flipkart_print_or_pattern_type(sku_list):

    invalid_print_or_pattern_type = []

    for sku in sku_list:

        if not sku.print_or_pattern_type:
            continue

        original_print_or_pattern_type = sku.print_or_pattern_type

        mapped_print_or_pattern_type = get_flipkart_print_or_pattern_type(original_print_or_pattern_type)

        if not mapped_print_or_pattern_type:
            invalid_print_or_pattern_type.append(
                f"{original_print_or_pattern_type} - Missing mapping"
            )
            continue

        if mapped_print_or_pattern_type not in FLIPKART_ALLOWED_PRINT_OR_PATTERN_TYPE:
            invalid_print_or_pattern_type.append(
                f"{original_print_or_pattern_type} -> {mapped_print_or_pattern_type} - Not a valid Flipkart Print Or Pattern Type"
            )

    return list(set(invalid_print_or_pattern_type))


# MYNTRA ORNAMENTATION
FLIPKART_ALLOWED_ORNAMENTATION= {
    "Beads",
    "Brocade",
    "Cotton Thread",
    "Decorative Stones",
    "Floral Design",
    "Fringes",
    "Gota",
    "Kundan",
    "Lace",
    "Metal Embellishment",
    "Mirror",
    "Mukesh",
    "NA",
    "Patchwork",
    "Pom Pom",
    "Resham/ Silk Thread",
    "Ruffle",
    "Schiffli",
    "Sequinns",
    "Shimmer",
    "Silver Thread",
    "Swarovski Crystal",
    "Tassel",
    "Zari",
    "Zari Buta",
}

def validate_flipkart_ornamentation(sku_list):

    invalid_ornamentation = []

    for sku in sku_list:

        if not sku.ornamentation:
            continue

        original_ornamentation = sku.ornamentation

        mapped_ornamentation = get_flipkart_ornamentation(original_ornamentation)

        if not mapped_ornamentation:
            invalid_ornamentation.append(
                f"{original_ornamentation} - Missing mapping"
            )
            continue

        if mapped_ornamentation not in FLIPKART_ALLOWED_ORNAMENTATION:
            invalid_ornamentation.append(
                f"{original_ornamentation} -> {mapped_ornamentation} - Not a valid Flipkart Ornamentation"
            )

    return list(set(invalid_ornamentation))


# MYNTRA BORDER
FLIPKART_ALLOWED_BORDER= {
    "Beaded",
    "Embroidered",
    "Gold",
    "Heavy",
    "Lace",
    "None",
    "Printed",
    "Self Design",
    "Sequins",
    "Solid",
    "Zari",
}

def validate_flipkart_border(sku_list):

    invalid_border = []

    for sku in sku_list:

        if not sku.border:
            continue

        original_border = sku.border

        mapped_border = get_flipkart_border(original_border)

        if not mapped_border:
            invalid_border.append(
                f"{original_border} - Missing mapping"
            )
            continue

        if mapped_border not in FLIPKART_ALLOWED_BORDER:
            invalid_border.append(
                f"{original_border} -> {mapped_border} - Not a valid Flipkart Border"
            )

    return list(set(invalid_border))




def validate_flipkart_template(sku_list):

    errors = {}

    # COLORS ERRORS
    color_errors = validate_flipkart_colors(sku_list)
    if color_errors:
        errors["Color"] = color_errors


    # TECHNIQUE ERRORS
    technique_errors = validate_flipkart_technique(sku_list)
    if technique_errors:
        errors["Type"] = technique_errors


    # OCCASION ERRORS
    occasion_errors = validate_flipkart_occasion(sku_list)
    if occasion_errors:
        errors["Occasion"] = occasion_errors

    # SAREE FABRIC ERRORS
    saree_fabric_errors = validate_flipkart_saree_fabric(sku_list)
    if saree_fabric_errors:
        errors["Saree Fabric"] = saree_fabric_errors

    # BLOUSE FABRIC ERRORS
    blouse_fabric_errors = validate_flipkart_blouse_fabric(sku_list)
    if blouse_fabric_errors:
        errors["Blouse Fabric"] = blouse_fabric_errors
    
    # BLOUSE ERRORS
    blouse_errors = validate_flipkart_blouse(sku_list)
    if blouse_errors:
        errors["Blouse"] = blouse_errors

    # BLOUSE ERRORS
    pattern_errors = validate_flipkart_pattern(sku_list)
    if pattern_errors:
        errors["Pattern"] = pattern_errors
    
    # print_or_pattern_type ERROR
    print_or_pattern_type_errors = validate_flipkart_print_or_pattern_type(sku_list)
    if print_or_pattern_type_errors:
        errors["Print Or Pattern Type"] = print_or_pattern_type_errors
    
    # Ornamentation ERROR
    ornamentation_errors = validate_flipkart_ornamentation(sku_list)
    if ornamentation_errors:
        errors["Ornamentation"] = ornamentation_errors
    
    # BORDER ERROR
    border_errors = validate_flipkart_border(sku_list)
    if border_errors:
        errors["Border"] = border_errors
    
    # fabric_errors = validate_flipkart_fabric(sku_list)
    # if fabric_errors:
    #     errors["Fabric"] = fabric_errors


    return errors