from django.urls import path
from problem import views as problem_views
app_name = "problem"
urlpatterns = [
    
    path('<int:id>/',problem_views.problem_page , name='problem'),
    path('submission/<int:id>/',problem_views.submitted_code , name='submitted_code'),
    path('submit/<int:id>/',problem_views.submit_code , name='submit_code'),

    
]