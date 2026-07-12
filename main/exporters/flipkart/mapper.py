class FlipkartMapper:

    def __init__(self, sku):
        self.sku = sku

    def map(self):
        return {
            "product_id": self.sku.sku,
            "title": self.get_title(),
            "brand": self.get_brand(),
            "description": self.sku.style_description or "",
            "mrp": self.sku.mrp,
            "selling_price": self.sku.sale_price,
            "stock": getattr(self.sku, "inventory", 0),

            "color": self.get_color(),
            "fabric": self.get_fabric(),
            "pattern": self.get_pattern(),

            "image_1": self.sku.product_image_link_1,
            "image_2": self.sku.product_image_link_2,
            "image_3": self.sku.product_image_link_3,
            "image_4": self.sku.product_image_link_4,
        }

    def get_title(self):
        return f"{self.get_brand()} {self.get_color()} Saree"

    def get_brand(self):
        return self.sku.brand.name if self.sku.brand else ""

    def get_color(self):
        return self.sku.color.color if self.sku.color else ""

    def get_fabric(self):
        return self.sku.saree_fabric or ""

    def get_pattern(self):
        return self.sku.pattern or ""