from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.common.keys import Keys
import time
import os
import csv
from bs4 import BeautifulSoup
from random import randint
from datetime import date

driver = webdriver.Chrome()
driver.maximize_window()
dia = date.today()

def delay(n):
    time.sleep(randint(2, n))

def buscarFundo(fundo):
    # faz a pesquisa da palavra chave
    driver.get(f'https://www.youtube.com/results?search_query={fundo}')

def rolarPagina(vezes):
    # rola um numero de vezes para carregar comentarios
    for i in range(vezes):
        driver.execute_script("window.scrollBy(0, 800);")
        delay(5)

def filtrarComentarios(fundo):
    qtCmtNv = 1 # quantidade de comentarios novos
    qtCmtAt = 0 # quantidade de comentarios antigos
    comentarios = []
    while(qtCmtNv > qtCmtAt):
        for k in range(2):
            rolarPagina(2)
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")
            comentarios = soup.find_all(id='content-text')
            if k == 0:
                qtCmtAt = len(comentarios)
            if k == 1:
                qtCmtNv = len(comentarios)
    
    # extrai somente o texto das tags
    texto = []
    for c in comentarios:
        texto.append(c.text)

    # salvar no arquivo
    comentariosFiltrados = open(f"comentarios_{fundo}_{dia}.txt", "a")
    for t in texto:
        comentariosFiltrados.write(t+"\n")

    # fecha o arquivo
    comentariosFiltrados.close()

def salvarLinks():
    filename = open("fundosListados.csv", "r")
    arquivo = csv.DictReader(filename)
    fundos = []
    for coluna in arquivo:
        fundos.append(coluna["codigo"])

    links = []
    # faz a pesquisa da palavra chave e salva os links dos videos
    for f in fundos:
        buscarFundo(f)
        rolarPagina(3)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        videos = soup.find_all(id="video-title")
        atual = {}
        linksFundo = []

        for v in videos:
            linksFundo.append(v["href"])

        atual[f] = linksFundo
        links.append(atual)

    return links

def buscarComentarios(links):
    # faz a pesquisa pelos links e filtra os comentarios
    for l in links:
        for key, value in l.items():
            print(key, value)
            for each in value:
                driver.get(f"https://youtube.com{each}")
                filtrarComentarios(key)

def main():
    #buscarComentarios(salvarLinks())
    buscarComentarios([{"MXRF11": ["/watch?v=qVWwUIOU7go"]}])

main()

driver.quit()
