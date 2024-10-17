from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View

from .forms import CustomUserCreationForm, AvailabilityForm
from .models import Tutor

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")  
    template_name = "registration/signup.html"  

# View for the tutors list page
class TutorsListView(ListView):
    model = Tutor
    template_name = 'tutors.html'
    context_object_name = 'tutors'

    def get(self, request, *args, **kwargs):
        tutors = Tutor.objects.all()
        return render(request, self.template_name, {'tutors': tutors})

# View for the tutor detail page
class TutorDetailView(DetailView):
    model = Tutor
    template_name = 'tutor_detail.html'

def home(request):
    tutors = Tutor.objects.all()  # Fetch all tutors from the database
    user_classes = request.user.classes.all() if request.user.is_authenticated else None
    return render(request, 'home.html', {'tutors': tutors, 'user_classes': user_classes})

@login_required
def add_availability(request):
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            availability = form.save(commit=False)
            availability.user = request.user  # Set the TA to the logged-in user
            availability.save()
            return redirect('home')
    else:
        form = AvailabilityForm()
    return render(request, 'add_availability.html', {'form': form})

class ScheduleView(View):
    def get(self, request):
        return render(request, 'schedule.html')

class TutorProfileView(DetailView):
    model = Tutor
    template_name = 'tutor_profile.html'
    context_object_name = 'tutor'

def edit_hours(request, tutor_id):
    #tutor = get_object_or_404(Tutor, id=tutor_id)
    tutor = Tutor.objects.get(id=tutor_id)  # Fetch the tutor by ID
    if request.method == 'POST':
        # Process form data here
        # tutor.available_hours = request.POST['available_hours']
        tutor.save()
        return redirect('tutors_list')  # Redirect to the tutor list after saving
    return render(request, 'edit_hours.html', {'tutor': tutor})


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user
            return redirect('home')  # Redirect to the home page or wherever
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})