from telegram.ext import Updater, CommandHandler, MessageHandler,    Filters, InlineQueryHandler
from webpreco import webprecos


pagina = 'https://www.nintendo.com/pt_BR/games/detail/metroid-dread-switch/'


def start(update, context):
    totalupdate = update['message']
    dadosuser = totalupdate['chat']
    username = dadosuser['first_name']
    update.message.reply_text(f"Olá {username}! Eu sou o switchRaks, bot de controle de preços para jogos do Switch! O que deseja?")

def add(update, context):
    totalupdate = update['message']
    dadosuser = totalupdate['chat']
    userid = dadosuser['id']
    update.message.reply_text(
        f"Novo jogo adicionado!")
    print(f'Para o userid: {userid}')

def lista(update, context, pagina):
    preco = webprecos(pagina)
    update.message.reply_text(f'Segue:\n {preco}')


def error(update, context):
    print(f"update {update} caused error {context.error}")

def main():
    updater = Updater('TOKEN', use_context=True)
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("add", add))
    dp.add_handler(CommandHandler("lista", lista))
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ =="__main__":
    main()
