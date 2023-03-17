from django.shortcuts import render, redirect  
from agent.forms import AgentForm  
from agent.models import Agent  
# Create your views here.  
def agent(request):  
    if request.method == "POST":  
        form = AgentForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = AgentForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    Agents = Agent.objects.all()  
    return render(request,"show.html",{'agents':agent})  
def edit(request, id):  
    agent = Agent.objects.get(id=id)  
    return render(request,'edit.html', {'agent':agent})  
def update(request, id):  
    agent = Agent.objects.get(id=id)  
    form = AgentForm(request.POST, instance = agent)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': agent})  
def destroy(request, id):  
    agent = Agent.objects.get(id=id)  
    agent.delete()  
    return redirect("/show")  