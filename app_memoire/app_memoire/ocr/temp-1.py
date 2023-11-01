
            """ for entry in ocr_analyze:
                term = entry[0]
                #term = entry
                #print(term)
                # print(Author.objects.filter(author=entry(0)))

                if entry[1] > 0.6:
                #if entry > 0.7:

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
                                author_query = Author.objects.filter(author_id=author_id[0].author_id)
                            except:
                                pass                       

                    if len(author_query):
                        author_id = author_query[0].author_id
                        wikidata_response = [vars(entry) for entry in WikidataAuthor.objects.filter(author_id=author_id)]
                        response = [vars(entry) for entry in author_query]
                        results.append([wikidata_response, response])
                        
                    # artwork Queriestemp
                    artwork_query = MusicArtwork.objects.filter(name=term)

                    if len(artwork_query) == 0 :
                        artwork_query = RejectedArtwork.objects.filter(rejected_name=term)

                    if len(artwork_query):
                        response = [vars(entry) for entry in author_query]
                        results.append(response)
                                           
            return render(request, 'details.html', {'user_pr': user_pr, 'keyword': list_text, 'query_results': results}) """


Add views / forms / template / url / 
add from django.views.decorators.csrf import csrf_protect // {% csrf_token %}
