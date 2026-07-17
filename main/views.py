from .models import BLOUSE_CHOICES, BLOUSE_COLOR_CHOICES, BLOUSE_FABRIC_CHOICES, BLOUSE_LENGTH_SIZE_CHOICES, BLOUSE_PATTERN_CHOICES, BORDER_CHOICES, BORDER_WIDTH_CHOICES, DESIGN_PATTERN_CHOICES, LOOM_TYPE_CHOICES, OCCASION_CHOICES, ORNAMENTATION_CHOICES, PALLU_DETAILS_CHOICES, PRINT_PATTERN_TYPE_CHOICES, SAREE_FABRIC_CHOICES, SAREE_LENGTH_SIZE_CHOICES, SKU, TRANSPARENCY_CHOICES, TYPE_CHOICES, VMS
from main.utils.mappings import FLIPKART_COLOR_MAPPING, FLIPKART_OCCASION_MAPPING, MEESHO_COLOR_MAPPING, MEESHO_OCCASION_MAPPING, SNAPDEAL_COLOR_MAPPING, SNAPDEAL_SET_CONTENTS_MAPPING
from main.forms import ATForm, BrandForm, ColorForm, GenderForm, SKUForm, SizeForm, UnitForm
from accounts.decorators import unauthenticated_user, allowed_users, admin_only
from main.models import SKU, Article_Type, Brand, Color, Gender, Size, Unit
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from datetime import datetime, time as dtime, timedelta
from django.db.models import Sum, Max, Q, Count, Min
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib import messages
from accounts.models import Profile
from django.db import transaction
from decimal import Decimal
from copy import copy
from .utils import *
import openpyxl
import re





# Create your views here.
@login_required
def home(request):

    return render(request, 'index.html')

@login_required
def View__Brand(request):
    search_query = request.GET.get('search', '').strip()
    brand_list = Brand.objects.all().order_by('-id')
    if search_query:
        brand_list = brand_list.filter(name=search_query)

    paginator = Paginator(brand_list, 10)  # Show 10 products per page
    page = request.GET.get('page')
    try:
        brand = paginator.page(page)
    except PageNotAnInteger:
        brand = paginator.page(1)
    except EmptyPage:
        brand = paginator.page(paginator.num_pages)
    d = {'brand': brand, 'search_query':search_query}
    return render(request, 'bag/brand/view_brand.html', d)

@login_required
def Change__Brand(request, id=None):
    brand = None
    if id:
        try:
            brand = Brand.objects.get(id=id)
        except Brand.DoesNotExist:
            messages.info(request, 'Brand does not exist')
            return redirect('view_brand')
    if request.method == "POST":
        form = BrandForm(request.POST, request.FILES, instance=brand)
        if form.is_valid():
            pro = form.save(commit=False)  # Don't save yet to modify additional fields
            if id:
                pro.modified_by = request.user  # Set the user who modified the SKU
                messages.info(request, 'Brand modified successfully')
            else:
                pro.created_by = request.user  # Set the user who created the SKU
                messages.info(request, 'Brand added successfully')
            pro.save()  # Now save the SKU with all fields
            return redirect('view_brand')
        else:
            messages.info(request, form.errors)
    d = { 'brand': brand }
    return render(request, 'bag/brand/change_brand.html', d)

@login_required
def Delete__Brand(request, id):
    brand = Brand.objects.filter(id=id)
    brand.delete()
    return redirect('view_brand')

@login_required
def View__Article__Type(request):
    search_query = request.GET.get('search', '').strip()
    at_list = Article_Type.objects.all().order_by('-id')
    if search_query:
        at_list = at_list.filter(name=search_query)

    paginator = Paginator(at_list, 10)  # Show 10 products per page
    page = request.GET.get('page')
    try:
        at = paginator.page(page)
    except PageNotAnInteger:
        at = paginator.page(1)
    except EmptyPage:
        at = paginator.page(paginator.num_pages)
    d = {'at': at, 'search_query':search_query}  # Pass the search query to the template
    return render(request, 'bag/at/view_article_type.html', d)

@login_required
def Change__Article__Type(request, id=None):
    at = None
    if id:
        try:
            at = Article_Type.objects.get(id=id)
        except Article_Type.DoesNotExist:
            messages.info(request, 'Article Type does not exist')
            return redirect('view_article_type')
    
    if request.method == "POST":
        form = ATForm(request.POST, request.FILES, instance=at)
        if form.is_valid():
            pro = form.save(commit=False)  # Don't save yet to modify additional fields
            if id:
                pro.modified_by = request.user  # Set the user who modified the SKU
                messages.info(request, 'Article Type modified successfully')
            else:
                pro.created_by = request.user  # Set the user who created the SKU
                messages.info(request, 'Article Type added successfully')
            pro.save()  # Now save the SKU with all fields
            return redirect('view_article_type')
        else:
            messages.info(request, form.errors)
    d = { 'at': at }
    return render(request, 'bag/at/change_article_type.html', d)

