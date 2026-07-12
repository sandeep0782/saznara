class MeeshoValidator:

    def validate(self, sku):
        errors = []

        if not sku.mrp:
            errors.append("MRP missing")

        if not sku.sale_price:
            errors.append("Sale price missing")

        if sku.sale_price and sku.mrp and sku.sale_price > sku.mrp:
            errors.append("Sale price greater than MRP")

        if not sku.product_image_link_1:
            errors.append("At least 1 image required")

        return errors