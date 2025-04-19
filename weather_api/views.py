from django.shortcuts import render ,HttpResponse       # type: ignore
import requests                             # type: ignore
api_keys='25b335a4127ae1dbe6ada781d1ff79ea'
# Create your views here.

def  index(request):
        context=None
        if request.method =='POST':
            city= request.POST.get('city')
            data= requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_keys}').json()
            print(data)
            main = data["weather"][0]["main"]
            description =data["weather"][0]['description']
            temp= data['main']['temp']
            wind= data['wind']['speed']
            name= data['name']
    # print(main,description)
            context={
                'main':main,
                'description':description,
                'temp':temp,
                'wind':wind,
                'name':name
            }
        return render(request,'index.html',context)


