from django.urls import path
from .import views

app_name = 'base'
urlpatterns = [
    path('', views.index, name='index'),
    path('hero/', views.HeroSectionListView.as_view(), name='hero_section_list'),
    path('hero/<int:pk>/', views.HeroSectionDetailView.as_view(), name='hero_section_detail'),
    path('hero/create/', views.HeroSectionCreateView.as_view(), name='hero_section_create'),
    path('hero/<int:pk>/update/', views.HeroSectionUpdateView.as_view(), name='hero_section_update'),
    path('hero/<int:pk>/delete/', views.HeroSectionDeleteView.as_view(), name='hero_section_delete'),

    # AboutSection URLs
    path('about/', views.AboutSectionListView.as_view(), name='about_section_list'),
    path('about/<int:pk>/', views.AboutSectionDetailView.as_view(), name='about_section_detail'),
    path('about/create/', views.AboutSectionCreateView.as_view(), name='about_section_create'),
    path('about/<int:pk>/update/', views.AboutSectionUpdateView.as_view(), name='about_section_update'),
    path('about/<int:pk>/delete/', views.AboutSectionDeleteView.as_view(), name='about_section_delete'),

    # MenuItem URLs
    path('menu/', views.MenuItemListView.as_view(), name='menuitem_list'),
    path('menu/<int:pk>/', views.MenuItemDetailView.as_view(), name='menuitem_detail'),
    path('menu/create/', views.MenuItemCreateView.as_view(), name='menuitem_create'),
    path('menu/<int:pk>/update/', views.MenuItemUpdateView.as_view(), name='menuitem_update'),
    path('menu/<int:pk>/delete/', views.MenuItemDeleteView.as_view(), name='menuitem_delete'),

    # SpecialOffer URLs
    path('special-offers/', views.SpecialOfferListView.as_view(), name='specialoffer_list'),
    path('special-offers/<int:pk>/', views.SpecialOfferDetailView.as_view(), name='specialoffer_detail'),
    path('special-offers/create/', views.SpecialOfferCreateView.as_view(), name='specialoffer_create'),
    path('special-offers/<int:pk>/update/', views.SpecialOfferUpdateView.as_view(), name='specialoffer_update'),
    path('special-offers/<int:pk>/delete/', views.SpecialOfferDeleteView.as_view(), name='specialoffer_delete'),

    # Testimonial URLs
    path('testimonials/', views.TestimonialListView.as_view(), name='testimonial_list'),
    path('testimonials/<int:pk>/', views.TestimonialDetailView.as_view(), name='testimonial_detail'),
    path('testimonials/create/', views.TestimonialCreateView.as_view(), name='testimonial_create'),
    path('testimonials/<int:pk>/update/', views.TestimonialUpdateView.as_view(), name='testimonial_update'),
    path('testimonials/<int:pk>/delete/', views.TestimonialDeleteView.as_view(), name='testimonial_delete'),

    # Reservation URLs
    path('reservations/', views.ReservationListView.as_view(), name='reservation_list'),
    path('reservations/<int:pk>/', views.ReservationDetailView.as_view(), name='reservation_detail'),


    # Location URLs
    path('locations/', views.LocationListView.as_view(), name='location_list'),
    path('locations/<int:pk>/', views.LocationDetailView.as_view(), name='location_detail'),
    path('locations/create/', views.LocationCreateView.as_view(), name='location_create'),
    path('locations/<int:pk>/update/', views.LocationUpdateView.as_view(), name='location_update'),
    path('locations/<int:pk>/delete/', views.LocationDeleteView.as_view(), name='location_delete'),

    # FAQ URLs
    path('faqs/', views.FAQListView.as_view(), name='faq_list'),
    path('faqs/<int:pk>/', views.FAQDetailView.as_view(), name='faq_detail'),
    path('faqs/create/', views.FAQCreateView.as_view(), name='faq_create'),
    path('faqs/<int:pk>/update/', views.FAQUpdateView.as_view(), name='faq_update'),
    path('faqs/<int:pk>/delete/', views.FAQDeleteView.as_view(), name='faq_delete'),

    # NewsletterSubscription URLs
    path('newsletter/', views.NewsletterSubscriptionListView.as_view(), name='newslettersubscription_list'),
    path('newsletter/<int:pk>/', views.NewsletterSubscriptionDetailView.as_view(), name='newslettersubscription_detail'),


    # GalleryImage URLs
    path('gallery/', views.GalleryImageListView.as_view(), name='galleryimage_list'),
    path('gallery/<int:pk>/', views.GalleryImageDetailView.as_view(), name='galleryimage_detail'),
    path('gallery/create/', views.GalleryImageCreateView.as_view(), name='galleryimage_create'),
    path('gallery/<int:pk>/update/', views.GalleryImageUpdateView.as_view(), name='galleryimage_update'),
    path('gallery/<int:pk>/delete/', views.GalleryImageDeleteView.as_view(), name='galleryimage_delete'),

    # ContactInfo URLs
    path('contact-info/', views.ContactInfoListView.as_view(), name='contactinfo_list'),
    path('contact-info/<int:pk>/', views.ContactInfoDetailView.as_view(), name='contactinfo_detail'),
    path('contact-info/create/', views.ContactInfoCreateView.as_view(), name='contactinfo_create'),
    path('contact-info/<int:pk>/update/', views.ContactInfoUpdateView.as_view(), name='contactinfo_update'),
    path('contact-info/<int:pk>/delete/', views.ContactInfoDeleteView.as_view(), name='contactinfo_delete'),

    # SocialMedia URLs
    path('social-media/', views.SocialMediaListView.as_view(), name='socialmedia_list'),
    path('social-media/<int:pk>/', views.SocialMediaDetailView.as_view(), name='socialmedia_detail'),
    path('social-media/create/', views.SocialMediaCreateView.as_view(), name='socialmedia_create'),
    path('social-media/<int:pk>/update/', views.SocialMediaUpdateView.as_view(), name='socialmedia_update'),
    path('social-media/<int:pk>/delete/', views.SocialMediaDeleteView.as_view(), name='socialmedia_delete'),

]