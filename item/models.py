from django.db import models
from django.contrib.auth.models import User
# Create table Category
class Category(models.Model):
    name = models.CharField(max_length=255)

    # Change table name and order by name
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    # Change items name
    def __str__(self):
        return self.name

# Field creation on items table
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    # If an user is deleted, the related items is also deleted 
    created_by = models.ForeignKey(User, related_name='items', on_delete= models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'item')

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('user', 'item')