import os

from django.db import models
from django.core.files import File
from barcode.writer import ImageWriter
from io import BytesIO
from datetime import datetime
import barcode
import time






# Create your models here.

from django.db import models

from accounts.models import Profile


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True, blank=True)
    abb = models.CharField(max_length=2, unique=True, )

    def __str__(self):
        return self.name
    
class Article_Type(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True, blank=True)
    abb = models.CharField(max_length=2, unique=True,  null=True, blank=True)

    def __str__(self):
        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True, blank=True)
    short_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Gender(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True, blank=True)
    abb = models.CharField(max_length=1, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.name and len(self.name) >= 3:
            self.abb = self.name[0]  # 2nd and 4th characters (index 1 and 3)
        else:
            self.abb = None  # Or handle it as you need
        super(Gender, self).save(*args, **kwargs)
        

    def __str__(self):
        return self.name
    
class Size(models.Model):
    size = models.CharField(max_length=9, unique=True, null=True, blank=True)
    abb = models.CharField(max_length=100, null=True, blank=True)
    remarks = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.size)
    
class Color(models.Model):
    color = models.CharField(max_length=100, unique=True, null=True, blank=True)
    abb = models.CharField(max_length=3, null=True, blank=True)
 
    def __str__(self):
        return str(self.color)
    
DESIGN_PATTERN_CHOICES = [
    ("APPLIQUE", "Applique"),
    ("CHECKED", "Checked"),
    ("CHIKANKARI", "Chikankari"),
    ("COLORBLOCKED", "Colorblocked"),
    ("DIGITAL_PRINT", "Digital Print"),
    ("DYED_WASHED", "Dyed/ Washed"),
    ("EMBELLISHED", "Embellished"),
    ("EMBROIDERED", "Embroidered"),
    ("PRINTED", "Printed"),
    ("SELF_DESIGN", "Self-Design"),
    ("SOLID", "Solid"),
    ("STRIPED", "Striped"),
    ("WOVEN_DESIGN", "Woven Design"),
    ("ZARI_EMBROIDERED", "Zari Embroidered"),
    ("ZARI_WOVEN", "Zari Woven"),
]

PALLU_DETAILS_CHOICES = [
    ("colourblock", "Colourblock"),
    ("embellished", "Embellished"),
    ("embroidered", "Embroidered"),
    ("half_half", "Half & Half"),
    ("jacquard", "Jacquard"),
    ("printed", "Printed"),
    ("same_as_border", "Same as Border"),
    ("same_as_saree", "Same as Saree"),
    ("solid", "Solid"),
    ("woven_design", "Woven Design"),
    ("zari_woven", "Zari Woven"),
]
    
ORNAMENTATION_CHOICES = [
    ("aari_work", "Aari Work"),
    ("applique", "Applique"),
    ("beads_stones", "Beads & Stones"),
    ("brocade", "Brocade"),
    ("brooch", "Brooch"),
    ("cutwork", "Cutwork"),
    ("embroidered", "Embroidered"),
    ("frills", "Frills"),
    ("gota_work", "Gota Work"),
    ("jacquard", "Jacquard"),
    ("kundan", "Kundan"),
    ("lace_border", "Lace Border"),
    ("maggam_work", "Maggam Work"),
    ("mirror_work", "Mirror Work"),
    ("mukaish", "Mukaish"),
    ("not_applicable", "Not Applicable"),
    ("patchwork", "Patchwork"),
    ("pintucks", "Pintucks"),
    ("pom_pom", "Pom-Pom"),
    ("ruffle", "Ruffle"),
    ("sequinned", "Sequinned"),
    ("tassels_latkans", "Tassels and Latkans"),
    ("zardozi", "Zardozi"),
]

OCCASION_CHOICES = [
    ("bridal_saree", "Bridal Saree"),
    ("celebrity_inspired", "Celebrity Inspired"),
    ("daily", "Daily"),
    ("farewell", "Farewell"),
    ("party", "Party"),
    ("traditional", "Traditional"),
    ("wedding", "Wedding"),
    ("party_and_festive", "Party & Festive"),
]

LOOM_TYPE_CHOICES = [
    ("handloom", "Handloom"),
    ("powerloom", "Powerloom"),
]

