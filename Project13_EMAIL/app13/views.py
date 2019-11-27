from django.shortcuts import render
from django.core.mail import send_mail
from Project13 import settings as se

def showIndex(request):
    return render(request,"index.html")


def validateUser(req):
    uname = req.POST.get("username")
    upass = req.POST.get("password")

    if uname == "sathya" and upass == "tech":
        subject = "A Test Mail"
        message = "MANY MANY HAPPY RETURNS OF THE DAY"

        send_mail(subject,message,se.EMAIL_HOST_USER,['diptiranjanjena234@gmail.com','rounakm69@gmail.com'])

        return render(req,"welcome.html")
    else:
        return render(req,"index.html",{"message":"Invalid User"})


def logoutUser(request):
    return render(request,"index.html")