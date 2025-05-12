from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Customer, Purchase, PurchaseItem
from .forms import ItemForm, PurchaseForm, PurchaseItemForm
from django.forms import modelformset_factory
from django.db import transaction

def dashboard(request):
    item_form = ItemForm()
    purchase_form = PurchaseForm()
    PurchaseItemFormSet = modelformset_factory(PurchaseItem, form=PurchaseItemForm, extra=1)
    purchase_formset = PurchaseItemFormSet(queryset=PurchaseItem.objects.none())

    if request.method == 'POST':
        if 'name' in request.POST and 'stock' in request.POST:
            item_form = ItemForm(request.POST, request.FILES)  # Add request.FILES
            if item_form.is_valid():
                item_form.save()
                return redirect('dashboard')

        elif 'customer_name' in request.POST:
            purchase_form = PurchaseForm(request.POST)
            purchase_formset = PurchaseItemFormSet(request.POST)
            if purchase_form.is_valid() and purchase_formset.is_valid():
                with transaction.atomic():
                    customer, _ = Customer.objects.get_or_create(
                        name=purchase_form.cleaned_data['customer_name'],
                        address=purchase_form.cleaned_data['customer_address']
                    )
                    purchase = Purchase.objects.create(customer=customer)

                    for form in purchase_formset:
                        if form.cleaned_data:
                            item = form.cleaned_data['item']
                            qty = form.cleaned_data['quantity']
                            PurchaseItem.objects.create(purchase=purchase, item=item, quantity=qty)
                return redirect('dashboard')

    # Add items to context
    items = Item.objects.all()
    purchases = PurchaseItem.objects.select_related('purchase__customer', 'item').all()

    return render(request, 'dashboard.html', {
        'item_form': item_form,
        'purchase_form': purchase_form,
        'purchase_formset': purchase_formset,
        'purchases': purchases,
        'items': items,  # Add items to context
    })

def delete_purchase_item(request, pk):
    item = get_object_or_404(PurchaseItem, pk=pk)
    item.delete()
    return redirect('dashboard')
