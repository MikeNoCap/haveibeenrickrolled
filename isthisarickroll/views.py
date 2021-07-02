from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
import requests as req
import pickle
import random
# Create your views here.
import os

print(os.path)



class EmptyInput(Exception):
    """Raised when a form is submitted without any content."""
    pass

with open('rick_db.pkl', 'rb') as fp:
    ricklinks = pickle.load(fp)
    


[ 
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "https://www. youtube.com/watch?v=iik25wqIuFo",
    "https://www.youtube.com/watch?v=O91DT1pR1ew",
    "https://www.youtube.com/watch?v=0lQqK-ofK3M",
    "https://www.youtube.com/watch?v=oHg5SJYRHA0",
    "https://www.youtube.com/watch?v=BjDebmqFRuc",
    "https://www.youtube.com/watch?v=xvFZjo5PgG0",
    "https://www.youtube.com/watch?v=QDia3e12czc",
    "https://www.youtube.com/watch?v=tmY-G6sngk8",
    "https://www.youtube.com/watch?v=7p78V3ohITc",
    "https://www.youtube.com/watch?v=QtBDL8EiNZo",
    "https://www.youtube.com/watch?v=FqdmWQ-ACv0",
    "https://www.youtube.com/watch?v=fOGEMwgqN20",
    "https://www.youtube.com/watch?v=8iN8T-1_hrI",
    "https://www.youtube.com/watch?v=m6OCJxOsiyw",
    "https://www.youtube.com/watch?v=z6wNtevjVOk",
    "https://www.youtube.com/watch?v=igaCvre6WmE",
    "https://www.youtube.com/watch?v=2EkXa0GMH1w",
    "https://www.youtube.com/watch?v=3-csLHSLS-k",
    "https://www.youtube.com/watch?v=6hlTj-cK7XU",
    "https://www.youtube.com/watch?v=JrdGAcZ8vhs",
    "https://www.youtube.com/watch?v=bIXm-Q-Xa4s",
    "https://www.youtube.com/watch?v=aqOoTQ-G-r4",
    "https://www.youtube.com/watch?v=4uoEEbLyBJA",
    "https://www.youtube.com/watch?v=C4rtrJjXkng",
    "https://www.youtube.com/watch?v=fOGEMwgqN20",
    "https://www.youtube.com/watch?v=SlwQ2JTfpHA",
    "https://www.youtube.com/watch?v=YZduI-_l6eQ",
    "https://www.youtube.com/watch?v=ydB5_UM6Abo",
    "https://www.youtube.com/watch?v=Nu9_fRJbD7U",
    "https://www.youtube.com/watch?v=ymW737-722M",
    "https://www.youtube.com/watch?v=1LyzZVkzhNg",
    "https://www.youtube.com/watch?v=hhxFmNAkDvc",
    "https://www.youtube.com/watch?v=FBhsqXYHAE4",
    "https://www.youtube.com/watch?v=nDNYN4-OYZM",
    "https://www.youtube.com/watch?v=PsAwRIT17Is",
    "https://www.youtube.com/watch?v=b0Ib9ZXxvg0",
    "https://www.youtube.com/watch?v=kYWWdDqm-5o",
    "https://www.youtube.com/watch?v=gMA1FUpuELo",
    "https://www.youtube.com/watch?v=GheaIsTd7pY",
    "https://www.youtube.com/watch?v=Un3QSlIfhYk",
    "https://www.youtube.com/watch?v=5qsptIjlHqM",
    "https://www.youtube.com/watch?v=aXcpY736XcI",
    "https://www.youtube.com/watch?v=gN1wZiwvjX4",
    "https://www.youtube.com/watch?v=DvqOdOY2a4I",
    "https://www.youtube.com/watch?v=oJ3tH0-T298",
    "https://www.youtube.com/watch?v=oml5cFYAlK80",
    "https://www.youtube.com/watch?v=UtPZcwPnvkw",
    "https://www.youtube.com/watch?v=i1EU-_Qe_28",
    "https://www.youtube.com/watch?v=YJWSAJjkTsI",
    "https://www.youtube.com/watch?v=iSIcWKEVQIw&t=0s"
    ]




def get_true_link(link):
    if (not link.startswith("https://")) and (not link.startswith("https://")):
        try:
            link = "https://"+link
            if link == "https://":
                raise EmptyInput("null")

            req.post(link)
                
        except req.exceptions.ConnectionError:
          link = "http://"+link
   
    prev_link = link
    new_link = req.post(link).url


    
    while prev_link != new_link:
        prev_link = new_link
        new_link = req.post(prev_link).url

    if new_link.endswith("&ucbcb=1"):
        new_link = new_link[:-8]
    if new_link.endswith("&t=0s"):
        new_link = new_link[:-5]
    
    if "bilibili" in new_link:
        if "&rt=V%" in new_link:
            new_link = new_link.split("&rt=V%")[0]
    
    return new_link




def checkrickroll(link: str):
    global ricklinks
    final_destination = get_true_link(link)
    #print(final_destination)
    for i in ricklinks:
        #print(f"{final_destination} vs {i}")
        if final_destination in i:
            return True
    
    return False


def lol(request):
    if request.method == "POST":
        if "handle" in request.POST:
            screenname = request.POST.get("handle", None)
            
            if random.randint(1, 1000) == 1000:
                return redirect("https://www.youtube.com/watch?v=QtBDL8EiNZo/")
            
            try:
                if checkrickroll(screenname):
                    return redirect('/result-bad/', foo='bar')
            except EmptyInput:
                return redirect("/home/")
            except req.exceptions.ConnectionError:
                return render(request, 'hello.html', {"message": "Invalid link"})
            return redirect('/result-ok/', foo='bar')
        return redirect("/report-rickroll/")

    
    return render(request, 'hello.html', {"message": "Enter a link"})

def rick_not_ok(request):
    return render(request, "rickwarning.html")

def rick_ok(request):
    return render(request, "rickok.html")

def home_re(request):
    return redirect(("/home/"))


def report_link(request):
    global ricklinks
    if request.method == "POST":
        if "handle" in request.POST:
            screenname = request.POST.get("handle", None)
            try:
                screenname = get_true_link(screenname)
            except EmptyInput:
                return redirect("/report-rickroll/")
            except req.exceptions.ConnectionError:
                return render(request, 'report.html', {"message": "Invalid link"})
            
            if screenname in ricklinks:
               return render(request, 'report.html', {"message": "Link already in blacklist!"}) 
            
            ricklinks.append(screenname)
            with open("rick_db.pkl", "wb") as fp:
                pickle.dump(ricklinks, fp)

            return render(request, 'report.html', {"message": "Added to blacklist!"}) 
        return redirect("/home/")

    return render(request, "report.html", {"message": "Enter a link to blacklist"})