@login_required
def Delete__Article__Type(request, id):
    at = Article_Type.objects.filter(id=id)
    at.delete()
    return redirect('view_article_type')

@login_required
def View__Gender(request):
    gender = Gender.objects.all().order_by('-id')
    d = {'gender': gender}  # Pass the search query to the template
    return render(request, 'bag/gender/view_gender.html', d)

@login_required
def Change__Gender(request, id=None):
    gender = None
    if id:
        try:
            gender = Gender.objects.get(id=id)
        except Gender.DoesNotExist:
            messages.info(request, 'Gender Type does not exist')
            return redirect('view_gender')
    
    if request.method == "POST":
        form = GenderForm(request.POST, request.FILES, instance=gender)
        if form.is_valid():
            pro = form.save(commit=False)  # Don't save yet to modify additional fields
            if id:
                pro.modified_by = request.user  # Set the user who modified the SKU
                messages.info(request, 'Gender modified successfully')
            else:
                pro.created_by = request.user  # Set the user who created the SKU
                messages.info(request, 'Gender added successfully')
            pro.save()  # Now save the SKU with all fields
            return redirect('view_gender')
        else:
            messages.info(request, form.errors)
    d = { 'gender': gender }
    return render(request, 'bag/gender/change_gender.html', d)

@login_required
def Delete__Gender(request, id):
    gender = Gender.objects.filter(id=id)
    gender.delete()
    return redirect('view_gender')

@login_required
def View__Size(request):
    search_query = request.GET.get('search', '').strip()
    size_list = Size.objects.all().order_by('-id')
    if search_query:
        size_list = size_list.filter(Q(size=search_query)|Q(abb=search_query))

    paginator = Paginator(size_list, 10)  # Show 10 products per page
    page = request.GET.get('page')
    try:
        size = paginator.page(page)
    except PageNotAnInteger:
        size = paginator.page(1)
    except EmptyPage:
        size = paginator.page(paginator.num_pages)
    d = {'size': size, 'search_query':search_query}  # Pass the search query to the template
    return render(request, 'bag/size/view_size.html', d)

@login_required
def Change__Size(request, id=None):
    size = None
    if id:
        try:
            size = Size.objects.get(id=id)
        except Size.DoesNotExist:
            messages.info(request, 'Size Type does not exist')
            return redirect('view_size')
    
    if request.method == "POST":
        form = SizeForm(request.POST, request.FILES, instance=size)
        if form.is_valid():
            pro = form.save(commit=False)  # Don't save yet to modify additional fields
            if id:
                pro.modified_by = request.user  # Set the user who modified the SKU
                messages.info(request, 'Size modified successfully')
            else:
                pro.created_by = request.user  # Set the user who created the SKU
                messages.info(request, 'Size added successfully')
            pro.save()  # Now save the SKU with all fields
            return redirect('view_size')
        else:
            messages.info(request, form.errors)
    d = { 'size': size }
    return render(request, 'bag/size/change_size.html', d)

@login_required
def Delete__Size(request, id):
    size = Size.objects.filter(id=id)
    size.delete()
    return redirect('view_size')

@login_required
def View__UOM(request):
    uom = Unit.objects.all().order_by('-id')
    d = {'uom': uom}  # Pass the search query to the template
    return render(request, 'bag/uom/view_uom.html', d)


@login_required
def Change__UOM(request, id=None):
    uom = None
    if id:
        try:
            uom = Unit.objects.get(id=id)
        except Unit.DoesNotExist:
            messages.info(request, 'Unit Type does not exist')
            return redirect('view_uom')
    
    if request.method == "POST":
        form = UnitForm(request.POST, request.FILES, instance=uom)
        if form.is_valid():
            pro = form.save(commit=False)  # Don't save yet to modify additional fields
            if id:
                pro.modified_by = request.user  # Set the user who modified the SKU
                messages.info(request, 'Unit modified successfully')
            else:
                pro.created_by = request.user  # Set the user who created the SKU
                messages.info(request, 'Unit added successfully')
            pro.save()  # Now save the SKU with all fields
            return redirect('view_uom')
        else:
            messages.info(request, form.errors)
    d = { 'uom': uom }
    return render(request, 'bag/uom/change_uom.html', d)


@login_required
def Delete__UOM(request, id):
    uom = Unit.objects.filter(id=id)
    uom.delete()
    return redirect('view_uom')


@login_required
def View__Color(request):
    search_query = request.GET.get('search', '').strip()
    color_list = Color.objects.all().order_by('-id')
    if search_query:
        color_list = color_list.filter(color=search_query)

    paginator = Paginator(color_list, 10)  # Show 10 products per page
    page = request.GET.get('page')
    try:
        color = paginator.page(page)
    except PageNotAnInteger:
        color = paginator.page(1)
    except EmptyPage:
        color = paginator.page(paginator.num_pages)
    d = {'color': color, 'search_query':search_query}  # Pass the search query to the template
    return render(request, 'bag/color/view_color.html', d)


