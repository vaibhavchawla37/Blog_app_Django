from django.shortcuts import render

from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def forms_1(request):
    if request.method =='POST':
        
        data = request.POST
        s = data['title'].replace(' ','-');
        print(data)
        t=Post(title=data['title'],author=data['author'],status=data['find-us'],content=data['message'],slug = s)
        t.save()
    return render(request,'wb/index.html')


# Create your views here.
