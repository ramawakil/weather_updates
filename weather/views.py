from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.

weather_url = 'https://weather.com/en-TZ/weather/today/l/e3098160bc6bf690b70244caadff6145e27802d46872aab77148bb873c0cb43b'


def weather(request):

    # search = request.POST.get('search')
    final_url = ''
    response = requests.get(weather_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    weather_div = soup.find('div', {'id': 'LookingAhead'})
    day_part = weather_div.find_all(class_='today-daypart')
    day_title = [item.get_text() for item in weather_div.find_all(class_='today-daypart-title')]
    day_temp = [item.get_text() for item in weather_div.find_all(class_='today-daypart-temp')]
    rain_chance = [item.get_text() for item in weather_div.find_all(class_='precip-val')]
    day_desc = [item.get_text() for item in weather_div.find_all(class_='today-daypart-wxphrase')]

    more_details_div = [item.get_text() for item in weather_div.find_all(class_='dp-details')]
    final_post = []

    for (title, desc, temp, rain) in zip(day_title,day_desc, day_temp, rain_chance):
        final_post.append((title, desc, temp, rain))

    stuff_for_frontend = {
        'final': final_post
    }

    return render(request, 'weather/weather_index.html', stuff_for_frontend)