@login_required
def Change__Color(request, id=None):
    color = None
    if id:
        try:
            color = Color.objects.get(id=id)
        except Color.DoesNotExist:
            messages.info(request, 'Color Type does not exist')
            return redirect('view_color')
    
    if request.method == "POST":
        form = ColorForm(request.POST, request.FILES, instance=color)
        if form.is_valid():
            pro = form.save(commit=False)  # Don't save yet to modify additional fields
            if id:
                pro.modified_by = request.user  # Set the user who modified the SKU
                messages.info(request, 'Color modified successfully')
            else:
                pro.created_by = request.user  # Set the user who created the SKU
                messages.info(request, 'Color added successfully')
            pro.save()  # Now save the SKU with all fields
            return redirect('view_color')
        else:
            messages.info(request, form.errors)
    d = { 'color': color }
    return render(request, 'bag/color/change_color.html', d)


@login_required
def Delete__Color(request, id):
    c = Color.objects.filter(id=id)
    c.delete()
    return redirect('view_color')

def get_filtered_skus(request):
    search_query = request.GET.get('search', '').strip()

    sku_list = SKU.objects.all().order_by('-id')

    if search_query:
        search_terms = search_query.split('%')

        for term in search_terms:
            term = term.strip()
            if term:
                sku_list = sku_list.filter(
                    Q(ref_no__icontains=term) |
                    Q(vendor__company__icontains=term) |
                    Q(sku__icontains=term) |
                    Q(brand__name__icontains=term) |
                    Q(style_no__icontains=term) |
                    Q(color__color__icontains=term) |
                    Q(article_type__name__icontains=term)
                )

    return sku_list, search_query
    

@login_required(login_url='login')
def View__SKU(request):

    # 🔹 GET PARAMETERS (ALL TOGETHER HERE)
    search_query = request.GET.get('search', '').strip()
    export = request.GET.get('export')   # ✅ ADD HERE

    # 🔹 BASE QUERYSET
    sku_list = SKU.objects.all().order_by('-id')

    # 🔹 FILTERING
    if search_query:
        search_terms = search_query.split('%')

        for term in search_terms:
            term = term.strip()
            if term:
                sku_list = sku_list.filter(
                    Q(ref_no__icontains=term) |
                    Q(vendor__company__icontains=term) |
                    Q(sku__icontains=term) |
                    Q(brand__name__icontains=term) |
                    Q(style_no__icontains=term) |
                    Q(color__color__icontains=term) |
                    Q(article_type__name__icontains=term)
                )

    # 🔥 EXPORT CHECK (OPTIONAL: if export happens, return early)
    if export == "meesho":
        return Meesho_Template(request, sku_list)

    if export == "flipkart":
        return Flipkart_Template(request, sku_list)
    
    if export == "snapdeal":
        return Snapdeal_Template(request, sku_list)

    # 🔹 PAGINATION (ONLY FOR NORMAL VIEW)
    paginator = Paginator(sku_list, 10)
    page = request.GET.get('page')

    try:
        sku = paginator.page(page)
    except PageNotAnInteger:
        sku = paginator.page(1)
    except EmptyPage:
        sku = paginator.page(paginator.num_pages)

    return render(request, 'sku/view_sku.html', {
        'sku': sku,
        'search_query': search_query
    })

