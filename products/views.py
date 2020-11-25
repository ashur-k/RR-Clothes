import json
from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.template.loader import render_to_string
from django.db.models.functions import Lower
from products.models import Product, Images, Variants, Category
from django.db.models import Q
from .forms import ProductForm, ProductVariantForm, CategoryForm, ProductColorForm, ProductSizeForm, ProductImageForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required


# Create your views here.

def all_products(request):
    """ A view to show all products """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    product = None

    if request.GET:
        if 'sort' in request.GET:
            print('here')
            print(request.GET['sort'])
            print('and there')
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'product' in request.GET:
            categories = request.GET['product'].split(',')
            products = products.filter(category__name__in=categories)
            products = products.filter(new_edition=True)

        if 'discount_30_percent' in request.GET:
            categories = request.GET['discount_30_percent'].split(',')
            products = products.filter(category__name__in=categories)
            products = products.filter(discount_30_percent=True)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('RR_home'))

            queries = Q(title__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
            messages.success(request, f'{products.count()} results found.')
    current_sorting = f'{sort}_{direction}'
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting
    }

    return render(request, 'products/products.html', context)


def search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        products = Product.objects.filter(title__icontains=q)
        print(products.count())

        results = []
        for rs in products:
            product_json = {}
            product_json = rs.title + " > " + rs.category.title
            results.append(product_json)
            print(rs.title)
        print(results)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def product_detail(request, product_id):
    """ A view to show product details """
    query = request.GET.get('q')
    product = get_object_or_404(Product, id=product_id)
    print(product.averagereviews())
    images = Images.objects.filter(product_id=product_id)

    # I am giving variant ID from server side to product detail template
    # to feed variant id to form when item is only product
    variant_id_value = None
    no_variants = Variants.objects.filter(product_id=product_id)

    # products which have no variant will always have
    # one variant by default and we are getting its id
    # saving in variant_id_value
    for items in no_variants:
        variant_id_value = items.id

    if request.method == 'POST':
        variant_id_value = None
        messages.error(request, 'Please request store owner to update product informaiton')

    if variant_id_value is None:
        if product.has_variant is True or product.variant != 'None':
            pass
        else:
            form_data = {
                'title': product.title,
                'quantity': product.quantity,
                'price': product.price,
                }
            variant_form = ProductVariantForm(form_data)
            variant = variant_form.save(commit=False)
            variant.product = product
            variant_form.save()
            variant_id_value = variant.id

    context = {
        'product': product,
        'images': images,
        'variant_id_value': variant_id_value
        }

    if request.method == 'POST':  # if we select color
        variant_id = request.POST.get('variantid')
        variant = Variants.objects.get(id=variant_id)
        colors = Variants.objects.filter(product_id=product_id, size_id=variant.size_id)
        sizes = Variants.objects.raw('SELECT * FROM  products_variants  WHERE product_id=%s GROUP BY size_id', [product_id])
        query += variant.title + ' Size:' + str(variant.size) + ' Color: ' + str(variant.color)
    else:
        variants = Variants.objects.filter(product_id=product_id)
        colors = Variants.objects.filter(product_id=product_id, size_id=variants[0].size_id)
        sizes = Variants.objects.raw('SELECT * FROM  products_variants  WHERE product_id=%s GROUP BY size_id', [product_id])
        variant = Variants.objects.get(id=variants[0].id)

        context.update({
            'sizes': sizes,
            'colors': colors,
            'variant': variant,
            'query': query,
                        })
    return render(request, 'products/products_detail.html', context)


def ajaxcolor(request):
    data = {}
    if request.POST.get('action') == 'post':
        size_id = request.POST.get('size')
        productid = request.POST.get('productid')
        colors = Variants.objects.filter(product_id=productid, size_id=size_id)
        for c in colors:
            print(c)
        context = {
            'size_id': size_id,
            'productid': productid,
            'colors': colors,
        }
        data = {'rendered_table': render_to_string('products/color_list.html', context=context)}
        return JsonResponse(data)
    return JsonResponse(data)