BORDER_WIDTH_CHOICES = [
    ("big_border", "Big Border"),
    ("no", "No"),
    ("no_border", "No Border"),
    ("small_border", "Small Border"),
]

BLOUSE_PATTERN_CHOICES = [
    ("embellished", "Embellished"),
    ("embroidered", "Embroidered"),
    ("foil_printed", "Foil Printed"),
    ("jacquard", "Jacquard"),
    ("printed", "Printed"),
    ("same_as_border", "Same as Border"),
    ("same_as_pallu", "Same as Pallu"),
    ("same_as_saree", "Same as Saree"),
    ("sequence", "Sequence"),
    ("sequinned", "Sequinned"),
    ("solid", "Solid"),
    ("woven_design", "Woven Design"),
    ("zari_woven", "Zari Woven"),
]

BLOUSE_FABRIC_CHOICES = [
    ("acrylic", "Acrylic"),
    ("art_silk", "Art Silk"),
    ("bamboo", "Bamboo"),
    ("banarasi_silk", "Banarasi Silk"),
    ("bangalori_silk", "Bangalori Silk"),
    ("brocade", "Brocade"),
    ("chambray", "Chambray"),
    ("chanderi_cotton", "Chanderi Cotton"),
    ("chanderi_silk", "Chanderi Silk"),
    ("chiffon", "Chiffon"),
    ("cotton", "Cotton"),
    ("cotton_blend", "Cotton Blend"),
    ("cotton_cambric", "Cotton Cambric"),
    ("cotton_linen", "Cotton Linen"),
    ("cotton_silk", "Cotton Silk"),
    ("cotton_slub", "Cotton Slub"),
    ("crepe", "Crepe"),
    ("denim", "Denim"),
    ("dola_silk", "Dola Silk"),
    ("dupion_silk", "Dupion Silk"),
    ("eri_silk", "Eri Silk"),
    ("georgette", "Georgette"),
    ("italian_silk", "Italian Silk"),
    ("jacquard", "Jacquard"),
    ("jute_cotton", "Jute Cotton"),
    ("jute_khadi", "Jute Khadi"),
    ("jute_silk", "Jute Silk"),
    ("kanjeevaram_silk", "Kanjeevaram Silk"),
    ("khadi_cotton", "Khadi Cotton"),
    ("khadi_silk", "Khadi Silk"),
    ("khan", "Khan"),
    ("kora_muslin", "Kora Muslin"),
    ("kota_doria_cotton", "Kota Doria Cotton"),
    ("kota_doria_silk", "Kota Doria Silk"),
    ("lace", "Lace"),
    ("linen", "Linen"),
    ("linen_blend", "Linen Blend"),
    ("litchi_silk", "Litchi Silk"),
    ("lycra", "Lycra"),
    ("lycra_blend", "Lycra Blend"),
    ("malai_silk", "Malai Silk"),
    ("muga_silk", "Muga Silk"),
    ("mulberry_silk", "Mulberry Silk"),
    ("mulmul", "Mulmul"),
    ("muslin", "Muslin"),
    ("mysore_silk", "Mysore Silk"),
    ("net", "Net"),
    ("no_blouse", "No Blouse"),
    ("nylon", "Nylon"),
    ("organza", "Organza"),
    ("paper_silk", "Paper Silk"),
    ("pashmina", "Pashmina"),
    ("poly_blend", "Poly Blend"),
    ("poly_chiffon", "Poly Chiffon"),
    ("poly_crepe", "Poly Crepe"),
    ("poly_georgette", "Poly Georgette"),
    ("poly_silk", "Poly Silk"),
    ("polycotton", "Polycotton"),
    ("polyester", "Polyester"),
    ("rayon", "Rayon"),
    ("rayon_slub", "Rayon Slub"),
    ("sana_silk", "Sana Silk"),
    ("satin", "Satin"),
    ("satin_silk", "Satin Silk"),
    ("shantoon", "Shantoon"),
    ("silk", "Silk"),
    ("silk_blend", "Silk Blend"),
    ("soft_silk", "Soft Silk"),
    ("super_net", "Super Net"),
    ("suti", "Suti"),
    ("synthetic", "Synthetic"),
    ("synthetic_crepe", "Synthetic Crepe"),
    ("taant", "Taant"),
    ("taffeta_silk", "Taffeta Silk"),
    ("tissue", "Tissue"),
    ("tussar", "Tussar"),
    ("tussar_silk", "Tussar Silk"),
    ("twill_net", "Twill Net"),
    ("velvet", "Velvet"),
    ("vichitra_silk", "Vichitra Silk"),
    ("viscose", "Viscose"),
    ("viscose_rayon", "Viscose Rayon"),
    ("viscose_silk", "Viscose Silk"),
    ("voile", "Voile"),
    ("wool", "Wool"),
]