@login_required
def Change__SKU(request, pid=None):
    sku = None

    brand = Brand.objects.all()
    gender = Gender.objects.all()
    article_type = Article_Type.objects.all()
    size = Size.objects.all()
    color = Color.objects.all()
    vendor = Profile.objects.all()
   

    selected_gender = Gender.objects.filter(name="WOMENS").first()
    selected_article_type = Article_Type.objects.filter(name="SAREE").first()
    selected_size = Size.objects.filter(size="Free Size").first()
    

    if pid:
        sku = SKU.objects.filter(id=pid).first()
        if not sku:
            messages.error(request, "SKU does not exist")
            return redirect('view_sku')

    if request.method == "POST":
        form = SKUForm(request.POST, request.FILES, instance=sku)

        if form.is_valid():
            obj = form.save(commit=False)

            if pid:
                obj.modified_by = request.user
                messages.success(request, "SKU updated successfully")
            else:
                obj.created_by = request.user
                obj.gender = selected_gender
                obj.article_type = selected_article_type
                obj.size = selected_size
                messages.success(request, "SKU created successfully")

            obj.save()
            return redirect('view_sku')

        else:
            # IMPORTANT: return form WITH ERRORS
            messages.error(request, "Please correct the errors below")
    else:
        form = SKUForm(instance=sku)

    context = {
        'form': form,
        'sku': sku,
        'brand': brand,
        'gender': gender,
        'article_type': article_type,
        'size': size,
        'color': color,
        'vendor': vendor,
        "BLOUSE_CHOICES":BLOUSE_CHOICES, "BORDER_CHOICES":BORDER_CHOICES, "PRINT_PATTERN_TYPE_CHOICES":PRINT_PATTERN_TYPE_CHOICES, 'SAREE_FABRIC_CHOICES':SAREE_FABRIC_CHOICES,
        "TRANSPARENCY_CHOICES":TRANSPARENCY_CHOICES, 'TYPE_CHOICES':TYPE_CHOICES, 'BLOUSE_LENGTH_SIZE_CHOICES':BLOUSE_LENGTH_SIZE_CHOICES, 'SAREE_LENGTH_SIZE_CHOICES':SAREE_LENGTH_SIZE_CHOICES,
        'BLOUSE_COLOR_CHOICES':BLOUSE_COLOR_CHOICES, 'BLOUSE_FABRIC_CHOICES':BLOUSE_FABRIC_CHOICES, 'BLOUSE_PATTERN_CHOICES':BLOUSE_PATTERN_CHOICES, 'BORDER_WIDTH_CHOICES':BORDER_WIDTH_CHOICES,
        'LOOM_TYPE_CHOICES':LOOM_TYPE_CHOICES, 'OCCASION_CHOICES':OCCASION_CHOICES,'ORNAMENTATION_CHOICES':ORNAMENTATION_CHOICES, 'PALLU_DETAILS_CHOICES':PALLU_DETAILS_CHOICES,'DESIGN_PATTERN_CHOICES':DESIGN_PATTERN_CHOICES,
    }

    return render(request, 'sku/change_sku.html', context)

@login_required
def Delete__SKU(request, pid):
    sku = SKU.objects.get(id=pid)  # Fetch the SKU object
    sku.delete()
    return redirect('view_sku')

@login_required
def Print__SKU(request, pid):
    sku = SKU.objects.get(id=pid)  # Fetch the SKU object
    if len(sku.sku) < 18:
        messages.warning(request, 'SKU code is not in a proper format, hence barcode cannot be printed')
        return redirect('view_sku')
    
    if sku.brand.name == "SUHA":
        return render(request, 'sku/print_suha.html', {'sku': sku})
    elif sku.brand.name == "NYRIKA" or sku.brand.name == "INDIE PICKS" or sku.brand.name == "FYREROSE" or sku.brand.name == "BUDA JEANS" or sku.brand.name == "SVARAA":
        return render(request, 'sku/print_ajio.html', {'sku': sku})
    else:
        return render(request, 'sku/print_myntra.html', {'sku': sku})
        
@login_required
def Print__Barcode(request, pid):
    sku = SKU.objects.get(id=pid)  # Fetch the SKU object
    if len(sku.sku) < 18:
        messages.warning(request, 'SKU code is not in a proper format, hence barcode cannot be printed')
        return redirect('view_sku')
    return render(request, 'sku/print_barcode.html', {'sku': sku})


@login_required
def Copy__SKU(request, pid=None):

    if not pid:
        messages.error(request, "No SKU ID provided.")
        return redirect("view_sku")

    try:
        sku = SKU.objects.get(id=pid)
    except SKU.DoesNotExist:
        messages.error(request, "SKU does not exist.")
        return redirect("view_sku")

    with transaction.atomic():

        # Get all SKUs of the same vendor
        skus = SKU.objects.filter(vendor=sku.vendor)

        max_number = 0
        prefix = ""
        width = 4

        for s in skus:
            style = str(s.style_no or "")
            match = re.search(r"([A-Za-z]*)(\d+)$", style)

            if match:
                prefix = match.group(1)
                number = int(match.group(2))
                width = len(match.group(2))

                if number > max_number:
                    max_number = number

        # Generate next style number
        new_style_no = f"{prefix}{str(max_number + 1).zfill(width)}"

        # Clone the SKU
        new_sku = copy(sku)
        new_sku.pk = None
        new_sku.id = None

        # Set new style number
        new_sku.style_no = new_style_no

        # Save (your save() method will generate SKU, VAN, EAN, Barcode)
        new_sku.save()

    messages.success(
        request,
        f"SKU copied successfully with Style No {new_style_no}"
    )

    return redirect("view_sku")

