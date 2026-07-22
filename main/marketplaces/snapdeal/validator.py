from main.marketplaces.snapdeal.mappings import ( get_snapdeal_blouse, get_snapdeal_blouse_color,get_snapdeal_blouse_fabric, get_snapdeal_blouse_pattern, get_snapdeal_border, get_snapdeal_color, get_snapdeal_ornamentation, get_snapdeal_pattern, get_snapdeal_print_or_pattern_type, get_snapdeal_saree_fabric, get_snapdeal_technique
)


# SNAPDEAL COLOR

SNAPDEAL_ALLOWED_COLORS = {
    "Beige",
    "Beige1",
    "Black",
    "Blue",
    "Bronze",
    "Brown",
    "Burgundy",
    "Charcoal",
    "Coffee",
    "Coral",
    "Cream",
    "Dark Grey",

    "Fluorescent Green",
    "Fluorescent Orange",
    "Fluorescent Pink",

    "Gold",
    "Green",
    "Grey",
    "Grey Melange",

    "Indigo",
    "Khaki",
    "Lavender",

    "Light Blue",
    "Light Green",
    "Light Grey",
    "LightBLue",
    "LightGreen",

    "Lime Green",
    "Lime Green1",

    "Magenta",
    "Maroon",
    "Mauve",
    "Mint Green",

    "Multicolor",

    "Mustard",
    "Navy Blue",
    "Nude",
    "Off White",

    "Olive",

    "Orange",
    "Peach",
    "Pink",

    "Purple",

    "Rama",
    "Rani",

    "Red",
    "Rose Gold",

    "Rust",

    "Sea Green",
    "Silver",

    "Tan",
    "Teal",
    "Turquoise",

    "White",

    "Wine",

    "Yellow",
    "Yellow1",

    "Aqua Blue",

    "Multicolor 1",
    "Multicolor 2",
    "Multicolor 3",
    "Multicolor 4",
    "Multicolor 5",
    "Multicolor 6",
    "Multicolor 7",
    "Multicolor 8",
    "Multicolor 9",
    "Multicolor 10",
    "Multicolor 11",
    "Multicolor 12",
    "Multicolor 13",
    "Multicolor 14",
    "Multicolor 15",
    "Multicolor 16",
    "Multicolor 17",
    "Multicolor 18",
    "Multicolor 19",
    "Multicolor 20",

    "Sky Blue",

    "Coffee Brown",

    "Fuchsia",
}


def validate_snapdeal_colors(sku_list):

    invalid_colors = []

    for sku in sku_list:

        if not sku.color:
            continue

        original_color = sku.color.color

        mapped_color = get_snapdeal_color(original_color)

        if not mapped_color:
            invalid_colors.append(
                f"{original_color} - Missing mapping"
            )
            continue

        if mapped_color not in SNAPDEAL_ALLOWED_COLORS:
            invalid_colors.append(
                f"{original_color} -> {mapped_color} - Not a valid Snapdeal color"
            )

    return list(set(invalid_colors))


SNAPDEAL_ALLOWED_BLOUSE_COLORS = {
    "Beige",
    "Black",
    "Blue",
    "Brown",
    "Gold",
    "Grey",
    "Green",
    "Maroon",
    "Orange",
    "Pink",
    "Purple",
    "Red",
    "Silver",
    "White",
    "Yellow",
    "Not Applicable",
    "Multicolor",
    "Cream",
    "Nude",
    "Navy Blue",
    "Teal",
    "Indigo",
    "Light Blue",
    "Bronze",
    "Camel",
    "Coffee",
    "Fluorescent Green",
    "Olive",
    "Sea Green",
    "Mint Green",
    "Lime Green",
    "Charcoal",
    "Grey Melange",
    "Dark Grey",
    "Light Grey",
    "Rust",
    "Fluorescent Orange",
    "Fluorescent Pink",
    "Magenta",
    "Rose Gold",
    "Mauve",
    "Violet",
    "Lavender",
    "Burgundy",
    "Wine",
    "Khaki",
    "Tan",
    "Turquoise",
    "Coral",
    "Peach",
    "Off White",
    "Mustard",
    "Aqua Blue",
}


