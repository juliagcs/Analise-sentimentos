# SentiFII

Scripts utilizados no projeto de inovação tecnológica SentiFII.

# Visão Geral

## Fundos listados

**Todos** os scripts utilizam o arquivo csv **fundosListados** para filtrar
os fundos nas diferentes plataformas. Esses fundos foram coletados
da B3. Há 406 códigos de FIIs.

## Scripts utilizando Selenium
O script **coletarComentarios** busca o código de cada fundo no YouTube,
salvando todos os comentários dos videos inicias no resultado de busca,
que são os mais relevantes.

O script **coletarFundamentus** busca o código de cada fundo no Fundamentus,
salvando os dados relevantes desses fundos disponiveis na plataforma.

## Script utilizando a API do Twitter
O script **coletarTwitter** busca o código de cada fundo pela API do Twitter,
filtrando os tweets do Brasil.
