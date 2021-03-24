from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from authentication.forms import SignUpForm
from django.contrib.auth.models import User
from feeds.models import Feed
from django.views.generic import CreateView

class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        welcome_post = u'{0} has joined the network.'.format(user.username, user.username)
        feed = Feed(user=user, post=welcome_post)
        feed.save()

        return redirect('home')

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if not form.is_valid():
#             return render(request, 'authentication/signup.html', {'form': form})
#         else:
#             username = form.cleaned_data.get('username')
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password')
#             User.objects.create_user(username=username, password=password, email=email)
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             welcome_post = u'{0} has joined the network.'.format(user.username, user.username)
#             feed = Feed(user=user, post=welcome_post)
#             feed.save()
#             return redirect('/')
#     else:
#         return render(request, 'authentication/signup.html', {'form': SignUpForm()})
