from django.shortcuts import render,redirect
from form_app.forms import *
from form_app.models import *
# Create your views here.
def home_view(request):

    return render(request, 'home.html')


def blog_list_view(request):
    data= BlogModel.objects.all()

    context = {'data':data}
    return render(request,'blog-list.html',context)

def blog_add_view(request):
    form_data = BlogForm()
    if request.method == "POST":
        form_data = BlogForm(request.POST, request.FILES)
        if form_data.is_valid():
            form_data.save()
            return redirect('blog_list_view')
    context = {
        'form_data' : form_data
    }
    return render(request, 'blog-add.html', context)
