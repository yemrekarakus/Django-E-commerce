from django.shortcuts import render
from django.contrib import messages
from .models import Carousel
from .forms import CarouselModelForm


def index(request):
    context = dict()
    context['images'] = Carousel.objects.filter(status="published")
    # context['images'] = images
    return render(request, 'home/index.html', context)


# stuff not checked
def carousel_create(request):
    context = dict()
    # item = Carousel.objects.first()
    # context['form'] = CarouselModelForm(instance=item)
    context['form'] = CarouselModelForm()
    if request.method == 'POST':
        print(request.POST)
        # print(request.FILES['cover_image'])
        carousel = Carousel.objects.create(
            title = request.POST.get('title')
        )
        form = CarouselModelForm(request.POST, files=request.FILES)
        # print(form)
        if form.is_valid():
            form.save()
    
        messages.success(request, 'Birseyler eklendi ama ne oldu bilemiyorum')
    return render(request, 'manage/carousel_create.html', context)

def carousel_list(request):
    context = dict()
    context['carousel'] = Carousel.objects.all()
    return render(request, 'manage/carousel_list.html', context)


def carousel_update(request):
    context = dict()
    item = Carousel.objects.get(pk=pk)
    return render(request, 'manage/carousel_update.html', context)


