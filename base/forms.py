from django import forms
from .models import (
    HeroSection, AboutSection, MenuItem, SpecialOffer, Testimonial, 
     Location, FAQ, GalleryImage, 
    ContactInfo, SocialMedia
)

class HeroSectionForm(forms.ModelForm):
    class Meta:
        model = HeroSection
        fields = '__all__'


class AboutSectionForm(forms.ModelForm):
    class Meta:
        model = AboutSection
        fields = '__all__'


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'


class SpecialOfferForm(forms.ModelForm):
    class Meta:
        model = SpecialOffer
        fields = '__all__'


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = '__all__'



class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'


class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = '__all__'





class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = '__all__'


class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = '__all__'


class SocialMediaForm(forms.ModelForm):
    class Meta:
        model = SocialMedia
        fields = '__all__'
