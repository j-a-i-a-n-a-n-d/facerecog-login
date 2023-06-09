from django.shortcuts import render, redirect
from app.MLMODEL import FaceRecognition
from .models import Profile
from .forms import RegisterationForm
from django.contrib import messages

faceRecognition = FaceRecognition()


def addFace(face_id):
    face_id = face_id
    faceRecognition.faceDetect(face_id)
    faceRecognition.trainFace()
    return redirect("/")


def home(request):
    return render(request, 'facerecog/home.html')


def register(request):
    if request.method == "POST":
        form = RegisterationForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered Successfully")
            addFace(request.POST['face_id'])
            redirect('home')
        else:
            messages.error(request, "Failed Registeration")
    else:
        form = RegisterationForm()
    return render(request, "facerecog/register.html", {"form": form})


def login(request):
    face_id = faceRecognition.recognizeFace()
    return redirect("greeting", str(face_id))


def greeting(request, face_id):
    face_id = int(face_id)
    context = {
        'user': Profile.objects.get(face_id=face_id)
    }
    return render(request, 'facerecog/greeting.html', context=context)
