from decimal import Decimal
from .constants import HSN_DEFAULT, INVENTORY, WR_PRICE_DEDUCTION

class MeeshoMapper:

    def __init__(self, sku, profile):
        self.sku = sku
        self.profile = profile

    def map(self):
        return [
            "", "", "",

            self.get_product_name(),
            self.get_variation(),

            self.sku.sale_price or "",
            self.get_wr_price(),
            self.sku.mrp or "",

            5,
            HSN_DEFAULT,

            getattr(self.sku, "weight", 400),
            INVENTORY,

            "India",

            self.get_vendor_name(),
            self.get_vendor_address(),
            self.get_vendor_pin(),

            self.get_vendor_name(),
            self.get_vendor_address(),
            self.get_vendor_pin(),

            "Not Required", "Not Required", "Not Required",

            self.get_blouse(),
            self.get_border(),
            self.get_color(),

            self.get_generic(),
            "1",

            self.get_pattern_type(),
            self.get_saree_fabric(),
            self.get_transparency(),
            self.get_type(),

            float(self.sku.blouse_length or 0.8),
            float(self.sku.saree_length or 5.5),

            self.sku.product_image_link_1 or "",
            self.sku.product_image_link_2 or "",
            self.sku.product_image_link_3 or "",
            self.sku.product_image_link_4 or "",

            # self.sku.style_no or "",
            self.sku.sku or "",
            self.sku.sku or "",
            self.get_brand(),

            "",
            self.sku.style_description or "",

            self.get_blouse_color(),
            self.get_blouse_fabric(),
            self.get_blouse_pattern(),
            self.get_border_width(),

            self.get_brand(),
            self.get_loom(),
            self.get_occasion(),
            self.get_ornamentation(),
            self.get_pallu(),
            self.get_pattern(),
        ]

    # ---------------- helpers ----------------

    def get_product_name(self):
        parts = [
            self.get_brand(),
            self.get_generic(),
            self.get_color(),
        ]
        return " ".join([p for p in parts if p])

    def get_variation(self):
        return self.sku.size.size if self.sku.size else "FREE SIZE"

    def get_wr_price(self):
        if self.sku.sale_price:
            return float(self.sku.sale_price) - WR_PRICE_DEDUCTION
        return ""

    def get_brand(self):
        return self.sku.brand.name if self.sku.brand else ""

    def get_color(self):
        return self.sku.color.color if self.sku.color else ""

    def get_generic(self):
        return self.sku.article_type.name if self.sku.article_type else ""

    def get_vendor_name(self):
        return self.profile.company if self.profile else ""

    def get_vendor_address(self):
        return self.profile.address if self.profile else ""

    def get_vendor_pin(self):
        return self.profile.pin if self.profile else ""

    def get_blouse(self):
        return self.sku.get_blouse_display() if self.sku.blouse else ""

    def get_border(self):
        return self.sku.get_border_display() if self.sku.border else ""

    def get_pattern_type(self):
        return self.sku.get_print_or_pattern_type_display() if self.sku.print_or_pattern_type else ""

    def get_saree_fabric(self):
        return self.sku.get_saree_fabric_display() if self.sku.saree_fabric else ""

    def get_transparency(self):
        return self.sku.get_transparency_display() if self.sku.transparency else ""

    def get_type(self):
        return self.sku.get_type_display() if self.sku.type else ""

    def get_blouse_color(self):
        return self.sku.get_blouse_color_display() if self.sku.blouse_color else ""

    def get_blouse_fabric(self):
        return self.sku.get_blouse_fabric_display() if self.sku.blouse_fabric else ""

    def get_blouse_pattern(self):
        return self.sku.get_blouse_pattern_display() if self.sku.blouse_pattern else ""

    def get_border_width(self):
        return self.sku.get_border_width_display() if self.sku.border_width else ""

    def get_loom(self):
        return self.sku.get_loom_type_display() if self.sku.loom_type else ""

    def get_occasion(self):
        return self.sku.get_occasion_display() if self.sku.occasion else ""

    def get_ornamentation(self):
        return self.sku.get_ornamentation_display() if self.sku.ornamentation else ""

    def get_pallu(self):
        return self.sku.get_pallu_details_display() if self.sku.pallu_details else ""

    def get_pattern(self):
        return self.sku.get_pattern_display() if self.sku.pattern else ""