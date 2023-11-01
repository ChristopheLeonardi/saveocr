from django import forms
from .models import Upload_Image, SearchText
#DataFlair #File_Upload
class Upload_Form(forms.ModelForm):
    class Meta:
        model = Upload_Image
        fields = [ 'image' ] 
        labels = { "image":  "Uploadez l'image à rechercher" }
class SearchTextForm(forms.ModelForm):
    class Meta:
        model = SearchText  
        fields = ['text_search']