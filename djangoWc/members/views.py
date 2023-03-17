from django.shortcuts import render
from django.http import HttpResponse
from .models import Member
from django.contrib import messages


def home(request):
    context = {
        "mymembers": Member.objects.all().values(),
    }

    return render(request, "members/home.html", context)


def details_page(request, id):
    print(id)

    context = {"member": Member.objects.filter(id=id).values()[0]}

    return render(request, "members/display.html", context=context)


def add_page(request):
    if request.method == "GET":
        return render(request, "members/add.html")

    elif request.method == "POST":
        # fname, lname, phone, joined_date = request.POST
        fname, lname, phone, joined_date = list(request.POST.values())[1:]

        print(fname, lname, phone, joined_date)

        Member(firstname=fname, lastname=lname, phone=phone, joined_date=joined_date).save()

        return render(request, "members/add.html")

def delete_page(request):

    if request.method == "POST":
        print(request.POST)
        ids = list(request.POST.values())[1:]

        members = list(Member.objects.all().values())
        for member in members:
            for id in ids:
                if member['id'] == int(id):
                    print(id)
                    Member.objects.all().filter(id=id).delete() # delete members[index of member]
                    pass


    context = {
        "members" : Member.objects.all().values()
    }

    return render(request, "members/delete.html", context)