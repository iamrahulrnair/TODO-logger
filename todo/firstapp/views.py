from django.shortcuts import render,redirect
from django.urls import reverse_lazy,reverse
from django.views import generic
from . import models
from .import forms
from django.contrib.auth import get_user_model

from django.http import HttpResponseRedirect

# def mainpage(request):
#     model=models.data
#     if request.user.is_authenticated:
#         dataoftheuser=models.data.objects.all().filter(user=request.user)

#         return render(request,'index.html',{"dataoftheuser":dataoftheuser})
#     else:
#         return render(request,'index.html')





class mainpage(generic.ListView):
    template_name='index.html'
    model=models.data

    context_object_name="dataoftheuser"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return models.data.objects.all().filter(user=self.request.user)
        else:
            return None





def registration(request):
    form=forms.userregform()
    if request.method=='POST':
        form=forms.userregform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
            


    return render(request,'registration.html',{'form':form})




def todo(request):
    if request.method=="POST":
        data_model=models.data
        user=request.user
        obj=data_model(user=request.user,data=request.POST['encodeddata'],list_length=request.POST['listlength'])
        obj.save()
        return redirect('index')

    return render(request,'todo-page.html')

   
# class detail(generic.DetailView):
#     model=models.data
#     template_name='todo-page.html'
#     context_object_name='detailobject'
#     success_url=reverse_lazy('index.html')
   
def detail(request,pk):
    if request.method=="POST":
        date=request.POST.get('datefield')
        def monthToNum(shortMonth):
            return {
            'jan': 1,
            'feb': 2,
            'mar': 3,
            'apr': 4,
            'may': 5,
            'jun': 6,
            'jul': 7,
            'aug': 8,
            'sep': 9, 
            'oct': 10,
            'nov': 11,
            'dec': 12
            }[shortMonth]
        date=date.replace(',','').split()
        monthvalue=monthToNum(date[0].lower())

        for i in range(0,len(date)):
            if i==0:
                date[i]=str(monthvalue)

        date=f"{date[2]}-{date[0]}-{date[1]}"
        
        data_model=models.data
        user=request.user
        haha=int(request.POST['listlength'])
        
        obj=data_model(id=pk,user=user,data=request.POST['encodeddata'],date_created=date,list_length=haha)
        obj.save()
        return redirect('index')
    detailobject=models.data.objects.get(pk=pk)
    return render(request,'todo-page.html',{'detailobject':detailobject})
   

def deletedata(request,pk):
    obj=models.data.objects.get(id=pk)
    obj.delete()
    return HttpResponseRedirect(reverse('index'))

