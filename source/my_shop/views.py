from django.shortcuts import render, redirect

from my_shop.models import Products, Categories

# Create your views here.
def products_view(request):
    products = Products.objects.all()
    context = {'products': products}
    return render(request, "my_shop_forms/products.html", context)

def categories_view(request):
    categories = Categories.objects.all()
    context = {'categories': categories}
    return render(request, "my_shop_forms/categories.html", context)

def product_detail(request, pk):
    product = Products.objects.get(pk=pk)
    context = {'product': product}
    return render(request, "my_shop_forms/detail_product.html", context)

def add_product(request):
    if request.method == "GET":
        categories = Categories.objects.all()
        context = { 'categories': categories}
        return render(request, "my_shop_forms/product_add.html", context)
    elif request.method == "POST":
        name = request.POST.get("name", "").strip()
        price = request.POST.get("price", "").strip()
        image = request.POST.get("image", "").strip()
        category = request.POST.get("category", "").strip()
        description = request.POST.get("description", "").strip()
        if not name or not price or not image or not category:
            return render(request,"my_shop_forms/product_add.html", context={"error": "Please enter a title, price, image"})
        category_obj = Categories.objects.get(pk=category)
        product = Products.objects.create(name=name, price=price, image=image, category=category_obj, description=description)
        return redirect("product_detail", pk=product.pk)

def delete_product(request, pk):
    product = Products.objects.get(pk=pk)
    product.delete()
    return redirect("products")

def edit_product(request, pk):
    product = Products.objects.get(pk=pk)
    if request.method == "GET":
        categories = Categories.objects.all()
        return render(request, "my_shop_forms/product_edit.html", {'product': product, 'categories': categories})
    elif request.method == "POST":
        product.name = request.POST.get("name", "").strip()
        product.price = request.POST.get("price", "").strip()
        product.image = request.POST.get("image", "").strip()
        product.description = request.POST.get("description", "").strip()
        category_pk = request.POST.get("category", "").strip()
        product.category = Categories.objects.get(pk=category_pk)
        if not product.name or not product.price or not product.image or not category_pk:
            return render(request, "my_shop_forms/product_edit.html",
                          context={"error": "Please enter a title, price, image", "product": product})
        product.save()
        return redirect("products")


def add_category(request):
    if request.method == "GET":
        return render(request, "my_shop_forms/category_add.html")
    elif request.method == "POST":
        name = request.POST.get("name", "").strip()
        if not name:
            return render(request, "my_shop_forms/category_add.html", {"error": "Please enter a name"})
        Categories.objects.create(name=name, description=request.POST.get("description", "").strip())
        return redirect("add_category")

def delete_category(request, pk):
    category = Categories.objects.get(pk=pk)
    Products.objects.filter(category=category).delete()
    category.delete()
    return redirect("categories_view")

def edit_category(request, pk):
    category = Categories.objects.get(pk=pk)
    if request.method == "GET":
        context = {'category': category}
        return render(request, "my_shop_forms/category_edit.html", context)
    elif request.method == "POST":
        name = request.POST.get("name", "").strip()
        if not name:
            return render(request, "my_shop_forms/category_edit.html", {"error": "Please enter a name"} )
        description = request.POST.get("description", "").strip()
        category.name = name
        category.description = description
        category.save()
        return redirect("categories_view")