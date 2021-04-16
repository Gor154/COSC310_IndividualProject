import requests
from bs4 import BeautifulSoup
def search(text):
    S = requests.Session()

    URL = "https://en.wikipedia.org/w/api.php"
    SEARCHPAGE = text

    PARAMS = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": SEARCHPAGE
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()

    res = ""
    soup = BeautifulSoup(DATA["query"]["search"][0]["snippet"],"html.parser")
    restext = soup.get_text()+"\n"
    res = res+"I'm not sure what you mean. Here's a wikipedia article I found about "+DATA["query"]["search"][0]["title"]+" that might be helpful\n"
    res += "Snippet preview:\n"
    res+= restext
    resurl = "https://en.wikipedia.org/wiki/"
    formatted_title=DATA["query"]["search"][0]["title"]
    formatted_title = formatted_title.replace(" ","_")
    resurl += formatted_title
    res+="Link to article:\n"
    res+=resurl
    return res
