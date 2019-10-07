import telepot
import time
from telepot.namedtuple import ReplyKeyboardMarkup
from telepot.namedtuple import KeyboardButton
# from telepot.namedtuple import ReplyKeyboardRemove
from gruppi import *
from risorse import *
from informazioni import *
from orari import *


# configurazione del bot e inizializzazione
TOKEN = '973948450:AAFHy9bP3mivPwTqFU7HpZ2uq6pN3Yt2Ymg'
bot = telepot.Bot(TOKEN)

# Spiegazioni comandi
select = 'Seleziona una voce dalla tastiera \n'
home = '/home Ritorna alla pagina principale del bot \n'


# funzione principale
def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(
        msg)  # inizializzazione delle variabili
    name = msg["from"]["first_name"]
    if content_type == 'text':
        comando = msg['text']

        # pulsantiera principale
        if (comando == '/start') or (comando == '/home'):
            bot.sendMessage(chat_id,
                            text="Ciao %s! " % name + select + '\n' +
                            info + gruppi + contatti + risorse + orario,
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[[KeyboardButton(text='/info'),
                                           KeyboardButton(text='/gruppi')],
                                          [KeyboardButton(text='/contatti'),
                                           KeyboardButton(text='/risorse')],
                                          [KeyboardButton(text='/orario')]]))

        # info del fiup
        if (comando == '/info'):
            bot.sendMessage(chat_id,
                            text=abstract + '\n' + scopo + '\n' +
                            rules + '\n\n' + home,
                            parse_mode='markdown')

        # Avvia la pulsantiera relativa ai gruppi
        if (comando == '/gruppi'):
            bot.sendMessage(chat_id,
                            primo + secondo + terzo + opzionali + altro,
                            parse_mode='markdown',
                            reply_markup=ReplyKeyboardMarkup(
                                keyboard=[[KeyboardButton(text='/primo'),
                                           KeyboardButton(text='/secondo')],
                                          [KeyboardButton(text='/terzo'),
                                           KeyboardButton(text='/opzionali')],
                                          [KeyboardButton(text='/altro'),
                                           KeyboardButton(text='/home')]]))

        if (comando == '/primo'):
            bot.sendMessage(chat_id, infoPrimo,
                            parse_mode='markdown',
                            disable_web_page_preview=True)
        if (comando == '/secondo'):
            bot.sendMessage(chat_id, infoSec,
                            parse_mode='markdown',
                            disable_web_page_preview=True)
        if (comando == '/terzo'):
            bot.sendMessage(chat_id, infoTer,
                            parse_mode='markdown',
                            disable_web_page_preview=True)
        if (comando == '/opzionali'):
            bot.sendMessage(chat_id, infoOpz,
                            parse_mode='markdown',
                            disable_web_page_preview=True)
        if (comando == '/altro'):
            bot.sendMessage(chat_id, infoAltro,
                            parse_mode='markdown',
                            disable_web_page_preview=True)

        # Avvia la pulsantiera del regolamento
        if comando == '/contatti':
            bot.sendMessage(chat_id,
                            contatti + '\n' + infoContatti + '\n' + social,
                            parse_mode='markdown',
                            disable_web_page_preview=True)

            # bot.sendMessage(chat_id, text = text="*bold* _italic_
            # `fixed width font` [link](http).", parse_mode = 'markdown')

        # Avvia la pulsantiera delle risorse
        if comando == '/risorse':
            bot.sendMessage(chat_id,
                            text=risorse + '\n' + mega + github + stampe,
                            parse_mode='markdown',
                            disable_web_page_preview=True)

        if comando == "/orario":
            bot.sendMessage(chat_id,
                            text=appDM + booking + aule,
                            parse_mode='markdown',
                            disable_web_page_preview=True)


bot.message_loop(on_chat_message)
print('Sto funzionando, spegnimi con CTRL+C')


while 1:
    time.sleep(10)
