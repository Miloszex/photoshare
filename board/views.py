from django.shortcuts import render
from .forms import PostForm
from models import Image
# Create your views here.

def post_image(request):

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.instance.user = request.user
            form.save()
            return render(request, 'board/upload_success.html', {'message':'Success!'})
    else:
        form = PostForm()

    return render(request, 'board/post_image.html',{'form':form})

def showMyPhotos(request):

    my_photos = Image.objects.all().filter(user=request.user.id)

    return render(request, 'board/my_photos.html', {'my_photos': my_photos})