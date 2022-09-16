from django.shortcuts import render
# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request
  
  
def home(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+ city +'&appid=0bb239bd01a7dffc3ab9df9c61ac09d0').read()
  
        # converting JSON data to a dictionary
        list_of_data = json.loads(source)
        # data for variable list_of_data
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "weather": str(list_of_data['weather'][0]['main']),
        }
        print(data)
    else:
        data ={}
    return render(request, "index.html", data)