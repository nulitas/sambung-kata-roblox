import os
import urllib.request
import json
from dotenv import load_dotenv

load_dotenv()
url = os.environ.get("ID_DICT_URL")
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        words = response.read().decode('utf-8').splitlines()
        words = set([w.strip().lower() for w in words if w.strip() and ' ' not in w and '-' not in w])
        print(f"URL: {url}")
        print(f"Total words (filtered): {len(words)}")
        print(f"Contains 'angpao': {'angpao' in words}")
        print(f"Contains 'lalat': {'lalat' in words}")
except Exception as e:
    print(f"Failed {url}: {e}")
