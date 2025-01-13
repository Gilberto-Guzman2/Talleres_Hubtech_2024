from django.http import JsonResponse
# from django.http import HttpResponse

from datetime import datetime

def getdatetime(request):

    now = datetime.now() 
    response = {"datetima": now}
    return JsonResponse(response)

    # now = datetime.now() 
    # html = f"<html><body><h1>Son las {now} </h1></body></html>"
    # return HttpResponse(html)

    # print(request)
    # return HttpResponse("Hello, World. You're at the index.")