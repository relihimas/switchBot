from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from datetime import date

# paginas = ['https://www.nintendo.com/pt_BR/games/detail/metroid-dread-switch/',
#            'https://www.nintendo.com/pt_BR/games/detail/gang-beasts-switch/',
#            'https://www.nintendo.com/pt_BR/games/detail/eastward-switch/',
#            'https://www.nintendo.com/pt_BR/games/detail/super-smash-bros-ultimate-switch/',
#            'https://www.nintendo.com/pt_BR/games/detail/star-wars-knights-of-the-old-republic-switch/']
#
# pagina = 'https://www.nintendo.com/pt_BR/games/detail/metroid-dread-switch/'

def webprecos(pagina):


    global lista
    lista = []
    # print(date.today().strftime('%d/%m/%Y'))

    # for pagina in paginas:
    html = urlopen(pagina)
    soup = BeautifulSoup(html, 'html.parser')

    titulo = pagina.split("/")[6].replace("-", " ").capitalize()
    preco = soup.find('span', {'class': 'h2 msrp'}).getText().strip()

    lista.append(f'{titulo}: {preco}')
    return str(lista)
