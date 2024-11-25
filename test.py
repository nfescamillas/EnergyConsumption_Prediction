import requests

"""Test Data for Deployment"""

# Use the url below for running on local
# run the following code upon buidling docker 
# docker run -it --rm -p 9696:9696  docker_image_name

### url = 'http://localhost:9696/predict'

# Use the url below for running on the cloud with pythonaanywhere
url = 'https://nikkiescamillas.pythonanywhere.com/predict'
data ={ 'lagging_kvarh': 54.83,
        'leading_kvarh':46.3, 
        'co2': 0.03,
        'lagging_pf':76.4,
        'leading_pf':100.0, 
        'nsm':42300, 
        'weekstatus': 'Weekday', 
        'day': 'Monday', 
        'load_type': 'Maximum_Load', 
        'month': 8, 
        'hour': 11}

response = requests.post(url, json=data).json()
print(response)