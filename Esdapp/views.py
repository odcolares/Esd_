from django.shortcuts import render, redirect
from Esdapp.forms import esdForm
from Esdapp.models import esd

# Create your views here.
def home(request):
    data = {}
    data['db'] = esd.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = esdForm()
    return render(request, 'form.html', data)

def create(request):
    form = esdForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def edit(request, pk):
    data = {}
    data['db'] = esd.objetcs.get(pk=pk)
    data['form'] = esdForm(instance=data['db'])
    return render(request, 'form.html', data)

#def delete(request, pk):
#    db = esd.objects.get(pk=pk)
#    db.delete()
#    return redirect('home')

def update(request, pk):
    data = {}
    data['db'] = esd.objetcs.get(pk=pk)
    form = esdForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save() 
        return redirect ('home')

def view(request, id):
    data = {}
    data['db'] = esd.objetcs.get(id=id)
    return render(request, 'view.html', data)
