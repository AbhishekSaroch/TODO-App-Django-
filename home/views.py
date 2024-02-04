from django.shortcuts import render,HttpResponse

def home(request):
    people=[{
        "name":"Abhijeet",
        "age":23
    },{
        "name":"Rohan",
        "age":24
    },{
        "name":"Deep",
        "age":25
    }]
    vegetables=['One','Two']
    return render(request,"home/index.html",context={'people':people,'text':vegetables})


def blog(request):
    return HttpResponse("<h1>This is Blogs Page!</h1>")

def success_page(request):
    return HttpResponse("<h1>Success Page</h1>")

def about(request):
    return render(request,"home/about.html")

def contact(request):
    return render(request,"home/contact.html")
