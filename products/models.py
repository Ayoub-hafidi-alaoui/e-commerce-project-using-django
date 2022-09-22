from distutils.command.upload import upload
from itertools import product
from random import choices
from tabnanny import verbose
from django.db import models
from django.utils.translation import  gettext as _
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.

PRODUCT_FLAG = (
    ("New", "New"),
    ("Feature", "Feature"),
    ("Sale", "Sale")
)

class Product(models.Model):
    name = models.CharField(_("name"), max_length=100)
    sku = models.IntegerField(_("sku"))
    subtitle = models.CharField(_("subtitle"), max_length=300)
    desc = models.TextField(_('description'), max_length=10000)
    image = models.ImageField(upload_to="products")
    flag = models.CharField(_("flag"), max_length=100, choices=PRODUCT_FLAG)
    price = models.FloatField(_("price"))
    tags = TaggableManager()
    category = models.ForeignKey('Category', verbose_name = _("category"), related_name="product_category" , on_delete=models.SET_NULL, null=True, blank=True)
    brand = models.ForeignKey('Brand', verbose_name = _("brand"), related_name="product_brand", on_delete=models.SET_NULL, null=True, blank=True)
    video_url = models.URLField(_("video_url"), max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.name


class ProductImages(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("Product"), related_name="product_image", on_delete=models.CASCADE)
    image = models.ImageField(_("image"), upload_to='productImages', height_field=None, width_field=None, max_length=None)
    
    def __str__(self):
        return str(self.product)
    

class Category(models.Model):
    name = models.CharField(_("name"), max_length=100)
    image = models.ImageField(_("image"), upload_to='category')
    
    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(_("name"), max_length=100)
    image = models.ImageField(_("image"), upload_to='brand')
    
    def __str__(self):
        return self.name
    
    
class ProductReview(models.Model):
    user = models.ForeignKey(User, verbose_name=_("user"), related_name="user_review", on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, verbose_name=_("product"), related_name="product_review", on_delete=models.SET_NULL, null=True, blank=True)
    rate = models.IntegerField(verbose_name=_("rate"))
    review = models.CharField(max_length=100, verbose_name=_("review"))
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.product)
     
    