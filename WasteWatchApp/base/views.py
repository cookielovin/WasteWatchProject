from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import SignUpForm
from .models import CustomUser
from .models import WasteReport
from .forms import WasteReportForm
from .models import WasteReportImage

def signin_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("base:home")  # ✅ This matches LOGIN_REDIRECT_URL
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "login.html")  # Show the error on the same page

    return render(request, "login.html")  # GET request

def home(request):
    latest_reports = WasteReport.objects.order_by('submitted_at')[:20]
    return render(request, 'home.html', {'reports': latest_reports})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Get role and other custom fields from the POST request
            is_individual = True if form.cleaned_data.get("is_individual") == "yes" else False
            role = form.cleaned_data.get("role") if not is_individual else None
            individual = request.POST.get("individual")
            id_number = form.cleaned_data.get("identification_Number")

            # Create profile with extra data
            CustomUser.objects.create(
                user=user,
                role=role,
                is_individual=is_individual,
                identification_Number=id_number
            )

            login(request, user)
            return redirect('base:home')
        else:
            print(form.errors)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def createreport_view(request):
    if request.method == 'POST':
        form = WasteReportForm(request.POST)
        images = request.FILES.getlist('images')

        if form.is_valid():
            report = form.save()

            for img in images:
                WasteReportImage.objects.create(report=report, image=img)

            #return redirect('report_success') This part later must do . Make it redirect to user_reports
        
    else:
        form = WasteReportForm()

    return render(request, 'createreport.html', {'form': form})
    