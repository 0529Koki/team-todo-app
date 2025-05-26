from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'todo/index.html')
def create_task(request):
    # POSTで来たタスクの処理を書くところ
    pass