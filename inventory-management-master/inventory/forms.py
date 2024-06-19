from django import forms
from .models import Stock

class StockForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):  # used to set CSS classes to the various fields
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        self.fields['expiry_date'].widget.attrs.update({'class': 'textinput form-control', 'type': 'date'})
        self.fields['price'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})

    class Meta:
        model = Stock
        fields = ['name', 'quantity', 'expiry_date', 'price']
        widgets = {
            'expiry_date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }
