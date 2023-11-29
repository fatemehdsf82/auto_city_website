# from django.urls import reverse_lazy
# from django.views import generic
# from django.contrib.auth.forms import UserCreationForm


# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm()
#     template_name = 'registration/signup.html'
#     success_url = reverse_lazy('login')


# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth import login, authenticate, logout
# from .forms import SignUpForm
# from django.urls import reverse_lazy


# def SignUpView(request):
#     if request.method == 'GET':
#         form = SignUpForm()
#         return render(request, 'registration/signup.html', { 'form': form})

#     success_url = reverse_lazy('login')


# true

# from django.shortcuts import render, redirect
# from django.contrib.auth import login
# from .forms import SignUpForm


# def signup(request):
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect("login")  # Redirect to the home page after signup
#     else:
#         form = SignUpForm()
#     return render(request, "registration/signup.html", {"form": form})
