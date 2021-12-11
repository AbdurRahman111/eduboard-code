from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import FormData

from django import forms
from .models import FormData
from .forms import EduboardForm
# Create your views here.
from pylatexenc.latex2text import LatexNodes2Text


def convert_latex(latex):
    data = LatexNodes2Text().latex_to_text(latex)
    return data


def create_question(request):
    if request.method == 'POST':
        Question = request.POST['Question']
        Clue = request.POST['Clue']
        Solution = request.POST['Solution']
        Answer = request.POST['Answer']
        CorrectAnswer = request.POST['CorrectAnswer']
        ImageData = request.FILES['imagedata']
        form1 = FormData(Question=convert_latex(Question),
                            Clue=convert_latex(Clue),
                            Solution=convert_latex(Solution),
                            Answer=convert_latex(Answer),
                            CorrectAnswer=convert_latex(CorrectAnswer),
                            ImageData=ImageData)
        form1.save()
        print('form created')

        data = FormData.objects.get(pk=17)
        print(data)
        dis = {
        "question_number": data
        }
        # return render_to_response("displayquestions.html", dis)
        return render(request, 'displayquestion.html', dis)
        # return redirect('/displayquestions/')

    else:
        return render(request, 'createquestions.html')
    

# def create_question(request):
#     if request.method == 'POST':
#         form = EduboardForm(request.POST, request.FILES)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.Question = convert_latex(instance.Question)
#             instance.Clue = convert_latex(instance.Clue)
#             instance.Solution = convert_latex(instance.Solution)
#             instance.Answer = convert_latex(instance.Answer)
#             instance.CorrectAnswer = convert_latex(instance.CorrectAnswer)
#             instance.save()
#             # form.save()
#         # Question = convert_latex(request.POST.get('question'))
#         # Clue = convert_latex(request.POST.get('clue'))
#         # Solution = convert_latex(request.POST.get('solution'))
#         # Answer = convert_latex(request.POST.get('answer'))
#         # CorrectAnswer = convert_latex(
#         #     request.POST.get('correctanswer'))
#         # ImageData = request.POST.get('imagedata')

#         # formdata = FormData(Question=Question,
#         #                     Clue=Clue,
#         #                     Solution=Solution,
#         #                     Answer=Answer,
#         #                     CorrectAnswer=CorrectAnswer,
#         #                     ImageData=ImageData,)

#         # formdata.save()
#         form = EduboardForm()
#         data = FormData.objects.all()
#         context = {
#             'title': 'Soarlogic',
#             'form': form,
#             'data': data,
#         }

#         print(context)
#     else:
#         form = EduboardForm()
#         context = {
#             'title': 'Soarlogic',
#             'form': form,

#         }

        
#     return render(request, 'api/new.html', context)


def show_question(request):
    data = FormData.objects.get(pk=6)
    print(data)
    return render(request, 'api/data.html', {'title': 'Soarlogic', 'data': data})

def form(request):
    # return HttpResponse('<h1>Hello</h1>')
    return render(request, 'landingpage.html')
    

def registration(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        isteacher = request.POST['isteacher']

        print(isteacher)

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('/registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('/registration')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('user created')
                if isteacher == "true":
                    return redirect('/login')
                else:
                    return redirect('/studentlogin')
        else:
             messages.info(request,'Password Taken')
        return redirect('/registration')

    else:
        return render(request, 'registration.html')

def submitanswer(request):
    if request.method == 'POST':
        answer = request.POST['answer']
        id =  request.POST['id']
        result = FormData.objects.get(pk=id)
        if(result.Answer == answer):
            # data = FormData.objects.get(pk=id)
            dis = {
            "question_number": result,
            "result": "true"
            }
            # return render_to_response("displayquestions.html", dis)
            return render(request, 'view_question.html', dis)
        else:
            # data = FormData.objects.get(pk=id)
            dis = {
            "question_number": result,
            "result": "false"
            }
            # return render_to_response("displayquestions.html", dis)
            return render(request, 'view_question.html', dis)



    else:
        return render(request, 'registration.html')
  
def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/index')
        else:
            messages.info(request,'invalid credentials')
            return redirect('/login')
    else:
        return render(request, 'hello.html')

def logout(request):
    auth.logout(request)
    return redirect('/login')

def index(request):
    return render(request, 'index.html')

def studentlogin(request):
    # return render(request, 'Studentlogin.html')
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/dashboard')
        else:
            messages.info(request,'invalid credentials')
            return redirect('/studentlogin')
    else:
        return render(request, 'Studentlogin.html')

def courses(request):
    return render(request, 'courses.html')

def about(request):
    return render(request, 'about.html')

def trainers(request):
    return render(request, 'trainers.html')

def events(request):
    return render(request, 'events.html')

def pricing(request):
    return render(request, 'pricing.html')

def contact(request):
    return render(request, 'contact.html')

def courseDetails(request):
    return render(request, 'course-details.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def user(request):
    return render(request, 'user.html')

def admindashboard(request):
    return render(request, 'admindashboard.html')

def viewquestions(request):
    # return render(request, 'view_question.html')
    if request.method== 'POST':
        id1 = request.POST['id']
        data = FormData.objects.get(pk=id1)
        dis = {
        "question_number": data
        }
        # return render_to_response("displayquestions.html", dis)
        return render(request, 'view_question.html', dis)
        # return redirect('/displayquestion/', dis)
    else: 
        data = FormData.objects.get(pk=1)
        dis = {
        "question_number": data
        }
        # return render_to_response("displayquestions.html", dis)
        return render(request, 'view_question.html', dis)
    


def questionsetupload(request):
    return render(request, 'questionsetupload.html')

def questionpanel(request):
    return render(request, 'questionpanel.html')

def createquestions(request):
    return render(request, 'createquestions.html')

def landing(request):
    return render(request, 'landingpage.html')

def displayquestions(request, id):
    if request.method== 'POST':
        id1 = request.POST['id']
        data = FormData.objects.get(pk=id1)
        dis = {
        "question_number": data
        }
        # return render_to_response("displayquestions.html", dis)
        return render(request, 'displayquestions.html', dis)
    else: 
        data = FormData.objects.get(pk=id)
        dis = {
        "question_number": data
        }
        # return render_to_response("displayquestions.html", dis)
        return render(request, 'displayquestions.html', dis)

def displayquestionnn(request):
    if request.method== 'POST':
        id = request.POST['id']
        data = FormData.objects.get(pk=id)
        dis = {
        "question_number": data
        }
        # return render_to_response("displayquestions.html", dis)
        return render(request, 'displayquestions.html', dis)
    else:
        return render(request, 'createquestions.html')


def displayquestion(request):
    if request.method== 'POST':
        id1 = request.POST['id']
        data = FormData.objects.get(pk=id1)
        dis = {
        "question_number": data
        }
        # return render_to_response("displayquestions.html", dis)
        return render(request, 'displayquestion.html', dis)
        # return redirect('/displayquestion/', dis)
    else: 
        data = FormData.objects.get(pk=1)
        dis = {
        "question_number": data
        }
        # return render_to_response("displayquestions.html", dis)
        return render(request, 'displayquestion.html', dis)
    

    