def validate_snapdeal_blouse_colors(sku_list):

    invalid_blouse_colors = []

    for sku in sku_list:

        if not sku.blouse_color:
            continue

        original_blouse_color = sku.blouse_color

        mapped_color = get_snapdeal_blouse_color(original_blouse_color)

        if not mapped_color:
            invalid_blouse_colors.append(
                f"{original_blouse_color} - Missing mapping"
            )
            continue

        if mapped_color not in SNAPDEAL_ALLOWED_BLOUSE_COLORS:
            invalid_blouse_colors.append(
                f"{original_blouse_color} -> {mapped_color} - Not a valid Snapdeal color"
            )

    return list(set(invalid_blouse_colors))



# SNAPDEAL TECHNIQUE

SNAPDEAL_ALLOWED_TECHNIQUE = {
    "Baluchari Saree",
    "Banarasi saree",
    "Bandhani Sarees",
    "Bhagalpuri Saree",
    "Bomkai Saree",
    "Chanderi saree",
    "Chettinad Saree",
    "Chikankari Saree",
    "Coorgi Saree",
    "Dharmavaram Saree",
    "Foam Saree",
    "Goan Kunbi Saree",
    "Ilkal Saree",
    "Jamdani Saree",
    "Kanjeevaram Sarees",
    "Kasavu Saree",
    "Kashmiri Kani Saree",
    "Kota Doria Saree",
    "Leheriya Saree",
    "Maheshwari Saree",
    "Mangalgiri Saree",
    "Mashru Saree",
    "Mekhela Chador",
    "Muga Silk Saree",
    "Mysore Silk Sarees",
    "Narayanpet Saree",
    "Paithani Sarees",
    "Pashmina Saree",
    "Patola Saree",
    "Phulkari saree",
    "Pochampally Ikkat Saree",
    "Regular Saree",
    "Sambalpuri Saree",
    "Tant Saree",
    "Uppada saree",
    "Venkatagiri Saree",

}


def validate_snapdeal_technique(sku_list):

    invalid_technique = []

    for sku in sku_list:

        if not sku.type:
            continue

        original_type = sku.type

        mapped_technique = get_snapdeal_technique(original_type)

        if not mapped_technique:
            invalid_technique.append(
                f"{original_type} - Missing mapping"
            )
            continue

        if mapped_technique not in SNAPDEAL_ALLOWED_TECHNIQUE:
            invalid_technique.append(
                f"{original_type} -> {mapped_technique} - Not a valid Snapdeal Type/Technique"
            )

    return list(set(invalid_technique))


# SNAPDEAL SAREE FABRIC

SNAPDEAL_ALLOWED_SAREE_FABRIC = {
    "Art Silk",
    "Asaam Silk",
    "Brasso",
    "Brocade",
    "Chanderi",
    "Chiffon",
    "Cotton",
    "Cotton Blend",
    "Cotton Silk",
    "Crepe",
    "Georgette",
    "Jacquard",
    "Jimmy Choo",
    "Jute",
    "Linen",
    "Lycra",
    "Net",
    "Nylon",
    "Organza",
    "Polyester",
    "Rayon",
    "Satin",
    "Shimmer",
    "Silk",
    "Silk Blend",
    "Synthetic",
    "Taffeta",
    "Tissue",
    "Velvet",
    "Viscose",
    "Bangalore Silk",
}