@login_required
def Meesho_Template(request, sku_list):
    sku_list, _ = get_filtered_skus(request)

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Meesho Saree Template"

    # =========================================================
    # HEADERS
    # =========================================================
    headers = [
        "Fields + Description:",
        "ERROR STATUS",
        "ERROR MESSAGE",
        "Product Name",
        "Variation",
        "Meesho Price",
        "Wrong/Defective Returns Price",
        "MRP",
        "GST %",
        "HSN ID",
        "Net Weight (gms)",
        "Inventory",
        "Country of Origin",
        "Manufacturer Name",
        "Manufacturer Address",
        "Manufacturer Pincode",
        "Packer Name",
        "Packer Address",
        "Packer Pincode",
        "Importer Name",
        "Importer Address",
        "Importer Pincode",

        "Blouse",
        "Border",
        "Color",
        "Generic Name",
        "Net Quantity (N)",
        "Print or Pattern Type",
        "Saree Fabric",
        "Transparency",
        "Type",
        "Blouse Length Size",
        "Saree Length Size",

        "Image 1 (Front)",
        "Image 2",
        "Image 3",
        "Image 4",

        "Product ID / Style ID",
        "SKU ID",
        "Brand Name",
        "Group ID",
        "Product Description",

        "Blouse Color",
        "Blouse Fabric",
        "Blouse Pattern",
        "Border Width",
        "Brand",
        "Loom Type",
        "Occasion",
        "Ornamentation",
        "Pallu Details",
        "Pattern",
    ]

    ws.append(headers)

    # =========================================================
    # QUERY
    # =========================================================
    skus = SKU.objects.select_related(
        'brand', 'vendor', 'gender', 'article_type', 'color', 'size'
    ).order_by('-created_at')[:100]

    profile = getattr(request.user, "profile", None)

    # =========================================================
    # ROWS
    # =========================================================
    for sku in sku_list:

        ws.append([
            "", "", "",

            sku.style_description or "",
            sku.size.size if sku.size else "FREE SIZE",

            sku.sale_price or "",
            (sku.sale_price - Decimal("10.00")) if sku.sale_price else "",
            sku.mrp or "",

            5,
            5407,

            400,
            100,

            "India",

            # company, address and pin will be as per data saved in database
            sku.vendor.company if sku.vendor else "",
            sku.vendor.address if sku.vendor else "",
            sku.vendor.pin if sku.vendor else "",

            sku.vendor.company if sku.vendor else "",
            sku.vendor.address if sku.vendor else "",
            sku.vendor.pin if sku.vendor else "",

            # if you need the data as per profile logged in 
            # getattr(profile, "company", ""),
            # getattr(profile, "address", ""),
            # getattr(profile, "pin", ""),

            # getattr(profile, "company", ""),
            # getattr(profile, "address", ""),
            # getattr(profile, "pin", ""),

            "Not Required", "Not Required", "Not Required",

            sku.get_blouse_display() if sku.blouse else "",
            sku.get_border_display() if sku.border else "",
            MEESHO_COLOR_MAPPING.get(sku.color.color, "") if sku.color else "",

            sku.article_type.name if sku.article_type else "",
            "Single",

            sku.get_print_or_pattern_type_display() if sku.print_or_pattern_type else "",
            sku.get_saree_fabric_display() if sku.saree_fabric else "",
            sku.get_transparency_display() if sku.transparency else "",
            sku.get_type_display() if sku.type else "",

            float(sku.blouse_length or 0.8),
            float(sku.saree_length or 5.5),

            sku.product_image_link_1 or "",
            sku.product_image_link_2 or "",
            sku.product_image_link_3 or "",
            sku.product_image_link_4 or "",

            sku.sku or "",
            sku.sku or "",
            sku.brand.name if sku.brand else "",

            "",
            sku.style_description or "",

            MEESHO_COLOR_MAPPING.get(sku.get_blouse_color_display(), "") if sku.get_blouse_color_display else "",

            sku.get_blouse_fabric_display() if sku.blouse_fabric else "",
            sku.get_blouse_pattern_display() if sku.blouse_pattern else "",
            sku.get_border_width_display() if sku.border_width else "",

            sku.brand.name if sku.brand else "",
            sku.get_loom_type_display() if sku.loom_type else "",
            MEESHO_OCCASION_MAPPING.get(sku.get_occasion_display(), "") if sku.occasion else "",


            sku.get_ornamentation_display() if sku.ornamentation else "",
            sku.get_pallu_details_display() if sku.pallu_details else "",
            sku.get_pattern_display() if sku.pattern else "",
        ])

    # =========================================================
    # RESPONSE
    # =========================================================
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="meesho_saree_template.xlsx"'

    wb.save(response)
    return response

