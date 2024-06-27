from django.shortcuts import render
import json
import requests

def calculate_total_calories(data):
    item = data[0]
    calories_from_fat = item['fat_total_g'] * 9
    calories_from_carbs = item['carbohydrates_total_g'] * 4
    total_calories = calories_from_fat + calories_from_carbs
    return total_calories

def home(request):
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url + query, headers={'X-Api-Key': 'hP8V6fK4YQNKyDlg/QoYdg==1ni2XZJ9Vve4fWsD'})
        try:
            api = json.loads(api_request.content)
            if api:  
                total_calories = calculate_total_calories(api)
                return render(request, 'home.html', {'api': api, 'total_calories': total_calories})
            else:
                return render(request, 'home.html', {'api': "No data found"})
        except Exception as e:
            api = "Oops! There was an error"
            return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'query': 'Enter a valid query'})