def validate_snapdeal_saree_fabric(sku_list):

    invalid_saree_fabric = []

    for sku in sku_list:

        if not sku.saree_fabric:
            continue

        original_saree_fabric = sku.saree_fabric

        mapped_saree_fabric = get_snapdeal_saree_fabric(
            original_saree_fabric
        )

        if not mapped_saree_fabric:
            invalid_saree_fabric.append(
                f"{original_saree_fabric} - Missing mapping"
            )
            continue

        if mapped_saree_fabric not in SNAPDEAL_ALLOWED_SAREE_FABRIC:
            invalid_saree_fabric.append(
                f"{original_saree_fabric} -> {mapped_saree_fabric} - Not a valid Snapdeal Saree Fabric"
            )

    return list(set(invalid_saree_fabric))

# SNAPDEAL BLOUSE FABRIC

SNAPDEAL_ALLOWED_BLOUSE_FABRIC = {
    "Acrylic",
    "Art Silk",
    "Banarasi Silk",
    "Bangalore Silk",
    "Brasso",
    "Brocade",
    "Chanderi",
    "Chiffon",
    "Cotton",
    "Cotton Blend",
    "Crepe",
    "Crochet",
    "Georgette",
    "Jacquard",
    "Jute",
    "Lace",
    "Linen",
    "Lycra",
    "Net",
    "Not Applicable",
    "Nylon",
    "Organza",
    "Polyester",
    "Poplin",
    "Rayon",
    "Satin",
    "Silk",
    "Silk Blend",
    "Taffeta Silk",
    "Tissue",
    "Tussar",
    "Velvet",
    "Viscose",
    "Viscose Rayon",
    "Shimmer",
}


def validate_snapdeal_blouse_fabric(sku_list):

    invalid_blouse_fabric = []

    for sku in sku_list:

        if not sku.blouse_fabric:
            continue

        original_blouse_fabric = sku.blouse_fabric

        mapped_blouse_fabric = get_snapdeal_blouse_fabric(
            original_blouse_fabric
        )

        if not mapped_blouse_fabric:
            invalid_blouse_fabric.append(
                f"{original_blouse_fabric} - Missing mapping"
            )
            continue

        if mapped_blouse_fabric not in SNAPDEAL_ALLOWED_BLOUSE_FABRIC:
            invalid_blouse_fabric.append(
                f"{original_blouse_fabric} -> {mapped_blouse_fabric} - Not a valid Snapdeal Blouse Fabric"
            )

    return list(set(invalid_blouse_fabric))



# SNAPDEAL BLOUSE

SNAPDEAL_ALLOWED_BLOUSE = {
    "With Unstitched Blouse Piece",
    "With Stitched Blouse",
    "Without Blouse Piece",
}


def validate_snapdeal_blouse(sku_list):

    invalid_blouse = []

    for sku in sku_list:

        if not sku.blouse:
            continue

        original_blouse = sku.blouse

        mapped_blouse = get_snapdeal_blouse(original_blouse)

        if not mapped_blouse:
            invalid_blouse.append(
                f"{original_blouse} - Missing mapping"
            )
            continue

        if mapped_blouse not in SNAPDEAL_ALLOWED_BLOUSE:
            invalid_blouse.append(
                f"{original_blouse} -> {mapped_blouse} - Not a valid Snapdeal Blouse"
            )

    return list(set(invalid_blouse))



# SNAPDEAL PATTERN
SNAPDEAL_ALLOWED_PATTERN = {
    "Applique",
    "Colorblock",
    "Dyed",
    "Embellished",
    "Embroidered",
    "Printed",
    "Self Design",
    "Striped",
    "Solid",
    "Cut Outs",
    "Woven",
    "Checked",
    "Woven Design",
}

def validate_snapdeal_pattern(sku_list):

    invalid_pattern = []

    for sku in sku_list:

        if not sku.pattern:
            continue

        original_pattern = sku.pattern

        mapped_pattern = get_snapdeal_pattern(original_pattern)

        if not mapped_pattern:
            invalid_pattern.append(
                f"{original_pattern} - Missing mapping"
            )
            continue

        if mapped_pattern not in SNAPDEAL_ALLOWED_PATTERN:
            invalid_pattern.append(
                f"{original_pattern} -> {mapped_pattern} - Not a valid Snapdeal Pattern"
            )

    return list(set(invalid_pattern))