@login_required
def Flipkart_Template(request, sku_list):

    sku_list, _ = get_filtered_skus(request)

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Flipkart Saree Template"

    # =========================================================
    # HEADERS
    # =========================================================
    headers = [
        "Flipkart Serial Number",
        "Catalog QC Status",
        "QC Failed Reason (if any)",
        "Flipkart Product Link",
        "Seller SKU ID",
        "Group ID",
        "Listing Status",
        "MRP (INR)",
        "Your selling price (INR)",
        "Fullfilment by",
        "Procurement type",
        "Procurement SLA (DAY)",
        "Stock",
        "Shipping provider",
        "Local handling fee (INR)",
        "Zonal handling fee (INR)",
        "National handling fee (INR)",
        "Length (CM)",
        "Breadth (CM)",
        "Height (CM)",
        "Weight (KG)",
        "HSN",
        "Luxury Cess",
        "Country Of Origin",
        "Manufacturer Details",
        "Packer Details",
        "Importer Details",
        "Tax Code",
        "Minimum Order Quantity (MinOQ)",
        "Brand",
        "Occasion",
        "Fabric",
        "Pattern",
        "Type",
        "Sari Purity",
        "Ideal For",
        "Pack of",
        "Fabric Care",
        "Sari Length",
        "Blouse Piece Length (m)",
        "Sari Style",
        "Brand Size",
        "Brand Size - Measuring Unit",
        "Style Code",
        "Color",
        "Brand Color",
        "Blouse Piece Type",
        "Main Image URL",
        "Other Image URL 1",
        "Other Image URL 2",
        "Other Image URL 3",
        "Other Image URL 4",
        "Other Image URL 5",
        "Other Image URL 6",
        "Other Image URL 7",
        "Main Palette Image URL",
        "Pattern/Print Type",
        "Border Details",
        "Decorative Material",
        "Blouse Fabric",
        "Type of Embroidery",
        "Secondary Color",
        "Items Included",
        "Video URL",
        "Domestic Warranty",
        "Domestic Warranty - Measuring Unit",
        "International Warranty",
        "International Warranty - Measuring Unit",
        "Uniform",
        "Construction Type",
        "Handloom Product",
        "Hand Embroidery",
        "Border Length",
        "Blouse Pattern",
        "Embroidery Method",
        "EAN/UPC",
        "EAN/UPC - Measuring Unit",
        "Weight (kg)",
        "Other Details",
        "Description",
        "Search Keywords",
        "Product Title",
    ]

    ws.append(headers)

    # =========================================================
    # DATA QUERY
    # =========================================================
    skus = SKU.objects.select_related(
        "brand", "vendor", "gender", "color", "article_type", "size"
    ).order_by("-created_at")

    profile = getattr(request.user, "profile", None)

    # =========================================================
    # ROWS
    # =========================================================
    for sku in sku_list:

        ws.append([
            "", "", "", "",

            sku.sku or "",
            sku.style_no or "",
            "",
            "",
            "Active",

            sku.mrp or 0,
            (sku.sale_price or 0)+200,

            "Seller",
            "instock",
            2,
            500,

            "Flipkart",
            0,
            0,
            0,

            40,
            30,
            10,
            0.450,

            sku.hsn or "5407",
            0,
            "India",

            ", ".join(filter(None, [
                sku.vendor.company if sku.vendor else "",
                sku.vendor.address if sku.vendor else "",
                str(sku.vendor.pin) if sku.vendor else ""
            ])),
            ", ".join(filter(None, [
                sku.vendor.company if sku.vendor else "",
                sku.vendor.address if sku.vendor else "",
                str(sku.vendor.pin) if sku.vendor else ""
            ])),
            ", ".join(filter(None, [
                sku.vendor.company if sku.vendor else "",
                sku.vendor.address if sku.vendor else "",
                str(sku.vendor.pin) if sku.vendor else ""
            ])),

            # ", ".join(filter(None, [
            # getattr(profile, "company", ""),
            # getattr(profile, "address", "")
            # ])),

            # ", ".join(filter(None, [
            # getattr(profile, "company", ""),
            # getattr(profile, "address", "")
            # ])),
            # ", ".join(filter(None, [
            # getattr(profile, "company", ""),
            # getattr(profile, "address", "")
            # ])),
            "GST_5",

            1,

            sku.brand.name if sku.brand else "",

            FLIPKART_OCCASION_MAPPING.get(sku.get_occasion_display(), "") if sku.occasion else "",
            
            sku.get_saree_fabric_display() if sku.saree_fabric else "",
            sku.get_pattern_display() if sku.pattern else "",
            sku.get_type_display() if sku.type else "",

            "Synthetic" if sku.saree_fabric == "Polyester" else "Blend",
            
            sku.gender.name if sku.gender else "Women",
            1,

            "Hand Wash::Wash with Like Colors",

            str(sku.saree_length or 5.5) + "m",

            sku.blouse_length or 0.8,

            "Regular Sari",
            sku.size.size.split()[0] if sku.size else "Free",
            "Regular",
            
            sku.sku or "",

            FLIPKART_COLOR_MAPPING.get(sku.color.color, "") if sku.color.color else "",
            FLIPKART_COLOR_MAPPING.get(sku.color.color, "") if sku.color.color else "",



            "Unstitched",

            sku.product_image_link_1 or "",
            sku.product_image_link_2 or "",
            sku.product_image_link_3 or "",
            sku.product_image_link_4 or "",
            sku.product_image_link_5 or "",
            "",
            "",
            "",

            "",

            sku.get_print_or_pattern_type_display() if sku.print_or_pattern_type else "",
            sku.get_border_display() if sku.border else "",
            "",
            sku.get_blouse_fabric_display() if sku.blouse_fabric else "",
            "",
            "",
            "1::Saree",

            "",

            "",
            "",

            "",
            "",
            "",
            "",
            "",
            "",

            None if sku.border_width == "no_border" else ("Thin/Small" if sku.border_width == "small_border" else "Big/Thick"),
            "Printed" if sku.blouse_pattern =="printed" else "Solid",
            

            "Machine",

            "",

            "",

           "",

            (
                f"{sku.brand.name if sku.brand else ''} "
                f"{sku.color.color if sku.color else ''} "
                f"{sku.get_saree_fabric_display() if sku.saree_fabric else ''} "
                f"{sku.get_pattern_display() if sku.pattern else ''}"
            ),
            "women saree, latest saree, designer saree, party wear saree, wedding saree, festive saree, silk saree, cotton saree, georgette saree, traditional saree, ethnic saree, stylish saree, fashion saree, indian saree"
        ])

    # =========================================================
    # RESPONSE
    # =========================================================
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="flipkart_saree_template.xlsx"'

    wb.save(response)
    return response

