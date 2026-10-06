from django.shortcuts import render,redirect,get_object_or_404
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

def blog_edit_view(req,id):
    blog_data = get_object_or_404(BlogModel, id = id )
    form_data = BlogForm(instance=blog_data)
    if req.method == 'POST':
        form_data = BlogForm(req.POST,req.FILES,instance=blog_data)
        if form_data.is_valid():
            form_data.save()
            return redirect('blog_list_view')

    return render(req, 'blog-edit.html', {'form_data':form_data})