BLOUSE_COLOR_CHOICES = [
    ("aqua_blue", "Aqua Blue"),
    ("beige", "Beige"),
    ("black", "Black"),
    ("blue", "Blue"),
    ("brown", "Brown"),
    ("coral", "Coral"),
    ("cream", "Cream"),
    ("gold", "Gold"),
    ("green", "Green"),
    ("grey", "Grey"),
    ("grey_melange", "Grey Melange"),
    ("khaki", "Khaki"),
    ("lavender", "Lavender"),
    ("maroon", "Maroon"),
    ("mehendi", "Mehendi"),
    ("metallic", "Metallic"),
    ("multicolor", "Multicolor"),
    ("mustard", "Mustard"),
    ("navy_blue", "Navy Blue"),
    ("nude", "Nude"),
    ("olive", "Olive"),
    ("orange", "Orange"),
    ("peach", "Peach"),
    ("pink", "Pink"),
    ("purple", "Purple"),
    ("red", "Red"),
    ("rust", "Rust"),
    ("silver", "Silver"),
    ("teal", "Teal"),
    ("white", "White"),
    ("yellow", "Yellow"),
    ("dark_blue", "Dark Blue"),
    ("dark_green", "Dark Green"),
    ("light_blue", "Light Blue"),
    ("light_green", "Light Green"),
    ("magenta", "Magenta"),
]

SAREE_LENGTH_SIZE_CHOICES = [
    ("5", "5"),
    ("5.1", "5.1"),
    ("5.2", "5.2"),
    ("5.3", "5.3"),
    ("5.4", "5.4"),
    ("5.5", "5.5"),
    ("5.6", "5.6"),
    ("5.7", "5.7"),
    ("5.8", "5.8"),
    ("5.9", "5.9"),
    ("6", "6"),
    ("6.1", "6.1"),
    ("6.2", "6.2"),
    ("6.3", "6.3"),
    ("8", "8"),
    ("8.8", "8.8"),
    ("9", "9"),
    ("9.6", "9.6"),
]

BLOUSE_LENGTH_SIZE_CHOICES = [
    ("0.8", "0.8"),
    ("0.9", "0.9"),
    ("1", "1"),
    ("1.1", "1.1"),
    ("1.2", "1.2"),
]

