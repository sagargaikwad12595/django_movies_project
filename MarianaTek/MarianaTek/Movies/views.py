from django.shortcuts import render,HttpResponse
import json
# Create your views here.


def movies(request):
        
    fd = open("Movies/index.json")
    data = json.load(fd)
    search_query = ''
    
    if request.method == 'POST':
        search_query = request.POST['search']
        
    result = []
    genres_list = []
    for each in data:
        for movie in each['movies']:
            if search_query and search_query == movie['title']:
                genres = ''
                for genre in movie['genre']:
                    if genres:
                        genres = genres + ', '+ genre
                    else:
                        genres = genre
                    
                    if genre not in genres_list:
                        genres_list.append(genre)          
                movie_data = {
                    'title' : movie['title'],
                    'poster' : movie['poster'],
                    'genre' : genres,
                    'rating' : movie['imdb_rating'],
                    'year_release' : movie['released'],
                    'metacritic_rating' : movie['meta_score'],
                    'runtime' : movie['runtime']
                }
                result.append(movie_data)
                return render(request,"movies.html",context={'data':result,'genres_list':genres_list})
                
            if not search_query:
                genres = ''
                for genre in movie['genre']:
                    if genres:
                        genres = genres + ', '+ genre
                    else:
                        genres = genre
                    if genre not in genres_list:
                        genres_list.append(genre)    
                movie_data = {
                    'title' : movie['title'],
                    'poster' : movie['poster'],
                    'genre' : genres,
                    'rating' : movie['imdb_rating'],
                    'year_release' : movie['released'],
                    'metacritic_rating' : movie['meta_score'],
                    'runtime' : movie['runtime']
                }
                result.append(movie_data)
    
    return render(request,"movies.html",context={'data':result,'genres_list':genres_list})


def getMatchMovie(request):
    if request.method == 'GET':
        searchInput = request.GET['searchInput']
        result = []
        genres_list = []
        fd = open("Movies/index.json")
        data = json.load(fd)
        for each in data:
            for movie in each['movies']:
                if searchInput in movie['title']:
                    genres = ''
                    for genre in movie['genre']:
                        if genres:
                            genres = genres + ', '+ genre
                        else:
                            genres = genre
                        if genre not in genres_list:
                            genres_list.append(genre)      
                        movie_data = {
                            'title' : movie['title'],
                            'poster' : movie['poster'],
                            'genre' : genres,
                            'rating' : movie['imdb_rating'],
                            'year_release' : movie['released'],
                            'metacritic_rating' : movie['meta_score'],
                            'runtime' : movie['runtime']
                        }

                        
                        result.append(movie_data)
        
        if result:
            done = set()
            res = []
            for d in result:
                if d['title'] not in done:
                    done.add(d['title']) 
                    res.append(d)
        

    return HttpResponse(json.dumps(res))

def getMoviesByGenre(request):

    
    fd = open("Movies/index.json")
    data = json.load(fd)
    res = []
    result = []
    genres_list = []
    for each in data:
        for movie in each['movies']:
            if request.GET.get('filter_text') and request.GET.get('filter_text') in movie['genre']:
                genres = ''
                for genre in movie['genre']:
                    
                    if genres:
                        genres = genres + ', '+ genre
                    else:
                        genres = genre
                    
                    if genre not in genres_list:
                        genres_list.append(genre)          
                movie_data = {
                    'title' : movie['title'],
                    'poster' : movie['poster'],
                    'genre' : genres,
                    'rating' : movie['imdb_rating'],
                    'year_release' : movie['released'],
                    'metacritic_rating' : movie['meta_score'],
                    'runtime' : movie['runtime']
                }
                result.append(movie_data)
    
    if result:
            done = set()
            res = []
            for d in result:
                if d['title'] not in done:
                    done.add(d['title']) 
                    res.append(d)
        

    return HttpResponse(json.dumps(res))
