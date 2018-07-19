from django.shortcuts import render, get_object_or_404
from .models import Post
#from spider.models import Post

def post_list(request):
    #posts = Post.objects.filter(name=name).order_by('name')
    posts =  Post.objects.order_by('name')
    return render(request, 'spider/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)    
    return render(request, 'spider/post_detail.html', {'post': post})

def genre_list(request):
    genries = Post.objects.all().values('genre').distinct()
    return render(request, 'spider/genre_list.html', {'items': genries})

def genre(request):
    genre = request.GET.get('genre')
    genries = Post.objects.filter(genre__icontains=genre).order_by('name')   
    return render(request, 'spider/genre.html', {'items': genries, 'genre': genre})

def country_list(request):
    contries = Post.objects.all().values('country').distinct()
    return render(request, 'spider/country_list.html', {'items': contries})

def country(request):
    country = request.GET.get('country')
    contries = Post.objects.filter(country__icontains=country).order_by('name')   
    return render(request, 'spider/country.html', {'items': contries, 'country': country})    

def city_list(request):
    cities = Post.objects.all().values('city').distinct()
    return render(request, 'spider/city_list.html', {'items': cities})

def city(request):
    city = request.GET.get('city')
    cities = Post.objects.filter(city__icontains=city).order_by('name')   
    return render(request, 'spider/city.html', {'items': cities, 'city': city})    
    
def bitrate_list(request):
    bitrates = Post.objects.all().values('bitrate').distinct()
    return render(request, 'spider/bitrate_list.html', {'items': bitrates})

def bitrate(request):
    bitrate = request.GET.get('bitrate')
    bitrates = Post.objects.filter(bitrate__icontains=bitrate).order_by('name')   
    return render(request, 'spider/bitrate.html', {'items': bitrates, 'bitrate': bitrate})  