TYPE_CHOICES = [
    ("assam_silk", "Assam Silk"),
    ("bagh", "Bagh"),
    ("balaton_silk", "Balaton Silk"),
    ("baluchari", "Baluchari"),
    ("banarasi", "Banarasi"),
    ("bandhani", "Bandhani"),
    ("bangalori_silk", "Bangalori Silk"),
    ("begumpuri", "Begumpuri"),
    ("belt_saree", "Belt Saree"),
    ("bhagalpuri", "Bhagalpuri"),
    ("bishnupuri", "Bishnupuri"),
    ("bollywood", "Bollywood"),
    ("bomkai_sonepuri", "Bomkai/Sonepuri"),
    ("brasso", "Brasso"),
    ("cape_saree", "Cape Saree"),
    ("chanderi", "Chanderi"),
    ("chettinad", "Chettinad"),
    ("chikankari", "Chikankari"),
    ("christian_bride", "Christian Bride"),
    ("cowdial_sarees", "Cowdial Sarees"),
    ("crush", "Crush"),
    ("darbari", "Darbari"),
    ("dhavani", "Dhavani"),
    ("dhoti_saree", "Dhoti Saree"),
    ("durga_puja_saree", "Durga Puja Saree"),
    ("gadhwal", "Gadhwal"),
    ("gadwal", "Gadwal"),
    ("garad", "Garad"),
    ("gharchola", "Gharchola"),
    ("hakoba", "Hakoba"),
    ("half_and_half", "Half and half"),
    ("hazar_buti", "Hazar Buti"),
    ("holographic_saree", "Holographic Saree"),
    ("ikat", "Ikat"),
    ("ilkal", "Ilkal"),
    ("irkal", "Irkal"),
    ("irkal_ilkal", "Irkal / Ilkal"),
    ("jacket_koti_saree", "Jacket/Koti Saree"),
    ("kaantha", "Kaantha"),
    ("kanjeevaram", "Kanjeevaram"),
    ("kasavu", "Kasavu"),
    ("kasavu_kerala_saree", "Kasavu (Kerala Saree)"),
    ("kashmiri", "Kashmiri"),
    ("katan", "Katan"),
    ("kathpadar", "Kathpadar"),
    ("khadi", "Khadi"),
    ("khan", "Khan"),
    ("khasi_jainsem_saree", "Khasi Jainsem Saree"),
    ("konrad_mubbhagam", "Konrad And Mubbhagam"),
    ("kota", "Kota"),
    ("kotki", "Kotki"),
    ("langa_voni", "Langa Voni"),
    ("lehenga_saree", "Lehenga Saree"),
    ("leheriya", "Leheriya"),
    ("maheshwari", "Maheshwari"),
    ("maheshwari_silk", "Maheshwari Silk"),
    ("mangalagiri", "Mangalagiri"),
    ("manipuri", "Manipuri"),
    ("marble", "Marble"),
    ("matka", "Matka"),
    ("mekhela_chador", "Mekhela chador"),
    ("metallic", "Metallic"),
    ("monochrome", "Monochrome"),
    ("muga_silk", "Muga Silk"),
    ("muggu", "Muggu"),
    ("mysore_silk", "Mysore Silk"),
    ("narayan_peth", "Narayan Peth"),
    ("nauvari", "Nauvari"),
    ("no_type", "No Type"),
    ("paithani", "Paithani"),
    ("palazzo_saree", "Palazzo Saree"),
    ("panetar", "Panetar"),
    ("pasapalli", "Pasapalli"),
    ("patola", "Patola"),
    ("pochampally", "Pochampally"),
    ("ready_to_wear", "Ready to Wear"),
    ("ruffle_saree", "Ruffle Saree"),
    ("sambhalpuri", "Sambhalpuri"),
    ("sana_silk", "Sana Silk"),
    ("shaded", "Shaded"),
    ("shimmer", "Shimmer"),
    ("sungudi", "Sungudi"),
    ("swastik", "Swastik"),
    ("taant", "Taant"),
    ("tangail", "Tangail"),
    ("tripura_silk", "Tripura Silk"),
    ("tussar", "Tussar"),
    ("two_tone", "Two-Tone"),
    ("upada_pattu", "Upada Pattu"),
    ("venkatgiri", "Venkatgiri"),
    ("jamdani", "Jamdani"),
]

TRANSPARENCY_CHOICES = [
    ("no", "No"),
    ("yes", "Yes"),
]

