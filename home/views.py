from django.shortcuts import render, HttpResponse, redirect
from home.models import Registerations, Team, Item, User_Emails, Scores
from datetime import date, datetime
from home.forms import EmailText
from .forms import EmailText
from random import randint


# Create your views here.

def index(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            get_user = Registerations.objects.get(email = email)
            pw = get_user.password

            if pw == password:
                request.session['uid'] = email
                return redirect('team')
            else:
                return render(request, 'index_issue.html')
        except:
            return render(request, 'index_issue.html')

    return render(request, 'index.html')

def logout(request):
    del request.session['uid']
    return redirect('/')

def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        first_pass = request.POST.get('first_password')
        second_pass = request.POST.get('second_password')

        if first_pass == second_pass:
            new_user = Registerations(name = name, email = email, password = first_pass)
            new_user.save()
            return render(request, 'register_success.html')
        else:
            context = {
                "name": name,
                "email": email
            }
            return render(request, 'register_issue.html', context)

    return render(request, 'base_register.html')

def team(request):
    if request.session.has_key('uid'):
        return render(request, 'team_page.html')
    else:
        return redirect('/')

def create_team(request):
    if request.session.has_key('uid'):
        if request.method == "POST":
            name = request.POST.get('team_name')
            try:
                get_name = Team.objects.get(name = name)
                # If exists, name already exists. Send error screen
                return render(request, 'create_team_issue.html')

            except:
                code = ''.join(["{}".format(randint(0, 9)) for num in range(0, 10)])
                new_team = Team(name = name, code = code)
                new_team.save()
                context = {
                    "name": name,
                    "code": code
                }
                return render(request, 'create_team_success.html', context)

        return render(request, 'create_team_base.html')
    else:
        return redirect('/')   

def join_team(request):
    if request.session.has_key('uid'):
        # Check if team code exist. If exists, register email of person in team. Increment team count by 1.
        # If count == 4, give message that four people full.
        # If does not exist, give error message.
        if request.method == "POST":
            code = request.POST.get('team_code')
            
            try:
                get_team = Team.objects.get(code = code)
                player_list = [get_team.P1, get_team.P1, get_team.P1, get_team.P1]
                get_player = Registerations.objects.get(email = request.session['uid']).name
                
                if request.session['uid'] in player_list:
                    request.session['code'] = code
                    return redirect('/team/info')

                # Team already full
                if get_team.total_members == 4:
                    context = {
                    "issue": "Team is already full"
                    }
                    return render(request, 'join_team_issue.html', context)

                elif get_team.total_members == 0:
                    get_team.P1 = request.session['uid']
                    get_team.total_members = 1
                    get_team.save()
                    
                
                elif get_team.total_members == 1:
                    get_team.P2 = request.session['uid']
                    get_team.total_members = 2
                    get_team.save()
                
                elif get_team.total_members == 2:
                    get_team.P3 = request.session['uid']
                    get_team.total_members = 3
                    get_team.save()
                
                elif get_team.total_members == 3:
                    get_team.P4 = request.session['uid']
                    get_team.total_members = 4
                    get_team.save()

                request.session['code'] = code
                
                return redirect('/team/info')
                
            except:
                context = {
                    "issue": "Invalid team code"
                }
                return render(request, 'join_team_issue.html', context)

        return render(request, 'join_team.html')
    else:
        return redirect('/')      

def team_info(request):
    if request.session.has_key('uid'):
        team_obj = Team.objects.get(code = request.session['code'])
        context = {
            "team_name": team_obj.name,
            "P1": team_obj.P1,
            "P2": team_obj.P2,
            "P3": team_obj.P3,
            "P4": team_obj.P4,
        }
        return render(request, 'team_info.html', context)
    else:
        return redirect('/')

def game(request):
    if request.session.has_key('uid'):
        obj = Item.objects.all()
        context = {
            "obj": obj
        }
        return render(request, 'training_session.html', context )
    else:
        return redirect('/')

def scenario(request):
    if request.session.has_key('uid'):
        return render(request, 'scenario.html')
    else:
        return redirect('/')

def task_one(request):
    if request.session.has_key('uid'):
        return render(request, 'first_task.html')
    else:
        return redirect('/')

def task_two(request):
    if request.session.has_key('uid'):
        return render(request, 'second_task.html')
    else:
        return redirect('/')

def email(request):
    if request.session.has_key('uid'):
        if request.method == "POST":
            code = request.session['code']
            form = EmailText(request.POST)
            if form.is_valid():
                email_body = form.cleaned_data['Body']
            # form.save()
            From = request.POST.get('FromField')
            To = request.POST.get('ToField')
            Subject = request.POST.get('Subject')
            email = User_Emails(Team_Code=code, To=To, From=From, Subject=Subject, Body = email_body, Date=datetime.today())
            email.save()
            return redirect('/game/first_task/second_email')

        form = EmailText
        context = {
            "form": form
        }
        return render(request, 'write_email.html', context)
    else:
        return redirect('/')

def second_email(request):
    if request.session.has_key('uid'):
        if request.method == "POST":
            code = request.session['code']
            form = EmailText(request.POST)
            if form.is_valid():
                email_body = form.cleaned_data['Body']
            # form.save()
            From = request.POST.get('FromField')
            To = request.POST.get('ToField')
            Subject = request.POST.get('Subject')
            email = User_Emails(Team_Code = code, To=To, From=From, Subject=Subject, Body = email_body, Date=datetime.today())
            email.save()
            return redirect('/game/second_task')

        form = EmailText
        context = {
            "form": form
        }
        return render(request, 'write_email2.html', context)
    else:
        return redirect('/')

def leaderboard(request):
    if request.session.has_key('uid'):
        leaderboard = Scores.objects.order_by('-points')
        team_names = []
        team_codes = []
        team_points = []
        entries = len(leaderboard)
        for x in leaderboard:
            team_names.append(x.name)
            team_codes.append(x.code)
            team_points.append(x.points)
        for x in range(0, 10-entries):
            team_names.append("-")
            team_codes.append("-")
            team_points.append("-")

        context = {
            "name": team_names,
            "code": team_codes,
            "points": team_points
        }
        return render(request, 'leaderboard.html', context)
    else:
        return redirect('/')

def email_1(request):
    if request.session.has_key('uid'):
        try:
            get_team = Scores.objects.get(code = request.session['code'])
            get_team.points = 0
            get_team.q1 = ""
            get_team.q2 = ""
            get_team.q3 = ""
            get_team.q4 = ""
            get_team.q5 = ""
            get_team.q6 = ""
            get_team.q7 = ""
            get_team.q8 = ""
            get_team.q9 = ""
            get_team.q10 = ""
            get_team.save()
            return render(request, 'email_one.html')
        except:
            get_name = Team.objects.get(code = request.session['code']).name
            get_code = request.session['code']
            points = 0
            new_team = Scores(code = get_code, name = get_name, points = points)
            new_team.save()
            return render(request, 'email_one.html')
    else:
        return redirect('/')

def email_2c(request):
    if request.session.has_key('uid'):
        get_team = Scores.objects.get(code = request.session['code'])
        get_team.q1 = "Correct"
        get_team.save()
        return render(request, 'email_two.html')
    else:
        return redirect('/')

def email_2w(request):
    if request.session.has_key('uid'):
        get_team = Scores.objects.get(code = request.session['code'])
        get_team.q1 = "Incorrect"
        get_team.save()
        return render(request, 'email_two.html')
    else:
        return redirect('/')

def email_3c(request):
    if request.session.has_key('uid'):
        get_team = Scores.objects.get(code = request.session['code'])
        get_team.q2 = "Correct"
        get_team.save()
        return render(request, 'email_three.html')
    else:
        return redirect('/')

def email_3w(request):
    if request.session.has_key('uid'):
        get_team = Scores.objects.get(code = request.session['code'])
        get_team.q2 = "Incorrect"
        get_team.save()
        return render(request, 'email_three.html')
    else:
        return redirect('/')

def email_4c(request):
    if request.session.has_key('uid'):
        get_team = Scores.objects.get(code = request.session['code'])
        get_team.q3 = "Correct"
        get_team.save()
        return render(request, 'email_four.html')
    else:
        return redirect('/')

def email_4w(request):
    if request.session.has_key('uid'):
        get_team = Scores.objects.get(code = request.session['code'])
        get_team.q3 = "Incorrect"
        get_team.save()
        return render(request, 'email_four.html')
    else:
        return redirect('/')

def email_5c(request):
    if request.session.has_key('uid'):
        get_team = Scores.objects.get(code = request.session['code'])
        get_team.q4 = "Correct"
        get_team.save()
        return render(request, 'email_five.html')
    else:
        return redirect('/')

def email_5w(request):
    if request.session.has_key('uid'):
        get_team = Scores.objects.get(code = request.session['code'])
        get_team.q4 = "Incorrect"
        get_team.save()
        return render(request, 'email_five.html')
    else:
        return redirect('/')

def email_6c(request):
    if request.session.has_key('uid'):
        get_team = Scores.objects.get(code = request.session['code'])
        get_team.q5 = "Correct"
        get_team.save()
        return render(request, 'email_six.html')
    else:
        return redirect('/')

def email_6w(request):
    if request.session.has_key('uid'):
        get_team = Scores.objects.get(code = request.session['code'])
        get_team.q5 = "Incorrect"
        get_team.save()
        return render(request, 'email_six.html')
    else:
        return redirect('/')

def email_7c(request):
    if request.session.has_key('uid'):
        get_team = Scores.objects.get(code = request.session['code'])
        get_team.q6 = "Correct"
        get_team.save()
        return render(request, 'email_seven.html')
    else:
        return redirect('/')

def email_7w(request):
    if request.session.has_key('uid'):
        get_team = Scores.objects.get(code = request.session['code'])
        get_team.q6 = "Incorrect"
        get_team.save()
        return render(request, 'email_seven.html')
    else:
        return redirect('/')

def email_8c(request):
    if request.session.has_key('uid'):
        get_team = Scores.objects.get(code = request.session['code'])
        get_team.q7 = "Correct"
        get_team.save()
        return render(request, 'email_eight.html')
    else:
        return redirect('/')

def email_8w(request):
    if request.session.has_key('uid'):
        get_team = Scores.objects.get(code = request.session['code'])
        get_team.q7 = "Incorrect"
        get_team.save()
        return render(request, 'email_eight.html')
    else:
        return redirect('/')

def email_9c(request):
    if request.session.has_key('uid'):
        get_team = Scores.objects.get(code = request.session['code'])
        get_team.q8 = "Correct"
        get_team.save()
        return render(request, 'email_nine.html')
    else:
        return redirect('/')

def email_9w(request):
    if request.session.has_key('uid'):
        get_team = Scores.objects.get(code = request.session['code'])
        get_team.q8 = "Incorrect"
        get_team.save()
        return render(request, 'email_nine.html')
    else:
        return redirect('/')

def email_10c(request):
    if request.session.has_key('uid'):
        get_team = Scores.objects.get(code = request.session['code'])
        get_team.q9 = "Correct"
        get_team.save()
        return render(request, 'email_ten.html')
    else:
        return redirect('/')

def email_10w(request):
    if request.session.has_key('uid'):
        get_team = Scores.objects.get(code = request.session['code'])
        get_team.q9 = "Incorrect"
        get_team.save()
        return render(request, 'email_ten.html')
    else:
        return redirect('/')

def email_11c(request):
    if request.session.has_key('uid'):
        get_team = Scores.objects.get(code = request.session['code'])
        get_team.q10 = "Correct"
        get_team.save()

        compile = [get_team.q1, get_team.q2, get_team.q3, get_team.q4, get_team.q5, get_team.q6, 
        get_team.q7, get_team.q8, get_team.q9, get_team.q10]
        correct = compile.count('Correct')
        points = correct * 10
        get_team.points = points
        name = get_team.name
        get_team.save()

        context = {
            "name": name,
            "points": points
        }
        return render(request, 'finish.html', context)
    else:
        return redirect('/')

def email_11w(request):
    if request.session.has_key('uid'):
        get_team = Scores.objects.get(code = request.session['code'])
        get_team.q10 = "Incorrect"
        get_team.save()
        
        compile = [get_team.q1, get_team.q2, get_team.q3, get_team.q4, get_team.q5, get_team.q6, 
        get_team.q7, get_team.q8, get_team.q9, get_team.q10]
        correct = compile.count('Correct')
        points = correct * 10
        get_team.points = points
        name = get_team.name
        get_team.save()

        context = {
            "name": name,
            "points": points
        }
        return render(request, 'finish.html', context)
    else:
        return redirect('/')
