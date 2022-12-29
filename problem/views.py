from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Problem , Submission , TestCase
from codecheck import CodeCheck
from user.models import UserDetail 
from django.contrib.auth.models import User
from contest.models import RegisteredContestant
from django.contrib import messages
import time
import math
import datetime
import asyncio
# Create your views here.

def problem_page(request,id):
    
    problem=Problem.objects.get(pk=id)
    return render(request,"problem/problem_page.html",{"problem":problem})

def submitted_code(request,id):
    
    submitted=Submission.objects.get(pk=id)
    return render(request,"problem/submitted_code.html",{"submitted":submitted})

def submit_code(request,id):
    
    if request.user.is_authenticated:
        problem=Problem.objects.get(pk=id)
        contest=problem.contest
        today=datetime.datetime.now()
        user_obj=UserDetail.objects.get(user=User.objects.get(username=request.user.username))
        obj=UserDetail.objects.get(user=User.objects.get(username=request.user.username))
        
        if contest.start_time < today and contest.end_time > today:
            if RegisteredContestant.objects.filter(user=request.user.id,contest=contest).count()==1:  
            
                submission_time=datetime.datetime.now()
                code = request.POST['textarea']
                lang_code = request.POST['language']
                today=datetime.datetime.now()
                
                
                testcase=TestCase.objects.get(problem=problem)
                codecheck=CodeCheck(lang_code,testcase,code)
                mssg=codecheck.run_code()                   #running code

                Submission(user=request.user,problem=problem,contest=contest,
                submitted_time=submission_time,lang=lang_code,code=code,verdict=mssg).save() #submission
                
                if mssg=="Accepted" and Submission.objects.filter(user=request.user,problem=problem,verdict=mssg).count()==0:
                    user_obj.update(problems_solved=1+obj.problems_solved)


                value={"A":10,"B":20,"C":30,"D":50}
                ques_tag={"A":"a_score","B":"b_score","C":"c_score","D":"d_score"}
                if mssg=="Accepted":
                    score=value[problem.tag]*(1-problem.total_submission/2*contest.registered_user)
                    score=math.ceil(score)
                    problem.total_submission+=1
                    problem.save()
                    participant=RegisteredContestant.objects.get(user=request.user,contest=contest)
                    print("score updating",problem.tag,participant.a_score)
                    if problem.tag=="A" and participant.a_score==0:
                        participant.a_score=score
                        participant.total_score+=score
                        user_obj.update(score=score+obj.score)
                        print("score updated")
                    if problem.tag=="B" and participant.b_score==0:
                        participant.b_score=score
                        participant.total_score+=score
                        user_obj.update(score=score+obj.score)
                    if problem.tag=="C" and participant.c_score==0:
                        participant.c_score=score
                        participant.total_score+=score
                        user_obj.update(score=score+obj.score)
                    if problem.tag=="D" and participant.d_score==0:
                        participant.d_score=score
                        participant.total_score+=score
                        user_obj.update(score=score+obj.score)
                    participant.save()
                user_obj.save()
                messages.info(request, mssg) 
                return render(request,"problem/problem_page.html",{"problem":problem}) 
            messages.info(request, "You are not Registered for this contest.")
            return render(request,"problem/problem_page.html",{"problem":problem})
        submission_time=datetime.datetime.now()
        code = request.POST['textarea']
        lang_code = request.POST['language']
        today=datetime.datetime.now()
        
        
        testcase=TestCase.objects.get(problem=problem)
        codecheck=CodeCheck(lang_code,testcase,code)
        mssg=codecheck.run_code()                   #running code

        Submission(user=request.user,problem=problem,contest=contest,
        submitted_time=submission_time,lang=lang_code,code=code,verdict=mssg).save() #submission
        
        if mssg=="Accepted" and Submission.objects.filter(user=request.user,problem=problem,verdict=mssg).count()==0:
            user_obj.problems_solved+=1
            user_obj.save()
        messages.info(request, mssg) 
        return   render(request,"problem/problem_page.html",{"problem":problem})
    return redirect('login')
    
