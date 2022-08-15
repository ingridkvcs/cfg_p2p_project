from Lendr import requests, json
from Lendr import go

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

fg_data1 = response.json()
fg_data = response.json()['fgi']

# Gauge Chart

fg_score = round(fg_data.get("now", {}).get("value", 0), 2)
fg_rating = fg_data.get("now", {}).get("valueText", "Error")
fg_prev = round(fg_data.get("previousClose", {}).get("value", 0), 2)
fg_ts = fg_data1.get("lastUpdated", {}).get("humanDate", "")

fig = go.Figure(go.Indicator(
    mode="gauge+number+delta",
    value=fg_score,
    delta={"reference": fg_prev, },
    title={"text": "Current Rating ({}): {}".format(fg_ts[0:10], fg_rating.capitalize())},
    domain={"x": [0, 1], "y": [0, 1]},
    gauge={"axis": {"range": [0, 100]},
           "bar": {"color": "#333333", },
           "steps": [
               {"range": [0, 25], "color": "#FF7777", },
               {"range": [25, 45], "color": "#FFCC88", },
               {"range": [45, 55], "color": "#FFFF55", },
               {"range": [55, 75], "color": "#CDFF55", },
               {"range": [75, 100], "color": "#77FF77", }
           ],
           }))

fig.update_layout(paper_bgcolor=None, font={"color": "black", })

fig.update_traces(
    gauge={
        "axis": {
            "tickmode": "array",
            "tickvals": [1, 25, 50, 75, 100],
            "ticktext": ["Extreme Fear", "Fear", "Neutral", "Greed", "Extreme Greed"],
        }
    }
)

if __name__ == '__main__':
    fig.write_html("templates/graph.html")

fg_pc_score = round(fg_data.get("previousClose", {}).get("value", 0), 2)
fg_pc_rating = fg_data.get("previousClose", {}).get("valueText", "Error")

# One Week


fg_owa_score = round(fg_data.get("oneWeekAgo", {}).get("value", 0), 2)
fg_owa_rating = fg_data.get("oneWeekAgo", {}).get("valueText", "Error")

# One Month


fg_oma_score = round(fg_data.get("oneMonthAgo", {}).get("value", 0), 2)
fg_oma_rating = fg_data.get("oneMonthAgo", {}).get("valueText", "Error")

# One Year


fg_oya_score = round(fg_data.get("oneYearAgo", {}).get("value", 0), 2)
fg_oya_rating = fg_data.get("oneYearAgo", {}).get("valueText", "Error")