SAREE_FABRIC_CHOICES = [
    ("acrylic", "Acrylic"),
    ("art_silk", "Art Silk"),
    ("aura_silk", "Aura Silk"),
    ("bamboo", "Bamboo"),
    ("banarasi_silk", "Banarasi Silk"),
    ("binny_silk", "Binny Silk"),
    ("brocade", "Brocade"),
    ("chambray", "Chambray"),
    ("chanderi_cotton", "Chanderi Cotton"),
    ("chanderi_silk", "Chanderi Silk"),
    ("chiffon", "Chiffon"),
    ("chinnon", "Chinnon"),
    ("cotton", "Cotton"),
    ("cotton_blend", "Cotton Blend"),
    ("cotton_cambric", "Cotton Cambric"),
    ("cotton_linen", "Cotton Linen"),
    ("cotton_silk", "Cotton Silk"),
    ("cotton_slub", "Cotton Slub"),
    ("crepe", "Crepe"),
    ("denim", "Denim"),
    ("dola_silk", "Dola Silk"),
    ("dupion_silk", "Dupion Silk"),
    ("eri_silk", "Eri Silk"),
    ("georgette", "Georgette"),
    ("italian_silk", "Italian Silk"),
    ("jacquard", "Jacquard"),
    ("jimmy_choo", "Jimmy Choo"),
    ("jute_cotton", "Jute Cotton"),
    ("jute_khadi", "Jute Khadi"),
    ("jute_silk", "Jute Silk"),
    ("kanchi_silk", "Kanchi Silk"),
    ("kanjeevaram_silk", "Kanjeevaram Silk"),
    ("khadi_cotton", "Khadi Cotton"),
    ("khadi_silk", "Khadi Silk"),
    ("khan", "Khan"),
    ("kora_muslin", "Kora Muslin"),
    ("kota_doria_cotton", "Kota Doria Cotton"),
    ("kota_doria_silk", "Kota Doria Silk"),
    ("lace", "Lace"),
    ("linen", "Linen"),
    ("linen_blend", "Linen Blend"),
    ("litchi_silk", "Litchi Silk"),
    ("lycra", "Lycra"),
    ("lycra_blend", "Lycra Blend"),
    ("malai_cotton", "Malai Cotton"),
    ("malai_silk", "Malai Silk"),
    ("muga_silk", "Muga Silk"),
    ("mulberry_silk", "Mulberry Silk"),
    ("mulmul", "Mulmul"),
    ("murshidabad_silk", "Murshidabad Silk"),
    ("muslin", "Muslin"),
    ("mysore_silk", "Mysore Silk"),
    ("net", "Net"),
    ("net_soft_net", "Net (Soft Net)"),
    ("net_supernet", "Net (Supernet)"),
    ("nylon", "Nylon"),
    ("organza", "Organza"),
    ("paper_silk", "Paper Silk"),
    ("pashmina", "Pashmina"),
    ("poly_blend", "Poly Blend"),
    ("poly_chiffon", "Poly Chiffon"),
    ("poly_crepe", "Poly Crepe"),
    ("poly_georgette", "Poly Georgette"),
    ("poly_silk", "Poly Silk"),
    ("polycotton", "Polycotton"),
    ("polyester", "Polyester"),
    ("rayon", "Rayon"),
    ("rayon_slub", "Rayon Slub"),
    ("sana_silk", "Sana Silk"),
    ("satin", "Satin"),
    ("satin_silk", "Satin Silk"),
    ("shantoon", "Shantoon"),
    ("silk", "Silk"),
    ("silk_blend", "Silk Blend"),
    ("simmer", "Simmer"),
    ("soft_silk", "Soft Silk"),
    ("super_net", "Super Net"),
    ("suti", "Suti"),
    ("synthetic", "Synthetic"),
    ("synthetic_crepe", "Synthetic Crepe"),
    ("taant", "Taant"),
    ("taffeta_silk", "Taffeta Silk"),
    ("tanchoi_silk", "Tanchoi Silk"),
    ("tissue", "Tissue"),
    ("tripura_silk", "Tripura Silk"),
    ("tussar", "Tussar"),
    ("tussar_silk", "Tussar Silk"),
    ("twill_net", "Twill Net"),
    ("vayal", "Vayal"),
    ("velvet", "Velvet"),
    ("vichitra_silk", "Vichitra Silk"),
    ("viscose", "Viscose"),
    ("viscose_rayon", "Viscose Rayon"),
    ("viscose_silk", "Viscose Silk"),
    ("voile", "Voile"),
    ("wool", "Wool"),
    ("zamato", "Zamato"),
]

