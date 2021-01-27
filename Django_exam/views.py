from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def exercise1(request):
    template = loader.get_template('exercise1.html')
    msg = '황영민'
    context = {'result': msg }
    return HttpResponse(template.render(context, request))

def exercise2(request):
    if request.method == 'POST':
        name = request.POST['name']
        opinion = request.POST['opinion']
        context = {'name': name,'opinion' : opinion}
    else:
        context = None
    return render(request, 'exercise2.html', context)