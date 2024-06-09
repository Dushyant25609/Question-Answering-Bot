from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .API import query,prompt
from .password import generate_password


def home(request):
    return render(request, 'Home.html')

def signin(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = generate_password(fname)
        user = User.objects.create_user(name,email,password)
        user.first_name = fname
        user.last_name = lname
        subject = "Successful Registration"
        message = f"""
        Congratulations {fname} 
        your credentials
        username: {name}
        password: {password}"""
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        user.save()
        return redirect('login')
    return render(request, 'Signin.html')

def login(request):
    if request.method == 'POST':
        name = request.POST["name"]
        password = request.POST["password"]
        user = authenticate(request, username=name, password=password)
        if user is not None:
            auth_login(request, user) 
            return redirect('buddy')
        else:
            messages.error(request, 'Incorrect username or password')
    return render(request, 'Login.html')


def main_page(request):
    Ques = request.POST.get('input')
    if Ques is not None:
        Question = Ques
        prompt_text = prompt(Question)
        payload = {"inputs": prompt_text}
        generated_text = query(payload)

        # Removing the question from the generated text
        question_index = generated_text.find(Question)
        if question_index != -1:
            answer = generated_text[question_index + len(Question):].strip()
        else:
            answer = generated_text
        context = {
        'message': f"{answer}",
        'question': Ques,
        }
    else:
        context = {
        }
    
    return render(request,'Main.html',context)