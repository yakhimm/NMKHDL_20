from bs4 import BeautifulSoup
import requests

def get_weather_air(url):
    content = requests.get(url).content
    soup = BeautifulSoup(content, 'html.parser')
    weather_air = {}
    # Weather
    div_left_side = soup.find('div', {'class' : 'left-side'})
    div_weather_detail = div_left_side.find('div', {'class':'weather__detail'}).find_all('tr')
    for detail in div_weather_detail:
        details = detail.find_all('td')
        weather_air[details[0].get_text()] = details[1].get_text()

    # Air
    table_aqi = soup.find('table', {'class' : 'aqi-overview-detail__other-pollution-table'}).find('tbody')
    details = table_aqi.find_all('tr')
    for detail in details:
        split_detail = detail.find_all('td')
        name = split_detail[0].get_text()
        value = split_detail[2].find('span').get_text()
        weather_air[name] = value

    # Chất lượng không khí
    target_aqi = soup.find('div', {'class': 'aqi-value-wrapper'}).find('span', {'class': 'aqi-status__text'})
    weather_air['target'] = target_aqi.get_text() 

    return weather_air