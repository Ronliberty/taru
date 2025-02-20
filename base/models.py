from django.db import models

class HeroSection(models.Model):
    title = models.CharField(max_length=255, default="Welcome to Our Restaurant")
    paragraph = models.TextField(default="Experience the finest dining with our exquisite menu and cozy ambiance.")
    background_image = models.ImageField(upload_to='hero_images/', blank=True, null=True)

    def __str__(self):
        return self.title
        
class AboutSection(models.Model):
    title = models.CharField(max_length=255, default="About Us")
    subtitle = models.CharField(max_length=255, default="Our Journey, Your Delight")
    paragraph1 = models.TextField(default="Welcome to [Your Restaurant Name], where passion meets flavor! Our story began with a simple dream: to create a dining experience that celebrates the art of cooking and the joy of sharing meals. Inspired by [specific inspiration, e.g., family recipes, cultural heritage, or a love for fresh ingredients], we craft every dish with care and creativity.")
    paragraph2 = models.TextField(default="What makes our food special? It’s the perfect blend of tradition and innovation. We source the finest ingredients, often locally and sustainably, to ensure every bite is bursting with freshness and flavor. From our signature [specific dish] to our ever-evolving seasonal menu, we strive to bring you a culinary journey that delights the senses.")
    paragraph3 = models.TextField(default="But it’s not just about the food—it’s about the people. Our team is dedicated to making every visit memorable, whether you’re joining us for a casual lunch, a romantic dinner, or a special celebration. At [Your Restaurant Name], you’re not just a guest; you’re part of our story.")

    def __str__(self):
        return self.title
        
        
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='menu_images/', default='default.jpg')

    def __str__(self):
        return f"{self.name} - ${self.price}"
        
class SpecialOffer(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    details = models.TextField()
    time_limit = models.CharField(max_length=255, help_text="E.g., 'Limited time offer until Sunday!'")

    def __str__(self):
        return self.title
        
class Testimonial(models.Model):
    customer_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    rating = models.PositiveIntegerField(default=5, choices=[(i, f"{'★' * i}") for i in range(1, 6)])
    review = models.TextField()

    def __str__(self):
        return f"{self.customer_name} - {self.rating} Stars"
        
        
class Reservation(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    date_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation by {self.name} on {self.date_time.strftime('%Y-%m-%d %H:%M')}"
        
class Location(models.Model):
    name = models.CharField(max_length=255, help_text="Name of the restaurant or location")
    map_embed_link = models.URLField(help_text="Google Maps embed link")

    def __str__(self):
        return self.name
        
        
class FAQ(models.Model):
    question = models.CharField(max_length=255, help_text="Enter the FAQ question")
    answer = models.TextField(help_text="Enter the answer to the FAQ question")

    def __str__(self):
        return self.question
        
class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True, help_text="Enter a valid email address")
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
        
        
class GalleryImage(models.Model):
    image = models.ImageField(upload_to="gallery/", help_text="Upload a gallery image")
    caption = models.CharField(max_length=255, help_text="Short caption for the image")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption
        
        
class ContactInfo(models.Model):
    email = models.EmailField(unique=True, help_text="Business email address")
    phone_number = models.CharField(max_length=20, help_text="Contact phone number")
    address = models.TextField(blank=True, help_text="Business address (optional)")

    def __str__(self):
        return self.email
        
class SocialMedia(models.Model):
    facebook = models.URLField(blank=True, help_text="Facebook profile or page URL")
    instagram = models.URLField(blank=True, help_text="Instagram profile URL")
    twitter = models.URLField(blank=True, help_text="Twitter (X) profile URL")

    def __str__(self):
        return "Social Media Links"