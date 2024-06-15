from django.shortcuts import render
from django.views.generic import View, TemplateView
from inventory.models import Stock
from transactions.models import SaleBill, PurchaseBill
from datetime import datetime, timedelta


class HomeView(View):
    template_name = "home.html"

    def get(self, request):
        labels = []
        data = []

        stockqueryset = Stock.objects.filter(is_deleted=False).order_by('-quantity')
        for item in stockqueryset:
            labels.append(item.name)
            data.append(item.quantity)

        sales = SaleBill.objects.order_by('-time')[:3]
        purchases = PurchaseBill.objects.order_by('-time')[:3]

        # Fetch products near to expire
        today = datetime.today()
        near_expiry_threshold = today + timedelta(days=30)  # Adjust the threshold as needed
        near_expiry_products = Stock.objects.filter(expiry_date__lte=near_expiry_threshold, is_deleted=False).order_by(
            'expiry_date')

        context = {
            'labels': labels,
            'data': data,
            'sales': sales,
            'purchases': purchases,
            'near_expiry_products': near_expiry_products,
        }
        return render(request, self.template_name, context)


class AboutView(TemplateView):
    template_name = "about.html"
