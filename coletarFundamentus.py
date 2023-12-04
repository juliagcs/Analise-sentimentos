from selenium import webdriver # importando a biblioteca de webdriver
from bs4 import BeautifulSoup 
import time # O modulo time aqui foi utilizado para esperar o carregamento das paginas
import re
from pprint import pprint

navegador = webdriver.Chrome()# atribuindo o webdriver + o navegador utilizado

def buscarFundo(fundo): # faz a pesquisa do fundo no site fundamentus
    navegador.get(f'https://www.fundamentus.com.br/detalhes.php?papel={fundo}')

def pegarTab(): #pegando Informações FII
    html = navegador.page_source #passando o html da pagina para a variavel html
    soup = BeautifulSoup(html, "html.parser") #Parse o html na variável 'html' e armazene-o no formato BeautifulSoup
    todos_dados = soup.find_all('td', class_="data") #extrair informações dentro de todas as tags de tabela
    todos_label = soup.find_all('td', class_="label") #extrair informações dentro de todas as tags de tabela
    
    tab = []
    tab2 = []
    for t in todos_dados:
        tab.append(t.text)

    for t in todos_label:
        tab2.append(t.text)

    i=0
    for t in tab2:
        if t.startswith("?"):
            t = t[1:]
            tab2[i] = t
        i = i+1
    
    dados = []
    i=0
    for t in tab2:
        dados.append([t,tab[i]])
        i = i+1

    pprint(dados)
    
    
def pegarImoveis(fundo): # faz a pesquisa do fndo no site 
    navegador.get('https://fundamentus.com.br/fii_imoveis_detalhes.php?papel={}'.format(str(fundo)))
    html = navegador.page_source #passando o html da pagina para a variavel html
    soup = BeautifulSoup(html, "html.parser") #Parse o html na variável 'html' e armazene-o no formato BeautifulSoup               s
    todos_dados = soup.find_all('td') #extrair informações dentro de todas as tags de tabela
    todos_cabec = soup.find_all('th') #extrair informações dentro de todas as tags de tabela
    todas_linhas = soup.find_all('tr')
    linhasDeDados = len(todas_linhas)-1

    tab = []
    teb = []

    for t in todos_cabec:
        teb.append(t.text)
    tab.append(teb)
    teb = []
    for t in todos_dados:
        teb.append(t.text)

    i = 0
    j = 0
    c = 0
    tib = []
    tob = []
    for t in tab[0]:
        while(i < len(teb) and c < linhasDeDados):
            tib.append(teb[i+j])
            i = i+8
            c = c+1
        i = 0
        c = 0
        j = j+1
        tob.append(tib)
        tib = []

    pprint(tab)
    pprint(tob)

def pegarRendimento(fundo):
    navegador.get('https://fundamentus.com.br/fii_proventos.php?papel={}&tipo=2'.format(str(fundo)))
    html = navegador.page_source #passando o html da pagina para a variavel html
    soup = BeautifulSoup(html, "html.parser") #Parse o html na variável 'html' e armazene-o no formato BeautifulSoup               s
    todos_cabec = soup.find_all('a', class_="fdTableSortTrigger") #extrair informações dentro de todas as tags de tabela    
    todos_dados = soup.find_all('td') #extrair informações dentro de todas as tags de tabela
    todas_linhas = soup.find_all('tr')
    linhasDeDados = len(todas_linhas)-1

    tab = []
    teb = []

    for t in todos_cabec:
        teb.append(t.text)
    tab.append(teb)
    teb = []
    for t in todos_dados:
        teb.append(t.text)

    i = 0
    j = 0
    c = 0
    tib = []
    tob = []
    for t in tab[0]:
        while(i < len(teb) and c < linhasDeDados):
            tib.append(teb[i+j])
            i = i+4
            c = c+1
        i = 0
        c = 0
        j = j+1
        tob.append(tib)
        tib = []

    pprint(tab)
    pprint(tob)


def pegarHistorico(fundo):
    navegador.get(f'https://fundamentus.com.br/cotacoes.php?papel={fundo}&tela=3')
    time.sleep(2)
    historico = navegador.execute_script("""
        values = []; 
        Highcharts.charts[0].series[0].data.forEach(
            function(d){ 
                values.push(d.y) 
            });
        return values;
        """)

    print(historico)

def coletarDados():
    fundos = ["MXRF11"]#, "FCFL11", "RCB11", "HGRE11", "HGLG11", "FIIB11", "KNRI11", "VRTA11", "HGCR11"]

    for f in fundos: # faz a pesquisa de fundo por fundo 
        buscarFundo(f)
        time.sleep(2) # o Sleep é para aguardar o carregamento da pagina
        print("Pegando dados da página principal")
        pegarTab()
        print("\npegando dados dos imoveis")
        pegarImoveis(f)
        print("\npegando dados do rendimento")
        pegarRendimento(f)
        print("\npegando dados do historico")
        pegarHistorico(f)

coletarDados()
navegador.quit()
