# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
# import datetime
# from spy import *

# async def hi(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     log(update, context)
#     await update.message.reply_text(f'Hi {update.effective_user.first_name}')


# async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     log(update, context)
#     await update.message.reply_text(f'/hi\n/time\n/help\n/sum')


# async def time(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     log(update, context)
#     await update.message.reply_text(f'{datetime.datetime.now().time()}')


# async def sum(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     log(update, context)
#     msg = update.message.text
#     print(msg)
#     items = msg.split()  
#     x = int(items[1])
#     y = int(items[2])
#     await update.message.reply_text(f'{x}+{y} = {x+y}')