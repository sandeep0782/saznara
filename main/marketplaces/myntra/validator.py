from main.marketplaces.myntra.mappings import get_myntra_blouse, get_myntra_blouse_fabric, get_myntra_border, get_myntra_color, get_myntra_occasion, get_myntra_ornamentation, get_myntra_pattern, get_myntra_print_or_pattern_type, get_myntra_saree_fabric, get_myntra_technique


MYNTRA_ALLOWED_COLORS = {
    "Red",
    "Blue",
    "Green",
    "Black",
    "Purple",
    "White",
    "Pink",
    "Grey",
    "Brown",
    "Yellow",
    "Orange",
    "Navy Blue",
    "Maroon",
    "Cream",
    "Silver",
    "Gold",
    "Tan",
    "Beige",
    "Peach",
    "Multi",
    "Copper",
    "Steel",
    "Olive",
    "Khaki",
    "Rose",
    "Taupe",
    "Off White",
    "Metallic",
    "Charcoal",
    "Grey Melange",
    "Turquoise Blue",
    "Coffee Brown",
    "Sea Green",
    "Lavender",
    "Lime Green",
    "Magenta",
    "Burgundy",
    "Teal",
    "Nude",
    "Bronze",
    "Fluorescent Green",
    "Rust",
    "Mustard",
    "NA",
    "Mauve",
    "Coral",
    "Rose Gold",
    "Assorted",
    "Champagne",
    "Fuchsia",
    "Violet",
    "Camel Brown",
    "Transparent",
}

def validate_myntra_colors(sku_list):

    invalid_colors = []

    for sku in sku_list:

        if not sku.color:
            continue

        original_color = sku.color.color

        mapped_color = get_myntra_color(original_color)

        if not mapped_color:
            invalid_colors.append(
                f"{original_color} - Missing mapping"
            )
            continue

        if mapped_color not in MYNTRA_ALLOWED_COLORS:
            invalid_colors.append(
                f"{original_color} -> {mapped_color} - Not a valid Myntra color"
            )

    return list(set(invalid_colors))


# MYNTRA TECHNIQUE
MYNTRA_ALLOWED_TECHNIQUE = {
"Bagh",
"Baluchari",
"Banarasi",
"Bandhani",
"Bhagalpuri",
"Chanderi",
"Ikat",
"Jamdani",
"Kanjeevaram",
"Kasavu",
"Kota",
"Leheriya",
"Maheshwari",
"Mangalagiri",
"Mysore Silk",
"Narayan Peth",
"Patola",
"Pochampally",
"Sambalpuri",
"Taant",
"Tussar",
"Venkatgiri",
"Khadi",
"NA",
"Dharmavaram",
"Kovai",
"Chettinad",
"Muga",
"Uppada",
"Garad",
"Paithani",
"Arani",
"Dabu",
"Bagru",
"Sungudi",
"Murshidabad silk",
"Bomkai silk",
"Ilkal",
"Gadwal",
"Block Print",
"Laal Paar",
}

def validate_myntra_technique(sku_list):

    invalid_technique = []

    for sku in sku_list:

        if not sku.type:
            continue

        original_type = sku.type

        mapped_technique = get_myntra_technique(original_type)

        if not mapped_technique:
            invalid_technique.append(
                f"{original_type} - Missing mapping"
            )
            continue

        if mapped_technique not in MYNTRA_ALLOWED_TECHNIQUE:
            invalid_technique.append(
                f"{original_type} -> {mapped_technique} - Not a valid Myntra Type/ Technique"
            )

    return list(set(invalid_technique))


# MYNTRA OCCATION
MYNTRA_ALLOWED_OCCASION = {
"Daily",
"Party",
"Traditional",
"Festive",
"Work",
"Fusion",
}

def validate_myntra_occasion(sku_list):

    invalid_occasion = []

    for sku in sku_list:

        if not sku.occasion:
            continue

        original_saree_fabric = sku.occasion

        mapped_occasion = get_myntra_occasion(original_saree_fabric)

        if not mapped_occasion:
            invalid_occasion.append(
                f"{original_saree_fabric} - Missing mapping"
            )
            continue

        if mapped_occasion not in MYNTRA_ALLOWED_OCCASION:
            invalid_occasion.append(
                f"{original_saree_fabric} -> {mapped_occasion} - Not a valid Myntra Occation"
            )

    return list(set(invalid_occasion))


# MYNTRA SAREE FABRIC
MYNTRA_ALLOWED_SAREE_FABRIC = {
"Art Silk",
"Pure Silk",
"Pure Cotton",
"Poly Georgette",
"Poly Crepe",
"Poly Chiffon",
"Jute Silk",
"Tissue",
"Velvet",
"Viscose Rayon",
"Net",
"Jute Cotton",
"Polycotton",
"Voile",
"Organza",
"Pure Georgette",
"Pure Crepe",
"Pure Chiffon",
"Supernet",
"Satin",
"Silk Cotton",
"Cotton Blend",
"Silk Blend",
"Poly Silk",
"Pure Linen",
"Linen Blend",
"Polyester",
"Nylon",
"Brocade",
"Brasso",
"Lace",
"Khandua Silk",
"Pashmina",
"Liva",
"Lycra",
"Lame",
"Modal Silk",
"Bemberg Crepe",
"Viscose Georgette",
"Silk Chiffon",
"Silk Georgette Satin",
"Silk Crepe",

}

