from django import forms
PRODUCT_QUANTITY_CHOICES=[(i,str(i)) fir i in range (1,30)]

class CartAddProductForm(forms.Form):
    quantity=forms.TypedChoicesField(choices=PRODUCT_QUANTITY_CHOICES,
                                    coerce=int)
    override=forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
                                