# SNAPDEAL BLOUSE PATTERN
SNAPDEAL_ALLOWED_BLOUSE_PATTERN = {
"Applique",
"Checks",
"Colorblock",
"Dyed",
"Embellished",
"Embroidered",
"Printed",
"Self Design",
"Plain",
"Striped",
"Cut-Outs",
"Sequined",
"Jacquard",
"Solid",
"Zari Woven",
}

def validate_snapdeal_blouse_pattern(sku_list):

    invalid_blouse_pattern = []

    for sku in sku_list:

        if not sku.blouse_pattern:
            continue

        original_blouse_pattern = sku.blouse_pattern

        mapped_blouse_pattern = get_snapdeal_blouse_pattern(original_blouse_pattern)

        if not mapped_blouse_pattern:
            invalid_blouse_pattern.append(
                f"{original_blouse_pattern} - Missing mapping"
            )
            continue

        if mapped_blouse_pattern not in SNAPDEAL_ALLOWED_BLOUSE_PATTERN:
            invalid_blouse_pattern.append(
                f"{original_blouse_pattern} -> {mapped_blouse_pattern} - Not a valid Snapdeal Blouse Pattern"
            )

    return list(set(invalid_blouse_pattern))


# SNAPDEAL PRINT OR PATTERN TYPE

SNAPDEAL_ALLOWED_PRINT_OR_PATTERN_TYPE = {
    "Abstract",
    "Ajrakh",
    "Animal",
    "Bagru Print",
    "Baluchari",
    "Bandhani",
    "Bandhej",
    "Batik",
    "Beads and Stones",
    "Birds",
    "Block",
    "Block Print",
    "Brand Logo",
    "Camouflage",
    "Checked",
    "Chevron",
    "Chikankari",
    "Colorblock",
    "Embossed",
    "Ethnic Motif",
    "Ethnic Motifs",
    "Floral",
    "Foil",
    "Geometric",
    "Gotta Patti",
    "Graphic",
    "Humor & Comic",
    "Ikat",
    "Indigo",
    "Jamawar",
    "Kalamkari",
    "Kantha Work",
    "Kasavu",
    "Leheria",
    "Madhubani",
    "Mirror Work",
    "Music",
    "Nature",
    "Ombre",
    "Paisely",
    "Paisley",
    "PatchWork",
    "Patola",
    "People",
    "Phulkari",
    "Pochampally",
    "Polka Dots",
    "Religious",
    "Sambalpuri",
    "Sequined",
    "Solid",
    "Superhero",
    "Textured",
    "Thread Work",
    "Tie & Dye",
    "Tribal",
    "Typography",
    "Warli Art",
    "Zardorsi",
    "Zari Work",
    "Striped",
    "Digital Printed",
    "Bagru",
    "Buta",
}


def validate_snapdeal_print_or_pattern_type(sku_list):

    invalid_print_or_pattern_type = []

    for sku in sku_list:

        if not sku.print_or_pattern_type:
            continue

        original_print_or_pattern_type = sku.print_or_pattern_type

        mapped_print_or_pattern_type = get_snapdeal_print_or_pattern_type(
            original_print_or_pattern_type
        )

        if not mapped_print_or_pattern_type:
            invalid_print_or_pattern_type.append(
                f"{original_print_or_pattern_type} - Missing mapping"
            )
            continue

        if mapped_print_or_pattern_type not in SNAPDEAL_ALLOWED_PRINT_OR_PATTERN_TYPE:
            invalid_print_or_pattern_type.append(
                f"{original_print_or_pattern_type} -> {mapped_print_or_pattern_type} - Not a valid Snapdeal Print Or Pattern Type"
            )

    return list(set(invalid_print_or_pattern_type))

# SNAPDEAL ORNAMENTATION

SNAPDEAL_ALLOWED_ORNAMENTATION = {

}


