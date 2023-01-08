#Doesn't work
import sys
import telepot

from urinotas import getNotas
from telepot.namedtuple import InlineQueryResultArticle, InputTextMessageContent

def on_inline_query(msg):
    query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')

    articles = []
    acesso = query_string.split()
    
    try:
        if acesso[2]:
            notas = getNotas(acesso[0], acesso[1])

            for nota in notas.keys():
                resultado =  nota + '\n' + notas[nota]
                articles.append(InlineQueryResultArticle(
                    id=nota.lower(),
                    title=nota,
                    input_message_content=InputTextMessageContent(
                    message_text=resultado)
                ))
                    
                bot.answerInlineQuery(query_id, articles)

            print('ok')

    except:
        pass

def on_chosen_inline_result(msg):
    result_id, from_id, query_string = telepot.glance(msg, flavor='chosen_inline_result')

TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
bot.message_loop({'inline_query': on_inline_query,
                  'chosen_inline_result': on_chosen_inline_result},
                 run_forever='Listening ...')