@login_required
def Snapdeal_Template(request, sku_list):
    sku_list, _ = get_filtered_skus(request)

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Snapdeal Saree Template"

    # =========================================================
    # SNAPDEAL HEADERS
    # =========================================================
    headers = [
        "Offer Group Name",
        "SKU Code",
        "Brand",
        "Product Name",
        "Color",
        "Fabric",
        "Set Contents",
        "Type",
        "Manufacturer's Name & Address",
        "Saree Length(in metre)",
        "Blouse Piece Length (in meter)",
        "Country of Origin or Manufacture or Assembly",
        "Packer's Name & Address",
        "Net Contents",
        "Pattern",
        "Pack",
        "Saree Type",
        "Style Code/Name",
        "MRP",
        "Selling Price",
        "Inventory",
        "Shipping Time in Days",
        "Height (cm)",
        "Width (cm)",
        "Length (cm)",
        "Weight (g)",
        "Image 1",
        "Image 2",
        "Image 3",
        "Image 4",
        "Image 5",
        "Image 6",
        "Image 7",
        "Image 8",
        "Image 9",
        "Image 10",
        "Image 11",
        "Image 12",
        "Description",
        "EAN",
        "UPC",
        "Blouse Fabric",
        "Blouse Color",
        "Border Specific",
        "Saree width(in metre)",
        "Product Weight (in kg)",
        "Common or Generic Name of the commodity",
        "Importer's Name & Address",
        "Marketer's Name & Address",
        "Blouse Pattern",
        "Pattern or Print Type",
        "Shop By Occasion",
        "Brand Color",
        "Generic Keywords",
    ]

    ws.append(headers)

    # =========================================================
    # ROWS
    # =========================================================
    for sku in sku_list:

        vendor_address = ""

        if sku.vendor:
            vendor_address = (
                f"{sku.vendor.company}, {sku.vendor.address}"
            )

        color = ""
        if sku.color:
            color = SNAPDEAL_COLOR_MAPPING.get(
                sku.color.color,
                sku.color.color
            )

        blouse_color = ""
        if sku.get_blouse_color_display:
            blouse_color = MEESHO_COLOR_MAPPING.get(
                sku.get_blouse_color_display(),
                sku.get_blouse_color_display()
            )

        occasion = ""
        if sku.occasion:
            occasion = MEESHO_OCCASION_MAPPING.get(
                sku.get_occasion_display(),
                sku.get_occasion_display()
            )

        ws.append([

            # Offer Group Name
            "",

            # SKU Code
            sku.sku or "",

            # Brand
            sku.brand.name if sku.brand else "",

            # Product Name
            sku.style_description or "",

            # Color
            color,

            # Fabric
            sku.get_saree_fabric_display()
            if sku.saree_fabric else "",

            # Set Contents
            SNAPDEAL_SET_CONTENTS_MAPPING.get(
            sku.blouse,
            "Without Blouse Piece"
            ),

            # Type
            sku.get_type_display()
            if sku.type else "",

            # Manufacturer Name & Address
            vendor_address,

            # Saree Length
            float(sku.saree_length or 5.5),

            # Blouse Length
            float(sku.blouse_length or 0.8),

            # Country
            "India",

            # Packer
            vendor_address,

            # Net Contents
            "1",

            # Pattern
            sku.get_pattern_display()
            if sku.pattern else "",

            # Pack
            "1",

            # Saree Type
            sku.article_type.name
            if sku.article_type else "",

            # Style Code/Name
            sku.sku or sku.style_description or "",

            # MRP
            sku.mrp or "",

            # Selling Price
            sku.sale_price or "",

            # Inventory
            100,

            # Shipping Time
            "",

            # Height
            "",

            # Width
            "",

            # Length
            "",

            # Weight grams
            400,

            # Images
            sku.product_image_link_1 or "",
            sku.product_image_link_2 or "",
            sku.product_image_link_3 or "",
            sku.product_image_link_4 or "",

            # Image 5-12 blank
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",

            # Description
            sku.style_description or "",

            # EAN
            "",

            # UPC
            "",

            # Blouse Fabric
            sku.get_blouse_fabric_display()
            if sku.blouse_fabric else "",

            # Blouse Color
            blouse_color,

            # Border Specific
            sku.get_border_display()
            if sku.border else "",

            # Saree width
            "",

            # Product Weight kg
            0.4,

            # Generic Name
            "Saree",

            # Importer
            "",

            # Marketer
            vendor_address,

            # Blouse Pattern
            sku.get_blouse_pattern_display()
            if sku.blouse_pattern else "",

            # Pattern or Print Type
            sku.get_print_or_pattern_type_display()
            if sku.print_or_pattern_type else "",

            # Occasion
            occasion,

            # Brand Color
            color,

            # Generic Keywords
            "",
        ])

    # =========================================================
    # RESPONSE
    # =========================================================
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    response["Content-Disposition"] = (
        'attachment; filename="snapdeal_saree_template.xlsx"'
    )

    wb.save(response)

    return response

