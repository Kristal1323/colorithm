import requests

def generate_ai_palette(input_colors=None):
    url = "http://colormind.io/api/"
    data = {"model": "default"}
    if input_colors:
        data["input"] = input_colors + ["N"] * (5 - len(input_colors))
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        result = response.json()
        return ['#%02x%02x%02x' % tuple(c) for c in result["result"]]
    except Exception as e:
        print(f"Error calling Colormind: {e}")
        return None
