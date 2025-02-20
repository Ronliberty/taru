from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import (
    HeroSection, AboutSection, MenuItem, SpecialOffer, Testimonial,
    Reservation, Location, FAQ, NewsletterSubscription, GalleryImage,
    ContactInfo, SocialMedia
)
from .forms import (
    HeroSectionForm, AboutSectionForm, MenuItemForm, SpecialOfferForm,
    TestimonialForm, LocationForm, FAQForm, ContactInfoForm,
    GalleryImageForm, SocialMediaForm
)
from datetime import datetime

# Create your views here.
def index(request):
    # Retrieve content for the landing page
    hero_section  = HeroSection.objects.first()
    about_section = AboutSection.objects.first()
    menu_items    = MenuItem.objects.all()
    specials      = SpecialOffer.objects.all()
    testimonials  = Testimonial.objects.all()
    locations     = Location.objects.all()
    faqs          = FAQ.objects.all()
    images        = GalleryImage.objects.all()
    contact       = ContactInfo.objects.first()
    social_links  = SocialMedia.objects.first()

    if request.method == "POST":
        # Check for reservation submission: expects 'name' and 'date_time'
        if request.POST.get('name') and request.POST.get('date_time'):
            name      = request.POST.get('name')
            email     = request.POST.get('email')
            date_time = request.POST.get('date_time')  # Expecting "YYYY-MM-DDTHH:MM" format

            if name and email and date_time:
                try:
                    # Convert the datetime-local string to a Python datetime object
                    dt = datetime.strptime(date_time, "%Y-%m-%dT%H:%M")
                    Reservation.objects.create(name=name, email=email, date_time=dt)
                except Exception as e:
                    print("Error processing reservation:", e)
            return redirect('base:index')

        # Check for newsletter subscription submission:
        elif request.POST.get('newsletter_email'):
            newsletter_email = request.POST.get('newsletter_email')
            if newsletter_email:
                try:
                    NewsletterSubscription.objects.create(email=newsletter_email)
                except Exception as e:
                    print("Error processing newsletter subscription:", e)
            return redirect('base:index')

    context = {
        'hero_section': hero_section,
        'about_section': about_section,
        'menu_items': menu_items,
        'specials': specials,
        'testimonials': testimonials,
        'locations': locations,
        'faqs': faqs,
        'images': images,
        'contact': contact,
        'social_links': social_links,
    }
    return render(request, 'base/index.html', context)




# ----- HeroSection Views -----
class HeroSectionListView(ListView):
    model = HeroSection
    template_name = 'base/hero_section_list.html'

class HeroSectionDetailView(DetailView):
    model = HeroSection
    template_name = 'base/hero_section_detail.html'

class HeroSectionCreateView(CreateView):
    model = HeroSection
    form_class = HeroSectionForm
    template_name = 'base/hero_section_form.html'
    success_url = reverse_lazy('base:hero_section_list')

class HeroSectionUpdateView(UpdateView):
    model = HeroSection
    form_class = HeroSectionForm
    template_name = 'base/hero_section_form.html'
    success_url = reverse_lazy('base:hero_section_list')

class HeroSectionDeleteView(DeleteView):
    model = HeroSection
    template_name = 'base/hero_section_confirm_delete.html'
    success_url = reverse_lazy('base:hero_section_list')


# ----- AboutSection Views -----
class AboutSectionListView(ListView):
    model = AboutSection
    template_name = 'base/about_section_list.html'

class AboutSectionDetailView(DetailView):
    model = AboutSection
    template_name = 'base/about_section_detail.html'

class AboutSectionCreateView(CreateView):
    model = AboutSection
    form_class = AboutSectionForm
    template_name = 'base/about_section_form.html'
    success_url = reverse_lazy('base:about_section_list')

class AboutSectionUpdateView(UpdateView):
    model = AboutSection
    form_class = AboutSectionForm
    template_name = 'base/about_section_form.html'
    success_url = reverse_lazy('base:about_section_list')

class AboutSectionDeleteView(DeleteView):
    model = AboutSection
    template_name = 'base/about_section_confirm_delete.html'
    success_url = reverse_lazy('base:about_section_list')


# ----- MenuItem Views -----
class MenuItemListView(ListView):
    model = MenuItem
    template_name = 'base/menuitem_list.html'

class MenuItemDetailView(DetailView):
    model = MenuItem
    template_name = 'base/menuitem_detail.html'

