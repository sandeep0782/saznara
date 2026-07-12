class FlipkartValidator:

    def validate(self, sku):
        errors = []

        # -------------------------
        # Core identity checks
        # -------------------------
        if not sku.sku:
            errors.append("SKU ID missing")

        if not sku.brand:
            errors.append("Brand missing")

        # -------------------------
        # Pricing rules
        # -------------------------
        if sku.mrp is None:
            errors.append("MRP missing")

        if sku.sale_price is None:
            errors.append("Selling price missing")

        if sku.mrp and sku.sale_price and sku.sale_price > sku.mrp:
            errors.append("Selling price cannot be greater than MRP")

        if sku.sale_price and sku.sale_price <= 0:
            errors.append("Selling price must be greater than 0")

        # -------------------------
        # Images (Flipkart is strict)
        # -------------------------
        if not sku.product_image_link_1:
            errors.append("At least Image 1 is required")

        # -------------------------
        # Category attributes (basic check)
        # -------------------------
        if not sku.color:
            errors.append("Color missing")

        if not sku.saree_fabric:
            errors.append("Fabric missing")

        # -------------------------
        # Optional but important checks
        # -------------------------
        if not sku.style_description:
            errors.append("Description missing")

        return errors