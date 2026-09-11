from celery import shared_task

from .models import SKU, SKUVideo


@shared_task
def generate_sku_video(sku_id):
    try:
        sku = SKU.objects.get(pk=sku_id)

        video, _ = SKUVideo.objects.get_or_create(sku=sku)

        video.status = "generating"
        video.error_message = None
        video.save(
            update_fields=[
                "status",
                "error_message",
                "updated_at",
            ]
        )

        # We will add Gemini/Veo generation here next.
        print(f"Starting video generation for SKU: {sku.sku}")

        return {
            "success": True,
            "sku_id": sku_id,
            "sku": sku.sku,
        }

    except SKU.DoesNotExist:
        return {
            "success": False,
            "error": f"SKU {sku_id} does not exist",
        }

    except Exception as e:
        try:
            video = SKUVideo.objects.get(sku_id=sku_id)
            video.status = "failed"
            video.error_message = str(e)
            video.save(
                update_fields=[
                    "status",
                    "error_message",
                    "updated_at",
                ]
            )
        except Exception:
            pass

        raise
