from django.shortcuts import render,redirect
from .models import Article,Comment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
register_form = UserCreationForm()
login_form = AuthenticationForm()
context = {
    'register_form': register_form,
    'login_form': login_form
    }
def article(request):
    articles=Article.objects.all().order_by('date')
    global context
    context.update({'articles':articles})
    return render(request,'article/article.html', context)


def details(request,slug):
    article =Article.objects.get(slug=slug)
    comment =Comment.objects.filter(article=article)
    form = forms.CreateComment()
    if request.method == 'POST':
        if request.user.is_authenticated :
            comment = forms.CreateComment(request.POST,request.FILES)
            instance = comment.save(commit=False)
            instance.author = request.user
            instance.article = article
            instance.save()
            comment = Comment.objects.filter(article=article)
            return render(request, 'article/details.html', {'article': article, 'comment': comment, 'form': form})
        else:
            return redirect('user:signin')
    else:
        return render(request,'article/details.html',{'article':article,'comment':comment,'form':form})


@login_required
def create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('article:home')
    else:
        form = forms.CreateArticle()
    return render(request,'article/create.html',{'form':form})
