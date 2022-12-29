from django.shortcuts import render , redirect
from contest.models import Contest , RegisteredContestant
from problem.models import Problem , TestCase ,Submission
from django.utils.dateparse import parse_duration
import datetime


# Create your views here.,
def create_contest(request):
    if request.method == "POST":
        name=request.POST['contest_name']
        start_time=(request.POST['start_time'])
        start_time=datetime.datetime.strptime(start_time,"%Y-%m-%dT%H:%M")
        duration=parse_duration(request.POST['duration'])
        end_time=start_time+duration

        contest=Contest(name=name,start_time=start_time,end_time=end_time,duration=duration)
        contest.save()
        #problem1
        problem1_name=request.POST['problem1_name']
        problem1_tag=request.POST['problem1_tag']
        problem1_desc=request.POST['problem1_desc']
        problem1_tc=request.POST['problem1_tc']
        problem1_mc=request.POST['problem1_mc']
        problem1_ex=request.POST['problem1_ex']
        problem1_in=request.POST['problem1_in']
        problem1_out=request.POST['problem1_out']

        problem1=Problem(contest=contest, name=problem1_name,tag=problem1_tag,discription=problem1_desc,
        time_complexity=problem1_tc,space_complexity=problem1_mc,example=problem1_ex)
        problem1.save()
        
        testcase1=TestCase(problem=problem1 ,input=problem1_in,output=problem1_out).save()
        #problem2
        problem2_name=request.POST['problem2_name']
        problem2_tag=request.POST['problem2_tag']
        problem2_desc=request.POST['problem2_desc']
        problem2_tc=request.POST['problem2_tc']
        problem2_mc=request.POST['problem2_mc']
        problem2_ex=request.POST['problem2_ex']
        problem2_in=request.POST['problem2_in']
        problem2_out=request.POST['problem2_out']

        problem2=Problem(contest=contest, name=problem2_name,tag=problem2_tag,discription=problem2_desc,
        time_complexity=problem2_tc,space_complexity=problem2_mc,example=problem2_ex)
        problem2.save()
        
        testcase1=TestCase(problem=problem2 ,input=problem2_in,output=problem2_out).save()
        #problem3
        problem3_name=request.POST['problem3_name']
        problem3_tag=request.POST['problem3_tag']
        problem3_desc=request.POST['problem3_desc']
        problem3_tc=request.POST['problem3_tc']
        problem3_mc=request.POST['problem3_mc']
        problem3_ex=request.POST['problem3_ex']
        problem3_in=request.POST['problem3_in']
        problem3_out=request.POST['problem3_out']

        problem3=Problem(contest=contest, name=problem3_name,tag=problem3_tag,discription=problem3_desc,
        time_complexity=problem3_tc,space_complexity=problem3_mc,example=problem3_ex)
        problem3.save()
        
        testcase1=TestCase(problem=problem3 ,input=problem3_in,output=problem3_out).save()
        #problem4
        problem4_name=request.POST['problem4_name']
        problem4_tag=request.POST['problem4_tag']
        problem4_desc=request.POST['problem4_desc']
        problem4_tc=request.POST['problem4_tc']
        problem4_mc=request.POST['problem4_mc']
        problem4_ex=request.POST['problem4_ex']
        problem4_in=request.POST['problem4_in']
        problem4_out=request.POST['problem4_out']

        problem4=Problem(contest=contest, name=problem4_name,tag=problem4_tag,discription=problem4_desc,
        time_complexity=problem4_tc,space_complexity=problem4_mc,example=problem4_ex)
        problem4.save()
        
        testcase1=TestCase(problem=problem4 ,input=problem4_in,output=problem4_out).save()
        
    return render (request,"contest/create_contest.html", context={"form":7})

def contest_list(request):
    today=datetime.datetime.now()
    contests=Contest.objects.all().order_by('-end_time')
    lst=[]
    today=datetime.datetime.now()
    if request.user.is_authenticated:
        registerds=RegisteredContestant.objects.filter(user=request.user)
        for registerd in registerds:
            if registerd.contest.start_time>today:
                lst.append(registerd.contest.pk)
    return render(request,"contest/contest_list.html",{"contests":contests,"today":today,"registered_ids":lst})

def register_contest(request,id):
    print(request.user.username,request.user.pk)
    if request.user.is_authenticated:
        if request.method == "POST":
            contest=Contest.objects.get(id=id)
            if RegisteredContestant.objects.filter(user=request.user.id,contest=id).count()==0:
               RegisteredContestant(user=request.user,contest=contest).save()
               contest.registered_user+=1
            return redirect("contest:contest_list")
        return render(request,"contest/register.html",{"contest":Contest.objects.get(pk=id)})
    return render(request,"user/login.html")

def enter_contest(request,id):
    problems={}
    contest=Contest.objects.get(pk=id)
    today=datetime.datetime.now()
    if request.user.is_authenticated:
        problems=RegisteredContestant.objects.filter(contest=contest,user=request.user)
    return render(request,"contest/contest_page.html",{"contest":contest,"problems":problems})    
def enter_contest2(request,id):
    problems={}
    contest=Contest.objects.get(pk=id)
    today=datetime.datetime.now()
    if request.user.is_authenticated:
        problems=RegisteredContestant.objects.filter(contest=contest,user=request.user)
    return render(request,"contest/contest_page.html",{"contest":contest,"problems":problems})    
        

def contest_submission(request,id):
    if request.user.is_authenticated:
        contest=Contest.objects.get(pk=id)
        submissions=Submission.objects.filter(user=request.user,contest=contest).order_by('-submitted_time')
        return render(request,"contest/contest_submission.html",{"submissions":submissions,"contest":contest})
    return render(request,"user/login.html")

def contest_standing(request,id):
    contest=Contest.objects.get(pk=id)
    registers=contest.registeredcontestant_set.all().order_by('-total_score')#RegisteredContestant.objects.get(contest=contest)
    print(registers)
    return render(request,"contest/standing.html",{"registers":registers,"contest":contest})

