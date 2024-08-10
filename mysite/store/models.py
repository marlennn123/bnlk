from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=32)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, verbose_name='В наличии')
    video = models.FileField(upload_to='product_videos/', null=True, blank=True)

    DELIVERY_CHOICES = (
        ('Самовывоз', 'Самовывоз'),
        ('Платная доставка', 'Платная доставка')
    )

    delivery = models.CharField(max_length=32, choices=DELIVERY_CHOICES, default='Самовывоз')

    def __str__(self):
        return self.product_name


class ProductPhotos(models.Model):
    image = models.ImageField(upload_to='product_images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.CharField(max_length=16)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.product}'