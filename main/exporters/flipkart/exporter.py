import openpyxl
from django.http import HttpResponse

from .validator import FlipkartValidator
from .mapper import FlipkartMapper
from ...models import SKU


class FlipkartExporter:

    def export(self):

        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Flipkart Export"

        skus = SKU.objects.select_related(
            "brand", "color", "size", "article_type"
        )

        headers = [
            "product_id", "title", "brand", "description",
            "mrp", "selling_price", "stock",
            "color", "fabric", "pattern",
            "image_1", "image_2", "image_3", "image_4"
        ]

        ws.append(headers)

        validator = FlipkartValidator()

        skipped_count = 0

        for sku in skus:

            errors = validator.validate(sku)

            # ❌ Skip invalid SKUs
            if errors:
                skipped_count += 1
                continue

            row = FlipkartMapper(sku).map()

            # safer than values() dependency
            ws.append([
                row.get("product_id", ""),
                row.get("title", ""),
                row.get("brand", ""),
                row.get("description", ""),
                row.get("mrp", ""),
                row.get("selling_price", ""),
                row.get("stock", ""),
                row.get("color", ""),
                row.get("fabric", ""),
                row.get("pattern", ""),
                row.get("image_1", ""),
                row.get("image_2", ""),
                row.get("image_3", ""),
                row.get("image_4", ""),
            ])

        response = HttpResponse(
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response["Content-Disposition"] = 'attachment; filename="flipkart.xlsx"'

        wb.save(response)

        print(f"Skipped SKUs due to validation errors: {skipped_count}")

        return response