PRINT_PATTERN_TYPE_CHOICES = [
    ("abstract", "Abstract"),
    ("ajrakh", "Ajrakh"),
    ("animal", "Animal"),
    ("applique", "Applique"),
    ("aztec", "Aztec"),
    ("bagru_print", "Bagru Print"),
    ("bandhani", "Bandhani"),
    ("batik", "Batik"),
    ("block", "Block"),
    ("bohemian", "Bohemian"),
    ("boho_saree", "Boho Saree"),
    ("botanical", "Botanical"),
    ("butterfly", "Butterfly"),
    ("checked", "Checked"),
    ("chevron", "Chevron"),
    ("colorblocked", "Colorblocked"),
    ("elephant", "Elephant"),
    ("embellished", "Embellished"),
    ("ethnic_motif", "Ethnic Motif"),
    ("floral", "Floral"),
    ("foil", "Foil"),
    ("geometric", "Geometric"),
    ("gradient", "Gradient"),
    ("graphic", "Graphic"),
    ("hand_painted", "Hand Painted"),
    ("herringbone", "Herringbone"),
    ("houndstooth", "Houndstooth"),
    ("ikat", "Ikat"),
    ("kalamkari", "Kalamkari"),
    ("leheriya", "Leheriya"),
    ("leopard", "Leopard"),
    ("madhubani", "Madhubani"),
    ("micro", "Micro"),
    ("moti_work", "Moti Work"),
    ("nath", "Nath"),
    ("newspaper_print", "Newspaper Print"),
    ("paisley", "Paisley"),
    ("peacock", "Peacock"),
    ("phulkari", "Phulkari"),
    ("polka_dot", "Polka Dot"),
    ("quirky", "Quirky"),
    ("ribbon", "Ribbon"),
    ("scenic", "Scenic"),
    ("shibori", "Shibori"),
    ("solid", "Solid"),
    ("stripe", "Stripe"),
    ("tie_and_dye", "Tie and Dye"),
    ("tiger", "Tiger"),
    ("tribal", "Tribal"),
    ("warli", "Warli"),
    ("woven_design", "Woven Design"),
    ("zari_woven", "Zari Woven"),
    ("zari_butta", "Zari Butta"),
    ("zebra", "Zebra"),
]

BORDER_CHOICES = [
    ("embellished", "Embellished"),
    ("embroidered", "Embroidered"),
    ("lace", "Lace"),
    ("no_border", "No Border"),
    ("printed", "Printed"),
    ("solid", "Solid"),
    ("temple_border", "Temple Border"),
    ("woven_design", "Woven Design"),
    ("zari", "Zari"),
]

BLOUSE_CHOICES = [
    ("running_blouse", "Running Blouse"),
    ("saree_with_multiple_blouse", "Saree with Multiple Blouse"),
    ("semi_stitched_blouse", "Semi-Stitched Blouse"),
    ("separate_blouse_piece", "Separate Blouse Piece"),
    ("stitched_blouse", "Stitched Blouse"),
    ("without_blouse", "Without Blouse"),
]

