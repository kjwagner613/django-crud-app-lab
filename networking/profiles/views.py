from django.forms import BaseForm
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import UserProfile
from .forms import UserProfileForm
from django.views.generic import TemplateView

class UserProfileCreateView(CreateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'myapp/userprofile_form.html'  
    success_url = reverse_lazy('home')  


class HomeView(TemplateView):
    template_name = 'home.html'  

    
class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def UserProfile_index(request):
    UserProfile = UserProfile.objects.filter(user=request.user)
    return render(request, 'UserProfiles/index.html', {'UserProfiles': UserProfiles})

@login_required
def UserProfile_detail(request, UserProfile_id):
    UserProfile = UserProfile.objects.get(id=UserProfile_id)
    cast_form = BaseForm()
    return render(request, 'UserProfiles/detail.html', {
        'UserProfile': UserProfile, 'cast_form': cast_form
    })

@login_required
def add_cast(request, UserProfile_id):
    form = BaseForm(request.POST)

    if form.is_valid():
        new_cast = form.save(commit=False)
        new_cast.UserProfile_id = UserProfile_id
        new_cast.save()
    return redirect('UserProfile-detail', UserProfile_id=UserProfile_id)

class UserProfileCreate(LoginRequiredMixin, CreateView):
    model = UserProfile
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UserProfileUpdate(LoginRequiredMixin, UpdateView):
    model = UserProfile
    fields = ['FieldOfWork', 'DOB', 'home_city', 'home-state', 'e-mail', 'linked-in_profile', 'phone_number']

class UserProfileDelete(LoginRequiredMixin, DeleteView):
    model = UserProfile
    success_url = '/UserProfiles/'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        
        
        form = UserCreationForm(request.POST)
        if form.is_valid():
            
            user = form.save()
            
            login(request, user)
            return redirect('UserProfile-index')
        else:
            error_message = 'Invalid sign up - try again'
   
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

    