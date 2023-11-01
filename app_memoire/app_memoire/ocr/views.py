from django.shortcuts import redirect, render
from django.http import HttpResponse
from .extract_text import extract_text
from .forms import Upload_Form, SearchTextForm
from .models import Upload_Image, Author, WikidataAuthor, MusicArtwork, RejectedAuthor, RejectedArtwork, SearchText
from django.views.decorators.csrf import csrf_protect
from django.conf import settings
from autocorrect import Speller
from rich import print
#import keras_ocr
import os
import glob
import time
import io
import uuid
from PIL import Image, ExifTags
from django.conf import settings
from skimage.transform import resize
from django.core.files import File
from pathlib import Path
from PIL import Image
from io import BytesIO
import time


@csrf_protect
def results(request):

    start_time = time.time()
    if request.method == "POST":
        form = SearchTextForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            term = form.cleaned_data['text_search']
            response = []

            # Author Queries
            author_query = Author.objects.filter(author=term)
            if len(author_query) == 0 :
                author_query = RejectedAuthor.objects.filter(rejected_name=term)
                
            if len(author_query) == 0 :
                try:
                    author_id = Author.objects.raw(f'SELECT author_id FROM author WHERE soundex(author) like soundex("{term}")')
                    author_query = Author.objects.filter(author_id=author_id[0].author_id)
                except:
                    try:
                        author_id = RejectedAuthor.objects.raw(f'SELECT author_id FROM rejected_author WHERE soundex(rejected_name) like soundex("{term}")')
                        author_query = Author.objects.filter(authorid=author_id[0].author_id)
                    except:
                        pass 

            response.append(author_query)           
            if len(author_query):
                author_id = author_query[0].author_id

                # Wikidata entries
                wikidata_response = WikidataAuthor.objects.filter(author_id=author_id)
                response.append(wikidata_response)

                # Artwork list
                artwork_response = MusicArtwork.objects.filter(author_0_id=author_id)
                response.append(artwork_response)
                
            # artwork Queriestemp
            #artwork_query = MusicArtwork.objects.filter(name=term)

            """ if len(artwork_query) == 0 :
                artwork_query = RejectedArtwork.objects.filter(rejected_name=term)

            if len(artwork_query):
                results = [vars(entry) for entry in artwork_query]
                response.append(results) """
            try:
                author_data = author_query[0]
            except:
                author_data = []
            try:
                wiki_data = wikidata_response[0]
            except:
                wiki_data = []

            music_data = artwork_response 


            print("--- Query Response : %s seconds ---" % (time.time() - start_time))
            return render(request, 'details.html', {'author_data':author_data,
                                                    'wiki_data':wiki_data,
                                                    'music_data':music_data,
                                                    })

    return render(request, "details.html")
  

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
@csrf_protect
def image_request(request):  
    
    def rotate_resize_image(filepath, orientation, maxWidth, maxHeight):
        start_time = time.time()
        image = Image.open(filepath)
        try:
            if orientation['num'] == 3:
                image = image.rotate(180, expand=True)
            elif orientation['num'] == 6:
                image = image.rotate(270, expand=True)
            elif orientation['num'] == 8:
                image = image.rotate(90, expand=True)

        except (AttributeError, KeyError, IndexError):
            print(AttributeError, KeyError, IndexError)
            # cases: image don't have getexif
            pass

        image.thumbnail((maxWidth, maxHeight), Image.ANTIALIAS)
        image.save(filepath)
        print("--- Rotate/Resize : %s seconds ---" % (time.time() - start_time))


    form = Upload_Form()
    if request.method == 'POST':
        form = Upload_Form(request.POST, request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.image = request.FILES['image']
            file_type = user_pr.image.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                return render(request, 'error.html')
            user_pr.save()

            is_file_exists = os.path.exists(user_pr.image.url)

            exif = user_pr.exif
            try:
                orientation = exif.get('Orientation')
            except KeyError:
                orientation = 'unknown'
                
            print(orientation)
            rotate_resize_image(user_pr.image.url, orientation, 400, 400)
            ocr_analyze = extract_text(user_pr.image.url)
            #ocr_analyze = [("Franz Schubert", 0.9)]

            list_text = [text[0] for text in ocr_analyze]
            spell = Speller(lang='fr')

            return render(request, 'select.html', {'user_pr': user_pr, 'keyword': list_text})
            results = []
            

    context = {"form": form,}
    return render(request, 'image_form.html', context) 




