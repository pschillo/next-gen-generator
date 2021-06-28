from telegram.ext import Updater,Filters,Dispatcher,CommandHandler,MessageHandler,ConversationHandler
import logging

# # # # # # # # # # # # # # Telegram formalities # # # # # # # # # # # # # # # #
# this bot's name: NextGen Generator
# this bot's unique tag: nextgen_generator_bot
# this bot's unique token, INSERT TOKEN HERE:
token = ''

# # # # # # # # # # # # # # # text bricks # # # # # # # # # # # # # # # # # # #
start_message = 'I am the NextGen Generator bot. Use me.'

# # # # # # # # # # # # # # # feedback range # # # # # # # # # # # # # # # # # #
FEEDBACK_1 = range(1)

# # # # # # # # # # # # # # # custom keyboards # # # # # # # # # # # # # # # # #
custom_keyboard_1 = [['OK!'],
                   ['commands'],
                   ['help']]

# # # # # # # # # # # # # # # # reply markups # # # # # # # # # # # # # # # # #
reply_markup_1 = telegram.ReplyKeyboardMarkup(custom_keyboard_1)

# # # # # # # # # # # # # # # # functions # # # # # # # # # # # # # # # # # # #
# the start function handles the first command and  delivers the first message
# (only!) in the very first chat between the user and the bot
def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text=start_message, reply_markup=reply_markup_1)
    return FEEDBACK_1

# # # # # # # # # # # # # # # # fallbacks # # # # # # # # # # # # # # # # # # #
def start_fallback(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text=start_fallback_message)
    return FEEDBACK_1

# # # # # # # # # # # # # # # # # cancel # # # # # # # # # # # # # # # # # # # #
# sends cancel confirmation message and ends conversation
def cancel(update, context):
    context.bot.send_messge(chat_id=update.message.chat_id, text=cancel_message)
    return ConversationHandler.END

# # # # # # # # # # # # # #  # # # main # # # # # # # # # # # # # # # # # # # #
def main():

    # # # # # # # # # # # more formalities # # # # # # # # # # # # # # # # # # #
    # logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    # update and dispatch
    updater = Updater(token=token, use_context=True)
    dp = updater.dispatcher

    # # # # # # # # # # # #  # handlers # # # # # # # # # # # # # # # # # # # #
    start_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states = {
            FEEDBACK_1: [MessageHandler(Filters.text, convo_1)]
        },
        fallbacks=[CommandHandler('cancel', cancel), MessageHandler(~Filters.text, start_fallback)]
    )

    # # # # # # # # # # # # # adding handlers # # # # # # # # # # # # # # # # #
    dp.add_handler(start_handler)

    # # # # # # # # # # # #  # important # # # # # # # # # # # # # # # # # # # #
    updater.start_polling()
    updater.idle()

# # # # # # # # # # # # # other important stuff # # # # # # # # # # # # # # # #
if __name__ == "__main__":
main()
