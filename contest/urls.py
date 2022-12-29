from django.urls import path , include
from contest import views as contest_views
app_name = "contest"
urlpatterns = [
    
    path('createcontest/',contest_views.create_contest , name='create_contest'),
    path('contestlist/',contest_views.contest_list , name='contest_list'),
    path('register/<int:id>',contest_views.register_contest , name='register_contest'),
    path('live/<int:id>',contest_views.enter_contest , name='enter_contest'),
    path('submission/<int:id>',contest_views.contest_submission , name='contest_submission'),
    path('standing/<int:id>',contest_views.contest_standing , name='contest_standing'),
    path('<int:id>',contest_views.enter_contest2 , name='enter_contest2'),
    

]