@login_required
def add_category(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that')
        return redirect(reverse('RR_home'))

    if request.method == 'POST':
        category_form = CategoryForm(request.POST, request.FILES)
        if category_form.is_valid():
            category_form.save()
    else:
        form = CategoryForm()

    form = CategoryForm()
    template = 'products/add_category.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def add_product(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that')
        return redirect(reverse('RR_home'))

    if request.method == 'POST':
        has_variant = request.POST.get('has_variant')
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            if has_variant == 'true':
                return redirect('add_variant', product_id=product.id)
            else:
                variant_form = ProductVariantForm(request.POST or None)
                variant = variant_form.save(commit=False)
                product = get_object_or_404(Product, id=product.id)
                variant.title = variant_form.cleaned_data['title']
                variant.product = product
                variant_form.save()
    else:
        form = ProductVariantForm()

    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def add_variant(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that')
        return redirect(reverse('RR_home'))
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        if product.variant == "Color":
            form_data = {
                'title': request.POST['title'],
                'color': request.POST['color'],
                'quantity': request.POST['quantity'],
                'price': request.POST['price'],
            }
            variant_form = ProductColorForm(form_data)
            if variant_form.is_valid():
                variant = variant_form.save(commit=False)
                variant.product = product
                variant_form.save()
                messages.success(request, 'Variant added successfully')

        elif product.variant == "Size":
            form_data = {
                'title': request.POST['title'],
                'size': request.POST['size'],
                'quantity': request.POST['quantity'],
                'price': request.POST['price'],
            }
            variant_form = ProductSizeForm(form_data)
            if variant_form.is_valid():
                variant = variant_form.save(commit=False)
                variant.product = product
                variant_form.save()
                messages.success(request, 'Variant added successfully')
        else:
            form_data = {
                'title': request.POST['title'],
                'color': request.POST['color'],
                'size': request.POST['size'],
                'quantity': request.POST['quantity'],
                'price': request.POST['price'],
            }
            variant_form = ProductVariantForm(form_data)
            if variant_form.is_valid():
                variant = variant_form.save(commit=False)
                variant.product = product
                variant_form.save()
                messages.success(request, 'Variant added successfully')

    if product.variant == "Color":
        form = ProductColorForm
    elif product.variant == "Size":
        form = ProductSizeForm
    else:
        form = ProductVariantForm

    context = {
        'form': form,
    }
    template = 'products/add_product_variant.html'
    return render(request, template, context)


@login_required
def product_management(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that')
        return redirect(reverse('RR_home'))

    product = get_object_or_404(Product, pk=product_id)
    images = Images.objects.filter(product_id=product_id)
    image_form = ProductImageForm

    if request.method == 'POST':
        image_form = ProductImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            image = image_form.save(commit=False)
            image.product = product
            image_form.save()
            messages.success(request, 'Image added successfully')

    if product.has_variant == 0:
        variant = get_object_or_404(Variants, product_id=product_id)
        template = 'products/product_management.html'
        context = {
            'product': product,
            'variant': variant,
            'images': images,
            'image_form': image_form,
            }
        return render(request, template, context)

    else:
        variants = Variants.objects.filter(product_id=product_id)
        template = 'products/product_management.html'
        context = {
            'product': product,
            'variants': variants,
            'images': images,
            'image_form': image_form,
        }
        return render(request, template, context)


@login_required
def edit_product_with_variant(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that')
        return redirect(reverse('RR_home'))
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product successfully added')
            return redirect(reverse('product_management', args=[product_id]))
    form = ProductForm(instance=product)
    messages.info(request, f'You are editing {product.title}')
    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def edit_product_without_variant(request, product_id, variant_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that')
        return redirect(reverse('RR_home'))
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        has_variant = request.POST.get('has_variant')
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            if has_variant == 'false':
                variant = get_object_or_404(Variants, pk=variant_id)
                variant_form = ProductVariantForm(request.POST, instance=variant)
                if variant_form.is_valid():
                    variant = variant_form.save(commit=False)
                    product = get_object_or_404(Product, id=product_id)
                    variant.product = product
                    variant_form.save()
                    messages.success(request, f'You have succesfully edited Product. {product.title}')
                    return redirect(reverse('product_management', args=[product_id]))

    form = ProductForm(instance=product)
    messages.info(request, f'You are editing {product.title}')
    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def edit_variant(request, product_id, variant_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that')
        return redirect(reverse('RR_home'))
    variant = get_object_or_404(Variants, pk=variant_id)
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductVariantForm(request.POST, instance=variant)
        if form.is_valid():
            form.save()
            messages.success(request, "Variant updated succesfully.")
            return redirect(reverse('product_management', args=[product_id]))
        else:
            messages.error(request, 'Failed to updated Product.')
    else:
        if product.variant == "Color":
            form = ProductColorForm(instance=variant)
            messages.info(request, f'You are editing {variant.title}')
        elif product.variant == "Size":
            form = ProductSizeForm(instance=variant)
            messages.info(request, f'You are editing {variant.title}')
        elif product.variant == "Size-Color":
            form = ProductVariantForm(instance=variant)
            messages.info(request, f'You are editing {variant.title}')

    template = 'products/edit_variant.html'
    #form = ProductVariantForm(instance=variant)
    context = {
        'form': form,
        'variant': variant,
    }
    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that')
        return redirect(reverse('RR_home'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted successfully!')
    return redirect(reverse('product_management', args=[product_id]))


@login_required
def delete_variant(request, variant_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that')
        return redirect(reverse('RR_home'))
    variant = get_object_or_404(Variants, pk=variant_id)
    variant.delete()
    messages.success(request, 'Variant deleted successfully!')
    return redirect(reverse('product_management', args=[variant.product_id]))


@login_required
def delete_image(request, image_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that')
        return redirect(reverse('RR_home'))
    image = get_object_or_404(Images, pk=image_id)
    image.delete()
    messages.success(request, 'Image deleted successfully!')
    return redirect(reverse('product_management', args=[image.product_id]))
