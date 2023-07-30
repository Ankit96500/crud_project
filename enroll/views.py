from django.shortcuts import render,HttpResponseRedirect
from enroll.forms import studentform     # <------ make sure import file correctly   
from enroll.models import studentdb     # <------ make sure import file correctly

# Create your views here.

#this function add data in the database..
def add_show(request):
    if request.method == 'POST':
        fm=studentform(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=studentdb(name=nm,email=em,password=pw)
            reg.save()
    fm=studentform()
    sh=studentdb.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm,'show':sh})

# this function delete data in the database
def delete(request,id):
    if request.method == 'POST':
        pi=studentdb.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

# this function update data in the database
def update(request,upid):
    if request.method == 'POST':
        pi=studentdb.objects.get(pk=upid)
        fm=studentform(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=studentdb.objects.get(pk=upid)
        fm=studentform(instance=pi)        
    return render(request,'enroll/update.html',{'form':fm})



    


