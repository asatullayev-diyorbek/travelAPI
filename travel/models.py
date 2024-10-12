from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Kateqoriya'
        verbose_name_plural = 'Kateqoriyalar'


class Tour(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)  # Joylashuv
    duration = models.PositiveIntegerField(help_text="Kunlar soni")  # Davomiyligi kunlarda
    start_date = models.DateField()  # Boshlanish sanasi
    end_date = models.DateField()  # Tugash sanasi
    availability = models.BooleanField(default=True)  # Mavjudlik
    image = models.ImageField(upload_to='tour/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Turi'
        verbose_name_plural = 'Turlar'


class Hotel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)  # Joylashuv
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)  # Reyting (masalan, 4.5)
    availability = models.BooleanField(default=True)  # Mavjudlik
    image = models.ImageField(upload_to='hotel/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Mehmonxona'
        verbose_name_plural = 'Mehmonxonalar'

    def get_image(self):
        if self.image:
            return self.image.url
        else:
            return '/media/default.jpg'


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)  # Tavsif
    video_url = models.URLField()
    upload_date = models.DateField(auto_now_add=True)  # Yuklangan sana
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='videos')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videolar'
