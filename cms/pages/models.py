from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# import uuid
# Create your models here.
# id = uuid.uuid4

class CategoryPage(models.Model):
    
    name = models.CharField(max_length=30,  blank=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    ref_categoryPage = models.OneToOneField('self',null=True, blank=True, on_delete=models.CASCADE )
    
    
    def __str__(self):
        return self.name

class Pages(models.Model):
    
    url = models.URLField()
    # url = models.CharField(max_length=255, default='', blank=False)
    title = models.CharField(max_length=255, default='', blank=False)
    category = models.ForeignKey(CategoryPage, on_delete=models.CASCADE, default=True, null=False)
    createionDate = models.DateTimeField(auto_now_add=True)
    modifyDate = models.DateTimeField(auto_now= True)
    image = models.ImageField(upload_to='photos/%y/%m/%d',)
    seo_tags = models.TextField()
    content = models.TextField()
    author_user = models.ForeignKey(User, null=True, on_delete= models.SET_NULL)
    published = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.category.name