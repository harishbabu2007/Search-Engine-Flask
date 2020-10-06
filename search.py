# from urllib import request
from bs4 import BeautifulSoup
from requests import get

"""
old algorithm(very very slow)

def search(inp):
    inp = inp.replace(" ", "")
    inp = inp.lower()

    start = "https://www."

    com = ".com"
    uin = ".in"
    us = ".us"
    ca = ".ca"
    coin = ".co.in"
    org = ".org"
    it = ".it"
    io = ".io"
    au = ".au"
    couk = ".co.uk"
    iss = ".is"
    es = ".es"
    kr = ".kr"
    cokr = ".co.kr"
    ly = ".ly"
    cous = ".co.us"

    domains = [com, uin, org, us, ca, it, io, coin, au, couk, iss, es, kr, cokr, ly, cous]
    url = start + inp

    results = {}

    for i in range(len(domains)):
        try:
            html = request.urlopen(url + domains[i]).read()
            soup = BeautifulSoup(html, 'html.parser')

            title = soup.title.text.strip() 
            title = title.replace("-&nbsp", "")

            results[f"{url}{domains[i]}"] = title
        except:
            continue

    return results
"""

# using google search
# faster response
def search(term, num_results=10, lang="en"):
    usr_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/61.0.3163.100 Safari/537.36'}

    def fetch_results(search_term, number_results, language_code):
        escaped_search_term = search_term.replace(' ', '+')

        google_url = 'https://www.google.com/search?q={}&num={}&hl={}'.format(escaped_search_term, number_results+1,
                                                                              language_code)
        response = get(google_url, headers=usr_agent)
        response.raise_for_status()

        return response.text

    def parse_results(raw_html):
        soup = BeautifulSoup(raw_html, 'html.parser')
        result_block = soup.find_all('div', attrs={'class': 'g'})
        for result in result_block:
            link = result.find('a', href=True)
            title = result.find('h3')
            if link and title:
                yield link['href']

    html = fetch_results(term, num_results, lang)

    return list(parse_results(html))
