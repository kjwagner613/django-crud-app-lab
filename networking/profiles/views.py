from pyexpat.errors import messages
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserProfile
from .forms import UserProfileForm
from django.shortcuts import render, redirect
from .forms import UserRegisterForm



class HomeView(TemplateView):
    template_name = 'home.html'

class UserProfileListView(ListView):
    model = UserProfile
    template_name = 'profiles/userprofile_list.html'
    context_object_name = 'userprofiles'

class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'profiles/userprofile_detail.html'

class UserProfileCreateView(LoginRequiredMixin, CreateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'profiles/userprofile_form.html'
    success_url = reverse_lazy('profile_list')

class UserProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'profiles/userprofile_form.html'
    success_url = reverse_lazy('profile_list')

class UserProfileDeleteView(DeleteView):
    model = UserProfile
    template_name = 'profiles/userprofile_confirm_delete.html'
    success_url = reverse_lazy('profile_list')



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # Consider adding a success message before redirecting
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
        else:
            # Handling form errors
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
