#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
import telepot
import time, datetime

from random import randint
from urinotas import getNotas

pasta = #sua_pasta
senha = #"sua_senha"
grupo_id = #id_do_seu_grupo
meu_id = #id_adm
permissao = [str(meu_id), "dos", "usuarios", "permitidos"] #Id usuarios que podem utilizar os comandos

def verificaNota():
    try:
        notas = getNotas(pasta, senha)
        for key in notasOld.keys():
            if notasOld[key] != notas[key]:
                bot.sendMessage(grupo_id, "Notas de %s lançadas!" % key)
                return notas

        bot.sendMessage(meu_id, "Verificado as: %s" % (time.ctime())) #Log para cotrole
        return notasOld

    except Exception as e:
        bot.sendMessage(meu_id, str(e))
        return notasOld

def handle(msg):
    try:
        command = msg['text']
    except:
        command = "ARQUIVO"
    msg_id = msg['message_id']
    chat_id = msg['chat']['id']
    user_id = msg['from']['id']

    if any(str(user_id) in s for s in permissao) and command == '/start':
         bot.sendMessage(meu_id, "Hi! It's %s" % (time.ctime()), reply_to_message_id = msg_id)
    elif any(str(user_id) in s for s in permissao) and command == '/atualizar':
         try:
            notasOld = verificaNota(grupo_id, meu_id, notasOld)
            bot.sendMessage(user_id, "Atualizado", reply_to_message_id = msg_id)
         except Exception as e:
            bot.sendMessage(meu_id, str(e))

TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)

#log para controle
notasOld = getNotas(pasta, senha)
print("Iniciado... Buscando atualizações para materias abaixo")
print(notasOld.keys())

while 1:
    time.sleep(randint(2000, 4500))
    now = datetime.datetime.now()
    if (8 <= now.hour <= 22) and now.weekday() != 6:
        notasOld = verificaNota(grupo_id, meu_id, notasOld)
