from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Project, Task, Client
from .forms import ProjectForm,TaskForm,ClientForm, CustomUserCreationForm,SubmissionForm
from django.contrib.auth.decorators import user_passes_test


admin_required = user_passes_test(lambda u: u.is_superuser, login_url='/login/')


@admin_required
def homefn(request):
    total_projects = Project.objects.count()
    total_tasks = Task.objects.count()
    completed_tasks = Task.objects.filter(status='Completed').count()
    total_clients = Client.objects.count()

    context = {
        "total_projects": total_projects,
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        'total_clients': total_clients,
    }

    return render(request, "home.html", context)




def signupfn(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})




def loginfn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect('/home/')
            return redirect('/mytasks/')

        return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

@login_required
def logoutfn(request):
    logout(request)
    return redirect('/')




@admin_required
def projectcreatefn(request):
    if request.method=='POST':
        f=ProjectForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/home/')

    else:
        f=ProjectForm()
        return render(request,'projectcreate.html',{'fm':f})
    
@admin_required
def projectlistfn(request):
    projects = Project.objects.all()
    return render(request, 'projectlist.html', {'projects': projects})

@admin_required
def projectupdatefn(request, id):
    project = Project.objects.get(id=id)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('/projectlist/')
    else:
        form = ProjectForm(instance=project)

    return render(request, 'projectform.html', {'form': form})

@admin_required
def projectdeletefn(request, id):
    project = Project.objects.get(id=id)
    project.delete()
    return redirect('/projectlist/')

@admin_required
def taskcreatefn(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tasklist/')
    else:
        form = TaskForm()

    return render(request, 'taskform.html', {'form': form})


from django.db.models import Q

def tasklistfn(request):
    query = request.GET.get('q')

    tasks = Task.objects.all() 
    if query:
        tasks = tasks.filter(
            Q(title__icontains=query) |
            Q(project__name__icontains=query) |
            Q(status__icontains=query) |
            Q(assigned_to__username__icontains=query)
        )
    return render(request, 'tasklist.html', {'tasks': tasks})

    


@admin_required
def taskupdatefn(request, id):
    task = Task.objects.get(id=id)

    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task)  
        if form.is_valid():
            form.save()
            return redirect('/tasklist/')
    else:
        form = TaskForm(instance=task)

    return render(request, 'taskform.html', {'form': form})


@admin_required
def taskdeletefn(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/tasklist/')



@admin_required
def clientcreatefn(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/clientlist/')
    else:
        form = ClientForm()

    return render(request, 'clientform.html', {'form': form})


@admin_required
def clientlistfn(request):
    clients = Client.objects.all()
    return render(request, 'clientlist.html', {'clients': clients})

@admin_required
def clientupdatefn(request, id):
    client = Client.objects.get(id=id)

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('/clientlist/')
    else:
        form = ClientForm(instance=client)

    return render(request, 'clientform.html', {'form': form})


@admin_required
def clientdeletefn(request, id):
    client = Client.objects.get(id=id)
    client.delete()
    return redirect('/clientlist/')


@admin_required
def calendarview(request):
    tasks = Task.objects.all().order_by('due_date')
    return render(request, 'calendar.html', {'tasks': tasks})



@admin_required
def reportview(request):
    total_projects = Project.objects.count()
    completed_projects = Project.objects.filter(status='Completed').count()
    pending_projects = Project.objects.filter(status='Pending').count()

    total_tasks = Task.objects.count()

    context = {
        'total_projects': total_projects,
        'completed_projects': completed_projects,
        'pending_projects': pending_projects,
        'total_tasks': total_tasks,
    }

    return render(request, 'report.html', context)



@login_required
def mytasks(request):
    tasks = Task.objects.filter(assigned_to=request.user)
    return render(request, 'mytasks.html', {'tasks': tasks})


def submittask(request, id):
    task = Task.objects.get(id=id)

    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            task.status = "Completed"
            form.save()
            return redirect('/mytasks/')
    else:
        form = SubmissionForm(instance=task)

    return render(request, 'submit.html', {'form': form})