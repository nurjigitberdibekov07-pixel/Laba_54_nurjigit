from django.shortcuts import render, redirect

from my_shop.models import Products, Categories

# Create your views here.
def products_view(request):
    products = Products.objects.all()
    context = {'products': products}
    return render(request, "my_shop_forms/products.html", context)

def add_product(request):
    if request.method == "GET":
        return render(request, "my_shop_form/product_view.html")


def add_category(request):
    if request.method == "GET":
        return render(request, "my_shop_forms/category_add.html")
    elif request.method == "POST":
        name = request.POST.get("name", "").strip()
        if not name:
            return render(request, "my_shop_forms/category_add.html", {"error": "Please enter a name"})
        Categories.objects.create(name=name, description=request.POST.get("description", "").strip())
        return redirect("add_category")