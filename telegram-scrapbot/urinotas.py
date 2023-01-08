# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def getNotas(username, password):
    URL="https://portal.santoangelo.uri.br/portal_aluno/login.aspx"
    headers = {'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",    'content-type': "application/x-www-form-urlencoded",    }
    link="ensino/shw_discs.aspx?curr=173&ansm=TODOS"

    s=requests.Session()
    s.headers.update(headers)
    r=s.get(URL)
    soup=BeautifulSoup(r.content, "html.parser")

    VIEWSTATEGENERATOR=soup.find(id="__VIEWSTATEGENERATOR")['value']
    VIEWSTATE=soup.find(id="__VIEWSTATE")['value']
    EVENTVALIDATION=soup.find(id="__EVENTVALIDATION")['value']
    EVENTARGUMENT=soup.find(id="__EVENTARGUMENT")['value']
    EVENTTARGET=soup.find(id="__EVENTTARGET")['value']

    login_data={"__VIEWSTATE":VIEWSTATE,"__VIEWSTATEGENERATOR":VIEWSTATEGENERATOR,"__EVENTVALIDATION":EVENTVALIDATION,"__EVENTARGUMENT":EVENTARGUMENT,"__EVENTTARGET":EVENTTARGET,"1":"RB1","TextBox1":username,"TextBox2":password,"Button3":"Entrar"}

    r=s.post(r.url, data=login_data)
    r.url = r.url.replace("menu.aspx", link)
    output = s.get(r.url)
    soup = BeautifulSoup(output.content, 'html.parser')
    notas = soup.find(id="DataGrid1")

    dicionario = {}
    for tr in notas.findAll('tr',{'class': 'textos'}):
        td = [x.text for x in tr.findAll('td')]
        if ('{13}'.format(*td) == 'CURSANDO'):
            dicionario['{2}'.format(*td)] = ('Nota 1: {7} Nota 2: {8} Nota 3: {9} Exame: {11}'.format(*td))

    return dicionario