def View__VMS(request):
    if request.method == 'GET':
        search_query = request.GET.get('search', '').strip()
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        vms_list = VMS.objects.all().order_by('-id')

        # Filter by start date
        if start_date:
            try:
                parsed_start_date = datetime.strptime(start_date, '%Y-%m-%d')
                vms_list = vms_list.filter(created_at__gte=parsed_start_date)
            except ValueError:
                pass  # Ignore invalid date

        # Filter by end date (inclusive of the entire day)
        if end_date:
            try:
                parsed_end_date = datetime.strptime(end_date, '%Y-%m-%d') + timedelta(days=1)
                vms_list = vms_list.filter(created_at__lt=parsed_end_date)
            except ValueError:
                pass

        # Search filter by tracking_id
        if search_query:
            vms_list = vms_list.filter(Q(tracking_id__icontains=search_query))

        # Pagination
        paginator = Paginator(vms_list, 10)
        page = request.GET.get('page', 1)
        try:
            vms = paginator.page(page)
        except PageNotAnInteger:
            vms = paginator.page(1)
        except EmptyPage:
            vms = paginator.page(paginator.num_pages)

        context = {
            'vms': vms,
            'search_query': search_query,
            'start_date': start_date,
            'end_date': end_date,
        }

        return render(request, 'vms/view_vms.html', context)


def Delete__VMS(request):
    if request.method == 'GET':
        search_query = request.GET.get('search', '').strip()
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        vms_list = VMS.objects.all().order_by('-id')

        # Filter by start date
        if start_date:
            try:
                parsed_start_date = datetime.strptime(start_date, '%Y-%m-%d')
                vms_list = vms_list.filter(created_at__gte=parsed_start_date)
            except ValueError:
                pass  # Ignore invalid date

        # Filter by end date (inclusive of the entire day)
        if end_date:
            try:
                parsed_end_date = datetime.strptime(end_date, '%Y-%m-%d') + timedelta(days=1)
                vms_list = vms_list.filter(created_at__lt=parsed_end_date)
            except ValueError:
                pass

        # Search filter by tracking_id
        if search_query:
            vms_list = vms_list.filter(Q(tracking_id__icontains=search_query))

        # Pagination
        paginator = Paginator(vms_list, 10)
        page = request.GET.get('page', 1)
        try:
            vms = paginator.page(page)
        except PageNotAnInteger:
            vms = paginator.page(1)
        except EmptyPage:
            vms = paginator.page(paginator.num_pages)

        context = {
            'vms': vms,
            'search_query': search_query,
            'start_date': start_date,
            'end_date': end_date,
        }

        return render(request, 'vms/view_vms.html', context)


@csrf_exempt
def save_video(request):
    if request.method == 'POST':
        tracking_id = request.POST.get('tracking_id')
        video_file = request.FILES.get('video_file')
        transaction_type = request.POST.get('transaction_type')

        vms = VMS.objects.create(
            tracking_id=tracking_id,
            video_type=transaction_type,
            video_file=video_file
        )

        return JsonResponse({'status': 'success', 'vms_id': vms.id})

    return JsonResponse({'status': 'error'}, status=400)


def record_video_page(request):
    return render(request, 'vms/record_video.html')  # use the full path inside 'templates'


