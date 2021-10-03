 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters 
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
 
def new_member(update, callback):
    name = update.effective_user.first_name
    update.message.reply_text(f'Bienvenido {name} use el comando /rules para leer las reglas',
    reply_markup=InlineKeyboardMarkup([   
            [InlineKeyboardButton(text='💠GitHub💠', url='https://github.com/Luisma535')],                     
            [InlineKeyboardButton(text='💠Twitter💠', url='https://twitter.com/Luisma5352')],
            [InlineKeyboardButton(text='💠Blog💠', url='https://luisma535.github.io')]                   
    ])
)
 
def rules(update,context):
    name = update.effective_user.first_name
    update.message.reply_text(f"{name} Estas son las reglas:\n\n\n Reglas")

if __name__ == '__main__':

    updater = Updater(token='TOKEN', use_context=True)

    dp = updater.dispatcher
    
    dp.add_handler(MessageHandler(filters = Filters.status_update.new_chat_members, callback=new_member)) 
    dp.add_handler(CommandHandler('rules',rules))
    
    updater.start_polling()
    print('Bot Online...')
    updater.idle()