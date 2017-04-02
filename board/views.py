from django.shortcuts import render
from .forms import PostForm
# Create your views here.

def post_image(request):

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'board/upload_success.html', {'message':'Success!'})
    else:
        form = PostForm()

    return render(request, 'board/post_image.html',{'form':form})