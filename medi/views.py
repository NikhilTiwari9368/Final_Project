from django.shortcuts import render , HttpResponse
from appointment.models import Appointment 
from DoctorFind.models import Doctor
from Contactus.models import Contact
from products.models import Product
from Blogs.models import BlogPost
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from Precaution.models import Disease 
from django.contrib import messages
from django.contrib.auth.models import User


def disease_info(request):
    # Initialize the disease variable
    disease = None
    
    if request.method == 'POST':
        # Get the search query from the POST data
        query = request.POST.get('q')
        
        if query:
            # Try to find a disease that matches the query
            disease = Disease.objects.filter(name__icontains=query).first()
    
    # Render the 'disease_info.html' template with the disease information
    return render(request, "information.html", {'disease': disease})


@login_required(login_url='LoginPage')
def information(requests):
    return render(requests, "information.html")

def healthcare_centre(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists. Please log in.")
            return render(request, 'signup.html')  # Replace with your signup template

        # Continue with your existing password checks here
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'signup.html')  # Replace with your signup template

        if len(password1) < 8:
            messages.error(request, "Password must contain at least 8 characters.")
            return render(request, 'signup.html')  # Replace with your signup template

        if password1.isnumeric():
            messages.error(request, "Password cannot be entirely numeric.")
            return render(request, 'signup.html')  # Replace with your signup template

        if name.lower() in password1.lower() or email.split('@')[0].lower() in password1.lower():
            messages.error(request, "Password is too similar to your personal information.")
            return render(request, 'signup.html')  # Replace with your signup template

        # If everything is valid, create the user
        user = User.objects.create_user(username=name, email=email, password=password1)
        user.save()
        messages.success(request, "Account created successfully. You can log in now.")
        return redirect('LoginPage')  # Redirect to login page or another page

    return render(request, 'signup.html')
        

def LoginPage(request):
    if request.method == "POST":
        name = request.POST.get('username').lower()  # Convert the username to lowercase
        password = request.POST.get('password')
        
        try:
            # Try to find the user with a case-insensitive search
            user_obj = User.objects.get(username__iexact=name)
            user = authenticate(username=user_obj.username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect("information")
            else:
                messages.error(request, 'Username or password is incorrect.')
                return redirect('LoginPage')
        
        except User.DoesNotExist:
            messages.error(request, 'Username or password is incorrect.')
            return redirect('LoginPage')
    
    return render(request, "login.html")

def LogoutPage(requests):
    logout(requests)
    return redirect('LoginPage')


def index(requests):
    return render(requests , "index.html" ) 

def about(requests):
    return render(requests , "about.html")


def saveform(requests):
    if requests.method == 'POST':
        department = requests.POST.get('department')
        doctor = requests.POST.get('doctor')
        name = requests.POST.get('name')
        email = requests.POST.get('email')
        appointment_date = requests.POST.get('appointment_date')
        appointment_time = requests.POST.get('appointment_time')
        
        ap = Appointment(department = department , doctor = doctor , name = name , email = email , appointment_date = appointment_date , appointment_time = appointment_time)
        ap.save()
        
    return render(requests , "information.html")


def blog(requests):
    blog_posts = BlogPost.objects.all()
    return render(requests, 'blog.html', {'blog_posts': blog_posts})

def contact(requests):
    return render(requests , "contact.html") 

def contact_view(requests):
    if requests.method == "POST":
        name = requests.POST.get('name')
        email = requests.POST.get('email')
        subject = requests.POST.get('subject')
        message = requests.POST.get('message')

        # Create a new Contact object and save it to the database
        ap = Contact(name=name, email=email, subject=subject, message=message)
        ap.save()
    
    return render(requests, "contact.html")

def price(requests):

    return render(requests , "price.html" ) 

def search(requests):
    return render(requests , "search.html") 


def doctorsearch(request):
    doctors = Doctor.objects.all()
    speciality = request.POST.get('speciality')
    city = request.POST.get('city')

    if speciality and speciality != "Select Specialty":
        doctors = doctors.filter(speciality=speciality)
    if city:
        doctors = doctors.filter(city__icontains=city)

    return render(request, "search.html", {'doctors': doctors})


def service(requests):
    return render(requests , "service.html") 

    
def team(requests):
    products = Product.objects.all()  # Fetch all products from the database
    return render(requests, "team.html", {'products': products})

def testimonial(requests):
    return render(requests , "testimonial.html") 