def validate_myntra_saree_fabric(sku_list):

    invalid_saree_fabric = []

    for sku in sku_list:

        if not sku.saree_fabric:
            continue

        original_saree_fabric = sku.saree_fabric

        mapped_saree_fabric = get_myntra_saree_fabric(original_saree_fabric)

        if not mapped_saree_fabric:
            invalid_saree_fabric.append(
                f"{original_saree_fabric} - Missing mapping"
            )
            continue

        if mapped_saree_fabric not in MYNTRA_ALLOWED_SAREE_FABRIC:
            invalid_saree_fabric.append(
                f"{original_saree_fabric} -> {mapped_saree_fabric} - Not a valid Myntra Saree Fabric"
            )

    return list(set(invalid_saree_fabric))


# MYNTRA BLOUSE FABRIC
MYNTRA_ALLOWED_BLOUSE_FABRIC = {
"Art Silk",
"Pure Silk",
"Pure Cotton",
"Poly Georgette",
"Poly Crepe",
"Poly Chiffon",
"Jute Silk",
"Tissue",
"Velvet",
"Viscose Rayon",
"Net",
"Jute Cotton",
"Polycotton",
"Voile",
"Organza",
"Pure Georgette",
"Pure Crepe",
"Pure Chiffon",
"Supernet",
"Satin",
"Silk Cotton",
"Cotton Blend",
"NA",
"Silk Blend",
"Poly Silk",
"Polyester",
"Brocade",
"Brasso",
"Lace",
"Pure Linen",
"Linen Blend",
"Liva",
"Lycra",
"Modal Silk",
"Viscose Georgette",
"Bemberg Crepe",

}

def validate_myntra_blouse_fabric(sku_list):

    invalid_blouse_fabric = []

    for sku in sku_list:

        if not sku.blouse_fabric:
            continue

        original_blouse_fabric = sku.blouse_fabric

        mapped_blouse_fabric = get_myntra_blouse_fabric(original_blouse_fabric)

        if not mapped_blouse_fabric:
            invalid_blouse_fabric.append(
                f"{original_blouse_fabric} - Missing mapping"
            )
            continue

        if mapped_blouse_fabric not in MYNTRA_ALLOWED_BLOUSE_FABRIC:
            invalid_blouse_fabric.append(
                f"{original_blouse_fabric} -> {mapped_blouse_fabric} - Not a valid Myntra Blouse Fabric"
            )

    return list(set(invalid_blouse_fabric))



# MYNTRA BLOUSE FABRIC
MYNTRA_ALLOWED_BLOUSE = {
"Blouse Piece",
"NA",
"Stitched Blouse",

}

def validate_myntra_blouse(sku_list):

    invalid_blouse = []

    for sku in sku_list:

        if not sku.blouse:
            continue

        original_blouse = sku.blouse

        mapped_blouse = get_myntra_blouse(original_blouse)

        if not mapped_blouse:
            invalid_blouse.append(
                f"{original_blouse} - Missing mapping"
            )
            continue

        if mapped_blouse not in MYNTRA_ALLOWED_BLOUSE:
            invalid_blouse.append(
                f"{original_blouse} -> {mapped_blouse} - Not a valid Myntra Blouse"
            )

    return list(set(invalid_blouse))


# MYNTRA BLOUSE FABRIC
MYNTRA_ALLOWED_PATTERN = {
"Checked",
"Colourblocked",
"Embellished",
"Embroidered",
"Printed",
"Woven Design",
"Solid",
"Striped",
"Dyed",
}

def validate_myntra_pattern(sku_list):

    invalid_pttern = []

    for sku in sku_list:

        if not sku.pattern:
            continue

        original_pattern = sku.pattern

        mapped_pattern = get_myntra_pattern(original_pattern)

        if not mapped_pattern:
            invalid_pttern.append(
                f"{original_pattern} - Missing mapping"
            )
            continue

        if mapped_pattern not in MYNTRA_ALLOWED_PATTERN:
            invalid_pttern.append(
                f"{original_pattern} -> {mapped_pattern} - Not a valid Myntra Pattern"
            )

    return list(set(invalid_pttern))

# MYNTRA PRINT_OR_PATTERN_TYPE 
MYNTRA_ALLOWED_PRINT_OR_PATTERN_TYPE = {
"Floral",
"Paisley",
"Abstract",
"Polka Dots",
"Geometric",
"Woven Design",
"Bandhani",
"Leheriya",
"Solid",
"Ethnic Motifs",
"Tie and Dye",
"Embellished",
"Checked",
"Striped",
"Colourblocked",
"Ombre",
"Bagh",
"Dabu",
"Ajrak",
"Kalamkari",
"Warli",
"Batik",
}

