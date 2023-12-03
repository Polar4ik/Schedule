import requests
import os
from config import VK_TOKEN

token = VK_TOKEN # VK user token
site_url = "https://nggtk.ru/api/v2/GetScheduleGroup/" + token # college API

group_number = "17"
group_obj = {
    "group": group_number
    }


respounce = requests.post(site_url, group_obj) # POST request for API

respounce_json_data = respounce.json() # get data in json
schedule_json_data = respounce_json_data['schedule'] # get schedult

for days in schedule_json_data: # schedult day by day
    print(days['name']) # print day name
    for lesson in days['couples']:  # lessons in day
        print(lesson['i'], "Пара:", lesson['name'], "Кабинет:", lesson['office']) # print lesson
        #if "--" in lesson['name']:
        #    lesson['name'] = "Нет"
        #    print(lesson['i'], "Пара:", lesson['name'])
        #else:
        #    print(lesson['i'], "Пара:", lesson['name'], "Кабинет:", lesson['office'])
    print('\n') # next day
