from django.shortcuts import render,HttpResponse
from joblib import load

model=load('./saved_model/model.joblib')
# Create your views here.
def index(request):
    return render(request,"index.html")

def output(request):
    temp_max=request.GET['temp_max']
    temp_min=request.GET['temp_min']
    wind_max=request.GET['wind_max']
    wind_min=request.GET['wind_min']
    precipitation=request.GET['precipitation']
    r_humid=request.GET['r_humid']
    y_pred=model.predict([[temp_max,temp_min,r_humid,precipitation,wind_max,wind_min]])
    y=y_pred[0]
    list1=[temp_max,temp_min,r_humid,precipitation,wind_max,wind_min,y]
    for i in list1:
            if i=="":
                return render(request,"weather.html")
    context={
        "temp_max":temp_max,
        "temp_min":temp_min,
        "r_humid":r_humid,
        "precipitation":precipitation,
        "wind_max":wind_max,
        "wind_min":wind_min,
        "y":y
        
    }
    print(y_pred)
    return render(request,"output.html",context)