def validate_myntra_print_or_pattern_type(sku_list):

    invalid_print_or_pattern_type = []

    for sku in sku_list:

        if not sku.print_or_pattern_type:
            continue

        original_print_or_pattern_type = sku.print_or_pattern_type

        mapped_print_or_pattern_type = get_myntra_print_or_pattern_type(original_print_or_pattern_type)

        if not mapped_print_or_pattern_type:
            invalid_print_or_pattern_type.append(
                f"{original_print_or_pattern_type} - Missing mapping"
            )
            continue

        if mapped_print_or_pattern_type not in MYNTRA_ALLOWED_PRINT_OR_PATTERN_TYPE:
            invalid_print_or_pattern_type.append(
                f"{original_print_or_pattern_type} -> {mapped_print_or_pattern_type} - Not a valid Myntra Print Or Pattern Type"
            )

    return list(set(invalid_print_or_pattern_type))


# MYNTRA ORNAMENTATION
MYNTRA_ALLOWED_ORNAMENTATION= {
"Embroidered",
"Zardozi",
"Sequinned",
"Mirror Work",
"Beads and Stones",
"Mukaish",
"Patchwork",
"NA",
"Jaali",
"Kashida",
"Phulkari",
"Kutchi Embroidery",
"Aari Work",
"Schiffli",
"Zari",
"Chikankari",
"Gotta Patti",
}

def validate_myntra_ornamentation(sku_list):

    invalid_ornamentation = []

    for sku in sku_list:

        if not sku.ornamentation:
            continue

        original_ornamentation = sku.ornamentation

        mapped_ornamentation = get_myntra_ornamentation(original_ornamentation)

        if not mapped_ornamentation:
            invalid_ornamentation.append(
                f"{original_ornamentation} - Missing mapping"
            )
            continue

        if mapped_ornamentation not in MYNTRA_ALLOWED_ORNAMENTATION:
            invalid_ornamentation.append(
                f"{original_ornamentation} -> {mapped_ornamentation} - Not a valid Myntra Ornamentation"
            )

    return list(set(invalid_ornamentation))


# MYNTRA BORDER
MYNTRA_ALLOWED_BORDER= {
"No Border",
"Zari",
"Embroidered",
"Solid",
"Printed",
"Embellished",
"Woven Design",
"Checked",
"Striped",
"Scallop",
}

def validate_myntra_border(sku_list):

    invalid_border = []

    for sku in sku_list:

        if not sku.border:
            continue

        original_border = sku.border

        mapped_border = get_myntra_border(original_border)

        if not mapped_border:
            invalid_border.append(
                f"{original_border} - Missing mapping"
            )
            continue

        if mapped_border not in MYNTRA_ALLOWED_BORDER:
            invalid_border.append(
                f"{original_border} -> {mapped_border} - Not a valid Myntra Border"
            )

    return list(set(invalid_border))




def validate_myntra_template(sku_list):

    errors = {}

    # COLORS ERRORS
    color_errors = validate_myntra_colors(sku_list)
    if color_errors:
        errors["Color"] = color_errors


    # TECHNIQUE ERRORS
    technique_errors = validate_myntra_technique(sku_list)
    if technique_errors:
        errors["Type"] = technique_errors


    # OCCASION ERRORS
    occasion_errors = validate_myntra_occasion(sku_list)
    if occasion_errors:
        errors["Occasion"] = occasion_errors

    # SAREE FABRIC ERRORS
    saree_fabric_errors = validate_myntra_saree_fabric(sku_list)
    if saree_fabric_errors:
        errors["Saree Fabric"] = saree_fabric_errors

    # BLOUSE FABRIC ERRORS
    blouse_fabric_errors = validate_myntra_blouse_fabric(sku_list)
    if blouse_fabric_errors:
        errors["Blouse Fabric"] = blouse_fabric_errors
    
    # BLOUSE ERRORS
    blouse_errors = validate_myntra_blouse(sku_list)
    if blouse_errors:
        errors["Blouse"] = blouse_errors

    # BLOUSE ERRORS
    pattern_errors = validate_myntra_pattern(sku_list)
    if pattern_errors:
        errors["Pattern"] = pattern_errors
    
    # print_or_pattern_type ERROR
    print_or_pattern_type_errors = validate_myntra_print_or_pattern_type(sku_list)
    if print_or_pattern_type_errors:
        errors["Print Or Pattern Type"] = print_or_pattern_type_errors
    
    # Ornamentation ERROR
    ornamentation_errors = validate_myntra_ornamentation(sku_list)
    if ornamentation_errors:
        errors["Ornamentation"] = ornamentation_errors
    
    # BORDER ERROR
    border_errors = validate_myntra_border(sku_list)
    if border_errors:
        errors["Border"] = border_errors
    
    # fabric_errors = validate_myntra_fabric(sku_list)
    # if fabric_errors:
    #     errors["Fabric"] = fabric_errors


    return errors