import operator

from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, "homepage.html", {"website": "My website"})

def count(request):
    fulltext = request.GET['fulltext']
    words = fulltext.split()
    wordcount = len(words)
    worddictionary = {}

    for word in words:
        if word in worddictionary:
            # increase the count
            worddictionary[word] += 1
        else:
            # initializing its count
            worddictionary[word] = 1

    # sorting the worddictionary
    sorteddictionary = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    dict_to_pass = {"fulltext": fulltext, "wordcount": wordcount, "sorteddictionary": sorteddictionary}
    return render(request, "count.html", dict_to_pass)

def about(request):
    return render(request, "about.html")