from django.shortcuts import render
from Reviews.forms import *
from django.core.mail import send_mail
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        Dic={'username':username}
        return render(request,'home.html',Dic)
    return render(request,'home.html')




def registration(request):
    UFO=UserForm()
    N={'UFA':UFO}

    if request.method=='POST':
        User_Data=UserForm(request.POST)
        if User_Data.is_valid():
            Unsaved=User_Data.save(commit=False)


            Unsaved.set_password(User_Data.cleaned_data['password'])
            Unsaved.save()


            send_mail('Enter Your Acount Details',
                      'your acount is successfully created....thank you for register your details',
                      'naveenavula130@gmail.com',
                      [Unsaved.email],
                      fail_silently=True)
            
            return HttpResponse('Data Inserted Successfully....!!!')
        return HttpResponse('Your Data Is Invalid Data')
    return render(request,'registration.html',N)






def user_login(request):
    if request.method=='POST':
        username=request.POST['UN']
        password=request.POST['PW']

        Auth_Usr_Obj=authenticate(username=username,password=password)

        if Auth_Usr_Obj and Auth_Usr_Obj.is_active:
            login(request,Auth_Usr_Obj)
            request.session['username']=username

            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('Invalid Username or Password')
    return render(request,'user_login.html')






@login_required
def user_Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))




@login_required
def ask_a_questions(request):
    QFO=QuestionForm()
    Dic={'QFO':QFO}
    if request.method=='POST':
        QFD=QuestionForm(request.POST)
        if QFD.is_valid():
            Unsaved=QFD.save(commit=False)

            Unsaved.username=request.user
            Unsaved.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse("not")
    return render(request,'ask_a_questions.html',Dic)





@login_required
def write_answer(request):
    AnsFO = AnswerForm()
    Dic = {'AFO': AnsFO}
    ques = Question.objects.all()

    if request.method == 'POST':
        AFOD = AnswerForm(request.POST)
        if AFOD.is_valid():
            username = request.session['username']
            user_obj = User.objects.get(username=username)

            unsaved = AFOD.save(commit=False)
            unsaved.username = user_obj  
            unsaved.save()

            Q = unsaved.question
            ans_obj = Answer.objects.filter(question=Q, username=user_obj)
            Dic1 = {'ANSO': ans_obj}
            return HttpResponseRedirect(reverse('display_output'))
        else:
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'write_answer.html', Dic)




@login_required
def question_list(request):
    if request.session.get('username'):
        username=request.session.get('username')
        Questions=Question.objects.all()
        Dic={'QUES':Questions, 'USER':username}
        return render(request,'question_list.html',Dic)
    
def display_output(request):
    ao=Answer.objects.all()
    d={'ao':ao}

    return render(request,'display_output.html',d)


def forget_password(request):
    if request.method=='POST':
        username=request.POST['UN']
        password=request.POST['PW']


        UO=User.objects.filter(username=username)

        if UO:
            UO[0].set_password(password)
            UO[0].save()

        else:
            return HttpResponse('Your Enter The User Name Is Invalid')
        return HttpResponseRedirect(reverse('user_login'))
    return render(request,'forget_password.html')





@login_required
def change_password(request):
    username=request.session.get('username')
    Dic={'username':username}

    if request.method=='POST':
        password=request.POST['PW']
        UO=User.objects.get(username=username)
        UO.set_password(password)
        UO.save()

        return HttpResponseRedirect(reverse('user_login'))
    return render(request,'change_password.html',Dic)


            


