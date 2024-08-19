from django.shortcuts import render,HttpResponse,redirect
from .models import Msg
# Create your views here.
def home(request):
    return HttpResponse("Welcome...This is home page.")

def about(request):
    return render(request,'hello.html')

def create(request):
    #print("Request is:",request.method)
    if request.method=='POST':  #POST==POST
        #fetch values from the form
        n=request.POST['uname']
        mail=request.POST['uemail']
        mob=request.POST['mob']
        msg=request.POST['msg']
        #print("Name:",n)
        #print("Email:",mail)
        #print("Mobile:",mob)
        #print("Message:",msg)
        m=Msg.objects.create(name=n,email=mail,mobile=mob,msg=msg)
        m.save()
        return redirect("/")
        #return HttpResponse("Data fetched succesfully..")
    else:
        return render(request,'create.html')

def dashboard(request):
    m=Msg.objects.all()
    #print(m)
    context={}
    context['data']=m
    return render(request,'dashboard.html',context)
    #return HttpResponse("Data fetched from database!!")        

def delete(request,rid):
    #print("Id to be deleted:",rid)
    m=Msg.objects.filter(id=rid)
    print(m)
    m.delete()
    return redirect('/')
    #return HttpResponse("Id to be deleted: "+rid)

def edit(request,rid):
    #print("Id to be edited:",rid)
    if request.method=='POST':
        #update data
        un=request.POST['uname']
        umail=request.POST['uemail']
        umob=request.POST['mob']
        umsg=request.POST['msg']
        #print(un,"-",umail,"-",umob,"-",umsg)
        m=Msg.objects.filter(id=rid)
        m.update(name=un,email=umail,mobile=umob,msg=umsg)
        return redirect("/")
    else:
        #m=Msg.objects.filter(id=rid)
        m=Msg.objects.get(id=rid)
        print(m)
        context={}
        context['data']=m
        return render(request,'edit.html',context)
    #return HttpResponse('Id to be edited'+rid)