from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration, UserRegistration
from .models import student, User
import pyautogui


# Create your views here.
def login(request):
    form = UserRegistration()
    return render(request, 'login.html', {'forms': form})



# This Function Will Add New Student And Show All Items.
def create_read(request):
    if request.method == 'POST':
        st1 = StudentRegistration(request.POST)

        if st1.is_valid():
            nm = st1.cleaned_data['name']
            em = st1.cleaned_data['email']
            mb = st1.cleaned_data['mobile']
            pw = st1.cleaned_data['password']
            reg = student(name=nm, email=em, mobile=mb, password=pw)
            reg.save()
            pyautogui.alert("Student added successfully...!")
            st1 = StudentRegistration() # to clean data on load add student data

    else:
        st1 = StudentRegistration()

    stud = student.objects.all()
    return render(request, 'crud.html', {'form':st1, 'showalldata':stud})



# This Function Will Update/Edit 1 Student Data.
def update_data(request, id):
    if request.method == "POST":
        pi = student.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)

        if fm.is_valid():
            fm.save()
            pyautogui.alert("Student Data Updating Successfully...!")

    else:
        pi = student.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)

    return render(request, 'update.html', {'form':fm})



# This Function Delete 1 Student Data.
def delete_data(request, id):
    if request.method == "POST":
        delete_row_data = student.objects.get(pk=id)
        delete_row_data.delete()
        pyautogui.alert("Student Data Deleting Successful...!")
        return HttpResponseRedirect('/crud/')
        # return HttpResponseRedirect('/crud/crud')












# from .forms import StudentRegistration, UserRegistration
# from .models import student, User
# from django.contrib import auth

# def login(request, uploads=None):
#     if request.method == "POST":
#         st1 = UserRegistration(request.POST)
#
#         if st1.is_valid():
#             user1 = request.POST["username123"]
#             pass1 = request.POST["password123"]
#             user = User(username123=user1, password123=pass1)
#             user.save()
#             pyautogui.alert("login successfully...!")
#             st1 = UserRegistration()
#
#         else:
#             pyautogui.alert("Wrong username & password!")
#             return render(request, "login.html")
#
#     else:
#         st1 = UserRegistration()
#
#     stud = User.objects.all()
#     return render(request, 'crud.html', {'form': st1, 'showalldata': stud})