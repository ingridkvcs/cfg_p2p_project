from Investr import requests, json

url = "https://fear-and-greed-index.p.rapidapi.com/v1/fgi"
headers = {
    "X-RapidAPI-Key": "6932a7e3aamsh5d1f2e65f9a19afp19cd13jsn8467296d7a8a",
    "X-RapidAPI-Host": "fear-and-greed-index.p.rapidapi.com"
}


def fng(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text


response = requests.get(url, headers=headers)
fng(response.json())
fgi = response.json()['fgi']

# Prints Stats as strings

# for time, data in fgi.items():
#   print("\nTime: ", time)
#  for stats in data:
#     print(stats + ":", data[stats])


# Appends values to gauge_value in descending order

gauge_value = []

for time, data in fgi.items():
    for stats in data:
        if stats == "value":
            gauge_value.append(data[stats])


# Assigns value to label

def fng_scale(num):
    if 0 < num <= 25:
        return "Extreme Fear"
    if 26 < num <= 45:
        return "Fear"
    if 46 < num <= 55:
        return "Neutral"
    if 56 < num <= 75:
        return "Greed"
    else:
        return "Extreme Greed"
