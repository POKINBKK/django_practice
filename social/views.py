from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms import formset_factory
from django.shortcuts import render, redirect


from social.forms import StatusForm, CommentForm
from social.models import Comment


def index(request):
    context = {}
    return render(request, 'social/index.html', context=context)

def my_login(request):
    context = {}
    next = request.POST.get('next')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            print(next)
            if next:
                return redirect(next)
            else:
                return redirect('index')
        else:
            context['username'] = username
            context['error'] = 'Wrong username or password'

    return render(request, 'social/login.html', context=context)

@login_required
def createpost(request):
    context = {}
    CommentFormSet = formset_factory(CommentForm, extra=3)
    if request.method == 'POST':
        form = StatusForm(request.POST)
        print(form.is_valid())
        formset = CommentFormSet(request.POST)
        if form.is_valid():
            print(1)

            obj = form.save(commit=False)
            obj.writer_id = (User.objects.get(username=request.user.username)).id
            obj.save()

            if formset.is_valid():
                print(2)
                for comment_form in formset:
                    obj2 = comment_form.save(commit=False)
                    obj2.status_id = obj.id
                    obj2.save()

                return redirect('index')
    else:
        form = StatusForm()
        formset = CommentFormSet()
    context['form'] = form
    context['formset'] = formset
    return  render(request, 'social/createpost.html', context=context)

def my_logout(request):
    logout(request)
    return redirect('index')