class MenuItemCreateView(CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'base/menuitem_form.html'
    success_url = reverse_lazy('base:menuitem_list')

class MenuItemUpdateView(UpdateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'base/menuitem_form.html'
    success_url = reverse_lazy('base:menuitem_list')

class MenuItemDeleteView(DeleteView):
    model = MenuItem
    template_name = 'base/menuitem_confirm_delete.html'
    success_url = reverse_lazy('base:menuitem_list')


# ----- SpecialOffer Views -----
class SpecialOfferListView(ListView):
    model = SpecialOffer
    template_name = 'base/specialoffer_list.html'

class SpecialOfferDetailView(DetailView):
    model = SpecialOffer
    template_name = 'base/specialoffer_detail.html'

class SpecialOfferCreateView(CreateView):
    model = SpecialOffer
    form_class = SpecialOfferForm
    template_name = 'base/specialoffer_form.html'
    success_url = reverse_lazy('base:specialoffer_list')

class SpecialOfferUpdateView(UpdateView):
    model = SpecialOffer
    form_class = SpecialOfferForm
    template_name = 'base/specialoffer_form.html'
    success_url = reverse_lazy('base:specialoffer_list')

class SpecialOfferDeleteView(DeleteView):
    model = SpecialOffer
    template_name = 'base/specialoffer_confirm_delete.html'
    success_url = reverse_lazy('base:specialoffer_list')


# ----- Testimonial Views -----
class TestimonialListView(ListView):
    model = Testimonial
    template_name = 'base/testimonial_list.html'

class TestimonialDetailView(DetailView):
    model = Testimonial
    template_name = 'base/testimonial_detail.html'

class TestimonialCreateView(CreateView):
    model = Testimonial
    form_class = TestimonialForm
    template_name = 'base/testimonial_form.html'
    success_url = reverse_lazy('base:testimonial_list')

class TestimonialUpdateView(UpdateView):
    model = Testimonial
    form_class = TestimonialForm
    template_name = 'base/testimonial_form.html'
    success_url = reverse_lazy('base:testimonial_list')

class TestimonialDeleteView(DeleteView):
    model = Testimonial
    template_name = 'base/testimonial_confirm_delete.html'
    success_url = reverse_lazy('base:testimonial_list')


# ----- Reservation Views -----
class ReservationListView(ListView):
    model = Reservation
    template_name = 'base/reservation_list.html'

class ReservationDetailView(DetailView):
    model = Reservation
    template_name = 'base/reservation_detail.html'







# ----- Location Views -----
class LocationListView(ListView):
    model = Location
    template_name = 'base/location_list.html'

class LocationDetailView(DetailView):
    model = Location
    template_name = 'base/location_detail.html'

class LocationCreateView(CreateView):
    model = Location
    form_class = LocationForm
    template_name = 'base/location_form.html'
    success_url = reverse_lazy('base:location_list')

class LocationUpdateView(UpdateView):
    model = Location
    form_class = LocationForm
    template_name = 'base/location_form.html'
    success_url = reverse_lazy('base:location_list')

class LocationDeleteView(DeleteView):
    model = Location
    template_name = 'base/location_confirm_delete.html'
    success_url = reverse_lazy('base:location_list')


# ----- FAQ Views -----
class FAQListView(ListView):
    model = FAQ
    template_name = 'base/faq_list.html'

class FAQDetailView(DetailView):
    model = FAQ
    template_name = 'base/faq_detail.html'

class FAQCreateView(CreateView):
    model = FAQ
    form_class = FAQForm
    template_name = 'base/faq_form.html'
    success_url = reverse_lazy('base:faq_list')

class FAQUpdateView(UpdateView):
    model = FAQ
    form_class = FAQForm
    template_name = 'base/faq_form.html'
    success_url = reverse_lazy('faq_list')

class FAQDeleteView(DeleteView):
    model = FAQ
    template_name = 'base/faq_confirm_delete.html'
    success_url = reverse_lazy('base:faq_list')


# ----- NewsletterSubscription Views -----
class NewsletterSubscriptionListView(ListView):
    model = NewsletterSubscription
    template_name = 'base/newslettersubscription_list.html'

class NewsletterSubscriptionDetailView(DetailView):
    model = NewsletterSubscription
    template_name = 'base/newslettersubscription_detail.html'




# ----- GalleryImage Views -----
class GalleryImageListView(ListView):
    model = GalleryImage
    template_name = 'base/galleryimage_list.html'

class GalleryImageDetailView(DetailView):
    model = GalleryImage
    template_name = 'base/galleryimage_detail.html'

class GalleryImageCreateView(CreateView):
    model = GalleryImage
    form_class = GalleryImageForm
    template_name = 'base/galleryimage_form.html'
    success_url = reverse_lazy('base:galleryimage_list')

class GalleryImageUpdateView(UpdateView):
    model = GalleryImage
    form_class = GalleryImageForm
    template_name = 'base/galleryimage_form.html'
    success_url = reverse_lazy('base:galleryimage_list')

class GalleryImageDeleteView(DeleteView):
    model = GalleryImage
    template_name = 'base/galleryimage_confirm_delete.html'
    success_url = reverse_lazy('base:galleryimage_list')


# ----- ContactInfo Views -----
class ContactInfoListView(ListView):
    model = ContactInfo
    template_name = 'base/contactinfo_list.html'

class ContactInfoDetailView(DetailView):
    model = ContactInfo
    template_name = 'base/contactinfo_detail.html'

class ContactInfoCreateView(CreateView):
    model = ContactInfo
    form_class = ContactInfoForm
    template_name = 'base/contactinfo_form.html'
    success_url = reverse_lazy('base:contactinfo_list')

class ContactInfoUpdateView(UpdateView):
    model = ContactInfo
    form_class = ContactInfoForm
    template_name = 'base/contactinfo_form.html'
    success_url = reverse_lazy('base:contactinfo_list')

class ContactInfoDeleteView(DeleteView):
    model = ContactInfo
    template_name = 'base/contactinfo_confirm_delete.html'
    success_url = reverse_lazy('base:contactinfo_list')


# ----- SocialMedia Views -----
class SocialMediaListView(ListView):
    model = SocialMedia
    template_name = 'base/socialmedia_list.html'

class SocialMediaDetailView(DetailView):
    model = SocialMedia
    template_name = 'base/socialmedia_detail.html'

class SocialMediaCreateView(CreateView):
    model = SocialMedia
    form_class = SocialMediaForm
    template_name = 'base/socialmedia_form.html'
    success_url = reverse_lazy('base:socialmedia_list')

class SocialMediaUpdateView(UpdateView):
    model = SocialMedia
    form_class = SocialMediaForm
    template_name = 'base/socialmedia_form.html'
    success_url = reverse_lazy('base:socialmedia_list')

class SocialMediaDeleteView(DeleteView):
    model = SocialMedia
    template_name = 'base/socialmedia_confirm_delete.html'
    success_url = reverse_lazy('base:socialmedia_list')
