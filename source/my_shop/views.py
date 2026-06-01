from django.shortcuts import render, redirect

from my_shop.models import Products, Categories

# Create your views here.
def products_view(request):
    products = Products.objects.all()
    context = {'products': products}
    return render(request, "my_shop_forms/products.html", context)

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
        Products.objects.create(name=name, price=price, image=image, category=category_obj, description=description)
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