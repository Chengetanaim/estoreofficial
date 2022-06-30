from django import forms
from .models import Item, EStore, ItemEstore, HotDeals


CATEGORIES = (
    ("1", "Men Collection"),
    ("2", "Ladies Collection"),
    ("3", "Kids Collection"),
    ("4", "Phones and Tablets"),
    ("5", "Laptops"),
    ("6", "Appliances and Machinery"),
    ("7", "Accessories"),
    ("8", "Dining and Lounge"),
    ("9", "Kitchen"),
    ("10", "Bedroom"),
    ("11", "Bathroom"),
    ("12", "Skin Care"),
    ("13", "Hair Products"),
    ("14", "Fragrances"),
    ("15", "Cars"),
    ("16", "Trucks"),
    ("17", "Vehicle Parts"),
    ("18", "Event Services"),
    ("19", "Food Services"),
    ("20", "Other Services"),
    ("21", "Other"),
    ("22", "Other Electronics"),
    ("23", "Other Beauty and Cosmetics"),
    ("24", "Other Vehicles"),
    ("25", "Other Homeware")
)


class ItemForm(forms.ModelForm):

    category = forms.ChoiceField(choices=CATEGORIES)

    class Meta:
       model = Item
       fields = ['product_name', 'price', 'location', 'description', 'category', 'image1', 'image2', 'image3', 'image4']
       labels = {'product_name': 'Name', 'price': 'Price', 'location': 'Location', 'description': 'Description', 'image1':
                 'Image', 'image2': 'Image', 'image3': 'Image', 'image4': 'Image'}


class Create_EStoreForm(forms.ModelForm):
    class Meta:
        model = EStore
        fields = ['store_name', 'category', 'location', 'profile_pic']
        labels = {'store_name': 'Store Name', 'category': 'Category', 'location': 'Location', 'profile_pic': 'Picture'}


class ItemEstoreForm(forms.ModelForm):
    category = forms.ChoiceField(choices=CATEGORIES)

    class Meta:
        model = ItemEstore
        fields = ['product_name', 'price', 'description', 'category', 'estore', 'image1', 'image2', 'image3', 'image4']
        labels = {'product_name': 'Name', 'price': 'Price', 'description': 'Description', 'category': 'Category'
            , 'estore': 'Estore', 'image1': 'Image', 'image2': 'Image', 'image3': 'Image', 'image4': 'Image'}


class HotDealsForm(forms.ModelForm):
    category = forms.ChoiceField(choices=CATEGORIES)

    class Meta:
        model = HotDeals
        fields = ['image', 'description', 'category']
        labels = {'image': 'Image', 'description': 'Description', 'category': 'Category'}

