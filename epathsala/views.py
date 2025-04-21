from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import EbookForm,Createuserform,AudiobookForm
from django.db.models import Q 
from .models import Ebook,comment,audiobook

# Create your views here.
def index(request):
    return render(request, 'index.html')

def iamebook(request):
    search_query = request.GET.get('search', '')
    ebooks=Ebook.objects.all()
    if search_query:
        ebooks = ebooks.filter(Q(name__icontains=search_query))
    return render(request, 'iamebook.html', {'ebooks': ebooks})
    
@login_required
def home(request):
 return render(request, "home.html", {})


def authView(request):
 if request.method == "POST":
  form = Createuserform(request.POST or None)
  if form.is_valid():
   form.save()
   return redirect("base:login")
 else:
  form = Createuserform
 return render(request, "registration/signup.html", {"form": form})

@login_required
def upload_ebook(request):
    if request.method == "POST":
        form = EbookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('base:home')
    else:
        form = EbookForm()
        return render(request, 'upload_ebook.html', {'form': form})
@login_required
def ebook_list(request):
    search_query = request.GET.get('search', '')
    ebooks=Ebook.objects.all()
    if search_query:
        ebooks = ebooks.filter(Q(name__icontains=search_query))

    return render(request, 'ebook_list.html', {'ebooks': ebooks})
@login_required
def contact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email= request.POST.get('email')
        message = request.POST.get('message')
        comment.objects.create(name=name,email=email,message=message)
        return redirect('base:home')
    return render(request, 'contact.html')


# inside ko category haru
@login_required
def action(request):
    ebooks = Ebook.objects.filter(category=4)
    ebooks12 = audiobook.objects.filter(category=4)
    return render(request, 'category/action.html', {'ebooks': ebooks,'ebooks12':ebooks12})
@login_required
def love(request):
    ebooks = Ebook.objects.filter(category=1)
    ebooks12 = audiobook.objects.filter(category=1)
    return render(request, 'category/love.html', {'ebooks': ebooks,'ebooks12':ebooks12})
@login_required
def horror(request):
    ebooks = Ebook.objects.filter(category=2)
    ebooks12 = audiobook.objects.filter(category=2)
    return render(request, 'category/horror.html', {'ebooks': ebooks,'ebooks12':ebooks12})
@login_required
def thriller(request):
    ebooks = Ebook.objects.filter(category=3)
    ebooks12 = audiobook.objects.filter(category=3)
    return render(request, 'category/thriller.html', {'ebooks': ebooks,'ebooks12':ebooks12})


# outside ko category haru
def iaction(request):
    ebooks = Ebook.objects.filter(category=4)
    ebooks12 = audiobook.objects.filter(category=4)
    return render(request, 'category/iaction.html', {'ebooks': ebooks,'ebooks12':ebooks12})
def ilove(request):
    ebooks = Ebook.objects.filter(category=1)
    ebooks12 = audiobook.objects.filter(category=1)
    return render(request, 'category/ilove.html', {'ebooks': ebooks,'ebooks12':ebooks12})
def ihorror(request):
    ebooks = Ebook.objects.filter(category=2)
    ebooks12 = audiobook.objects.filter(category=2)
    return render(request, 'category/ihorror.html', {'ebooks': ebooks,'ebooks12':ebooks12})
def ithriller(request):
    ebooks = Ebook.objects.filter(category=3)
    ebooks12 = audiobook.objects.filter(category=3)
    return render(request, 'category/ithriller.html', {'ebooks': ebooks,'ebooks12':ebooks12})
@login_required
def upload_audiobook(request):
    if request.method == "POST":
        form = AudiobookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('base:home')
    else:
        form = AudiobookForm()
        return render(request, 'upload_audiobook.html', {'form': form})
@login_required   
def audiobook_list(request):
    search_query = request.GET.get('search', '')
    ebooks=audiobook.objects.all()
    if search_query:
        ebooks = ebooks.filter(Q(name__icontains=search_query))

    return render(request, 'audiobook_list.html', {'ebooks': ebooks})

def audiobook_b(request):
    search_query = request.GET.get('search', '')
    ebooks=audiobook.objects.all()
    if search_query:
        ebooks = ebooks.filter(Q(name__icontains=search_query))

    return render(request, 'audiobook/audiobook_b.html', {'ebooks': ebooks})