from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse  
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task,NoteApp,Remainder 
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RemainderForm


# Create your views here.
@login_required(login_url='login')

def source(request):
    return render(request,"main/source.html")

def notes(request):
    return render(request,"main/notes.html")

@login_required(login_url='signin')

def noteapp(request):
    user_notes = NoteApp.objects.filter(user=request.user)
    docid = int(request.GET.get('docid',0))
    documents = user_notes.order_by('-id')

    if request.method == "POST":
        docid = int(request.POST.get('docid',0))
        title = request.POST.get('title')
        content = request.POST.get('content','')

        if docid > 0:
            document = get_object_or_404(user_notes,pk=docid)
            document.title = title
            document.content = content
            document.save()

            return redirect('noteapp' % docid)
        else:
            document = NoteApp.objects.create(user=request.user,title=title,content=content)
            return redirect('noteapp')
 

    if docid > 0:
        document = get_object_or_404(user_notes,pk=docid)
    else:
        document = ''


    context = {
        'docid': docid,
        'documents': documents,
        'document':document
    }

    return render(request,"main/noteapp.html",context)

def delete_document(request,docid):
    document = NoteApp.objects.get(pk=docid)
    document.delete()

    return redirect('noteapp')

def signup(request):

    if request.method == "POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')

        myuser = User.objects.create_user(username,email,password1)
        myuser.save()

        return redirect('signin')


    return render(request,"main/signup.html")

def signin(request):
    
    if request.method =="POST":
        username=request.POST.get('username')
        password1=request.POST.get('pass')

        user=authenticate(username=username,password=password1)

        if user is not None:
            login(request,user)
            return redirect('source')

        else:
            messages.error(request,"BAD CREDENTIALS!")
            return redirect('signup')


    return render(request,"main/signin.html")


def logoutpage(request):
    logout(request)
    return redirect('signin')

#def add_note(request):
  #  if request.method == 'POST':
   #     title = request.POST['title']
    #    description = request.POST['description']
     #   note = Notes(title=title,description=description)
      #  note.save()
       # return redirect('notes.html')

def timer(request):
    return render(request,"main/timer.html")

def calender(request):
    return render(request,"main/calender.html")




class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = self.get_queryset().values()
        context['tasks'] = self.get_queryset().values().count() 
        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'main/task.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(TaskCreate,self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

#---------------------------------------- Remainder View -----------------------------------#

@login_required
def create_remainder(request):
    if request.method == "POST":
        form = RemainderForm(request.POST)
        if form.is_valid():
            remainder = form.save(commit=False)
            remainder.user = request.user
            remainder.save()
            return redirect("list")

    else:
        form = RemainderForm()
    return render(request,'main/create.html',{'form':form})

@login_required

def remainder_list(request):
    remainders = Remainder.objects.filter(user=request.user)
    return render(request,'main/remainder_list.html',{"remainders":remainders})