from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse, JsonResponse


def companylist(request):
    a = pd.read_csv("final_draft.csv")
    string=""
    for i in a["Name"]:
        string=string+"\n"+i

    return HttpResponse(string)


def riccodeCompany(request,ricCode):
    a = pd.read_csv("final_draft.csv")
    df = pd.DataFrame(a)
    data = df.loc[df[df["ricCode"]==ricCode].index,"ESG":"GovernancePillar"]
    file = data.to_dict(orient='index')
    return JsonResponse(file , safe=False)
