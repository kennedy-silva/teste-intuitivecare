from bs4 import BeautifulSoup
from requests import get
import wget

# obetendo a requisição
url = "http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar"
page_response = get(url)

# parseando a página html
page_soup = BeautifulSoup(page_response.text, 'html.parser')

# obtendo o tiss mais atualizado
tiss_atualizado = page_soup.find('li', class_='item-2652')
for tag in tiss_atualizado.find_all('a', href=True):
    url_tiss = tag['href']
    url_tiss = str(url_tiss)
    url_tiss = 'http://www.ans.gov.br'+url_tiss

    # obtendo a requisição da página do tiss mais atualizado
    tiss_response = get(url_tiss)
    tiss_page_soup = BeautifulSoup(tiss_response.text, 'html.parser')

    tabela_arquivos = tiss_page_soup.find('table')
    for tag in tabela_arquivos.tbody.tr.find_all('a', href=True):
        url_arquivo = tag['href']
        url_arquivo = str(url_arquivo)
        url_arquivo = 'http://www.ans.gov.br'+url_arquivo

    # baixando o arquivo
    print('Baixando o arquivo...')
    filename = wget.download(url_arquivo)
