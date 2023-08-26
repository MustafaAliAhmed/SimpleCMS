from django import forms

from . models import Pages

class ProductForm(forms.ModelForm):
    class Meta:
        model = Pages
        fields = ['url' ,'title' ,'category' ,'image' ,'seo_tags' ,'content' ,'author_user' ,]
        widgets = {
            'url': forms.URLInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'seo_tags': forms.Textarea(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'author_user': forms.Select(attrs={'class': 'form-control'}),

        }
        labels = {
            'url': 'enter a url',
            'title': 'enter the title',
            'category': 'selecte category',
            'image': 'Select an Image',
            'seo_tags': 'enter a seo tags',
            'content': 'enter a content',
            'author_user': 'select user',
        }
   


 
  