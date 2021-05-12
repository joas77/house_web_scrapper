import requests
from bs4 import BeautifulSoup


HOUSE_INFO_PROVIDER = "http://www.inmuebles24.com/"
#"https://casa.sapo.pt/Venda/Apartamentos/?sa=11&or=10"


if __name__=="__main__":
    print("hola")
    headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
    housing_data = requests.get(HOUSE_INFO_PROVIDER, headers=headers)
    print(housing_data)