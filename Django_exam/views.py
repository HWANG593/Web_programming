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
        na = request.POST['name']
        op = request.POST['opinion']
        context = {'nam': na,'opi' : op}
    else:
        context = None
    return render(request, 'exercise2.html', context)

def product1(request):
    context = None
    return render(request, 'product1.html', context)

def basket1(request):
    if request.method == 'GET':
        productid = request.GET['pid']
        context = {
            'pid':productid,
        }
    return render(request, 'basket1.html', context)