class SKU(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Profile, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    article_type = models.ForeignKey('Article_Type', on_delete=models.CASCADE)
    style_no = models.CharField(max_length=4, null=True, blank=True)
    style_description = models.CharField(max_length=500, null=True, blank=True)
    style_id = models.CharField(max_length=8, null=True, blank=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    ref_no = models.CharField(max_length=40, null=True, blank=True)
    hsn = models.CharField(max_length=8, null=True, blank=True)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    mrp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    van = models.CharField(max_length=20, null=True, blank=True)   
    sku = models.CharField(max_length=18, unique=True, null=True, blank=True)
    old_sku = models.CharField(max_length=30, null=True, blank=True)
    ean = models.CharField(max_length=20, null=True, blank=True)
    product_image_link_1 = models.URLField(null=True, blank=True)
    product_image_link_2 = models.URLField(null=True, blank=True)
    product_image_link_3 = models.URLField(null=True, blank=True)
    product_image_link_4 = models.URLField(null=True, blank=True)
    product_image_link_5 = models.URLField(null=True, blank=True)
    barcode_image = models.ImageField(upload_to='barcode_image/', null=True, blank=True)
    live_status = models.BooleanField(default=False)
    image_urls = models.JSONField(default=list, null=True, blank=True)  
    blouse = models.CharField( max_length=50, choices=BLOUSE_CHOICES, null=True, blank=True)
    border = models.CharField( max_length=50, choices=BORDER_CHOICES, null=True, blank=True)
    print_or_pattern_type = models.CharField( max_length=50, choices=PRINT_PATTERN_TYPE_CHOICES, null=True, blank=True)
    saree_fabric = models.CharField( max_length=50, choices=SAREE_FABRIC_CHOICES, null=True, blank=True)
    transparency = models.CharField( max_length=50, choices=TRANSPARENCY_CHOICES, null=True, blank=True)
    type = models.CharField( max_length=50, choices=TYPE_CHOICES, null=True, blank=True)
    blouse_length = models.CharField( max_length=50, choices=BLOUSE_LENGTH_SIZE_CHOICES, null=True, blank=True)
    saree_length = models.CharField( max_length=50, choices=SAREE_LENGTH_SIZE_CHOICES, null=True, blank=True)
    blouse_color = models.CharField( max_length=50, choices=BLOUSE_COLOR_CHOICES, null=True, blank=True)
    blouse_fabric = models.CharField( max_length=50, choices=BLOUSE_FABRIC_CHOICES, null=True, blank=True)
    blouse_pattern = models.CharField( max_length=50, choices=BLOUSE_PATTERN_CHOICES, null=True, blank=True)
    border_width = models.CharField( max_length=50, choices=BORDER_WIDTH_CHOICES, null=True, blank=True)
    loom_type = models.CharField( max_length=50, choices=LOOM_TYPE_CHOICES, null=True, blank=True)
    occasion = models.CharField( max_length=50, choices=OCCASION_CHOICES, null=True, blank=True)
    ornamentation = models.CharField( max_length=50, choices=ORNAMENTATION_CHOICES, null=True, blank=True)
    pallu_details = models.CharField( max_length=50, choices=PALLU_DETAILS_CHOICES, null=True, blank=True)
    pattern = models.CharField( max_length=50, choices=DESIGN_PATTERN_CHOICES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.sku)
        
    def save(self, *args, **kwargs):

        # Style No
        if self.style_no:
            self.style_no = str(self.style_no).zfill(4)
        else:
            self.style_no = "0000"

        # ===========================
        # Generate SKU
        # ===========================
        generated_sku = (
            f"{self.ref_no}-"
            f"{self.color}"
        )

        # Check duplicate SKU (excluding current record)
        sku_value = generated_sku
        while SKU.objects.exclude(pk=self.pk).filter(sku=sku_value).exists():
            sku_value = f"{generated_sku}-{int(time.time())}"

        self.sku = sku_value

        # ===========================
        # Generate VAN
        # ===========================
        self.van = (
            f"{self.ref_no}-"
            f"{self.color}"
        )

        # ===========================
        # Generate EAN
        # ===========================
        self.ean = (
           f"{self.brand.abb}-"
            f"{self.ref_no}-"
            f"{self.color}"
        )

        # ===========================
        # Barcode
        # ===========================
        old_instance = None
        if self.pk:
            old_instance = SKU.objects.filter(pk=self.pk).first()

        if (
            not self.barcode_image
            or not old_instance
            or old_instance.ean != self.ean
        ):
            self.generate_barcode()

        super().save(*args, **kwargs)


    def generate_barcode(self):
        """Generate and save barcode image based on the SKU."""
        if self.ean:  # Ensure SKU exists
            # Generate barcode using the 'code128' format with added margin for quiet zone
            code128 = barcode.get('code128', self.ean, writer=ImageWriter())
            
            # Set options for margin (quiet zone) and image size
            options = {
                'module_width': 0.2,     # Width of the barcode bars (higher = thicker bars)
                'module_height': 10,     # Height of the barcode (adjust to ensure readability)
                'font_size': 10,         # Font size of the text below the barcode (optional)
                'text_distance': 5,      # Distance between the barcode and the text
                'quiet_zone': 0,        # Quiet zone (space around the barcode, set to 10)
            }

            # Create a buffer to hold the barcode image
            buffer = BytesIO()

            # Write barcode to buffer with options
            code128.write(buffer, options)

            # If a barcode image exists, delete it before saving a new one
            if self.barcode_image and os.path.isfile(self.barcode_image.path):
                os.remove(self.barcode_image.path)

            # Save the new barcode image
            buffer.seek(0)
            self.barcode_image.save(f'{self.ean}.png', File(buffer), save=False)