def validate_snapdeal_ornamentation(sku_list):

    invalid_ornamentation = []

    for sku in sku_list:

        if not sku.ornamentation:
            continue

        original_ornamentation = sku.ornamentation

        mapped_ornamentation = get_snapdeal_ornamentation(
            original_ornamentation
        )

        if not mapped_ornamentation:
            invalid_ornamentation.append(
                f"{original_ornamentation} - Missing mapping"
            )
            continue

        if mapped_ornamentation not in SNAPDEAL_ALLOWED_ORNAMENTATION:
            invalid_ornamentation.append(
                f"{original_ornamentation} -> {mapped_ornamentation} - Not a valid Snapdeal Ornamentation"
            )

    return list(set(invalid_ornamentation))



# SNAPDEAL BORDER

SNAPDEAL_ALLOWED_BORDER = {
    "Digital Printed",
    "Kantha Work",
    "Mirror Work",
    "Printed",
    "Plain",
    "Embellished",
    "Embroidered",
    "Stone work",
    "Zari Work",
    "Block printed",
    "Cut work",
    "Sequined",
    "Zardosi work",
    "Floral",
    "None",
    "Lace",
    "Woven Design",
}


def validate_snapdeal_border(sku_list):

    invalid_border = []

    for sku in sku_list:

        if not sku.border:
            continue

        original_border = sku.border

        mapped_border = get_snapdeal_border(original_border)

        if not mapped_border:
            invalid_border.append(
                f"{original_border} - Missing mapping"
            )
            continue

        if mapped_border not in SNAPDEAL_ALLOWED_BORDER:
            invalid_border.append(
                f"{original_border} -> {mapped_border} - Not a valid Snapdeal Border"
            )

    return list(set(invalid_border))



# SNAPDEAL TEMPLATE VALIDATION

def validate_snapdeal_template(sku_list):

    errors = {}


    # COLORS
    color_errors = validate_snapdeal_colors(sku_list)

    if color_errors:
        errors["Color"] = color_errors


    # BLOUSE COLORS
    blouse_color_errors = validate_snapdeal_blouse_colors(sku_list)

    if blouse_color_errors:
        errors["Blouse Color"] = blouse_color_errors



    # TECHNIQUE
    technique_errors = validate_snapdeal_technique(sku_list)

    if technique_errors:
        errors["Type"] = technique_errors


    # SAREE FABRIC
    saree_fabric_errors = validate_snapdeal_saree_fabric(sku_list)

    if saree_fabric_errors:
        errors["Saree Fabric"] = saree_fabric_errors



    # BLOUSE FABRIC
    blouse_fabric_errors = validate_snapdeal_blouse_fabric(sku_list)

    if blouse_fabric_errors:
        errors["Blouse Fabric"] = blouse_fabric_errors



    # BLOUSE
    blouse_errors = validate_snapdeal_blouse(sku_list)

    if blouse_errors:
        errors["Blouse"] = blouse_errors



    # PATTERN
    pattern_errors = validate_snapdeal_pattern(sku_list)

    if pattern_errors:
        errors["Pattern"] = pattern_errors


    # BLOUSE PATTERN
    blouse_pattern_errors = validate_snapdeal_blouse_pattern(sku_list)

    if blouse_pattern_errors:
        errors["Blouse Pattern"] = blouse_pattern_errors



    # PRINT OR PATTERN TYPE
    print_or_pattern_type_errors = validate_snapdeal_print_or_pattern_type(
        sku_list
    )

    if print_or_pattern_type_errors:
        errors["Print Or Pattern Type"] = print_or_pattern_type_errors



    # # ORNAMENTATION
    # ornamentation_errors = validate_snapdeal_ornamentation(sku_list)

    # if ornamentation_errors:
    #     errors["Ornamentation"] = ornamentation_errors



    # BORDER
    border_errors = validate_snapdeal_border(sku_list)

    if border_errors:
        errors["Border"] = border_errors



    return errors