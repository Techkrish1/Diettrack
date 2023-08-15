from django.shortcuts import render

def home(request):

    import json
    import requests
    
    if request.method == 'POST':
        query =request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query=' # this is the api url of Nutrition
        api_request = requests.get(api_url + query, headers= {'X-Api-Key': 'hP8V6fK4YQNKyDlg/QoYdg==1ni2XZJ9Vve4fWsD'}) # this is my api key for api-ninjas website
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "oops! there was an error"
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'query': 'Enter a valid query'})

