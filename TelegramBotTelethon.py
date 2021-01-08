from telethon import TelegramClient, events, sync
import csv
import os
import threading
import logging
from time import sleep
from telethon import functions, types



# bot_token = ''
name101 = ""
api_id = 
api_hash = ""
phone = '+'
dict = {}
fieldnames = ['name']
timer = 60
messageToRemain = "empty message"
helpMessage = """/view_usernames
to view all the usernames you add.
/add @example
to add @example to the sending list.
/delete @example
to delete @example from the sending list.
/clear
to clear the list.
/send this is the whole message you wanna
to send "this is the whole message you wanna" once as a message to all the list.
/set_timer
to set a timer for your messages.
/show_timer
to show the saved timer (minutes).
/set_message
to set a message to be sent later.
/show_message
to show the saved message.
"""



bot = TelegramClient(phone, api_id, api_hash)
# bot = client.start(bot_token)
bot.connect()
if not bot.is_user_authorized():
    bot.send_code_request(phone)
    bot.sign_in(phone, input('Enter the code: '))

def reCreat():
    with open(name101+'chat_IDs.csv', mode='w') as csv_file:
        employee_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        employee_writer.writeheader()

def getTheIDHere(message):
    with open(name101+'chat_IDs.csv', mode='a') as csv_file:
        employee_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        employee_writer.writerow({'name': message})

if not os.path.exists(name101+'chat_IDs.csv'):
    reCreat()
@bot.on(events.NewMessage())
async def echo(event):
    print(event.raw_text)

@bot.on(events.NewMessage(pattern='^/start'))
async def send_welcome(event):
    await event.respond("bew bew bew")

@bot.on(events.NewMessage(pattern='^/help'))
async def viewHelp(event):
    await event.respond(helpMessage)

@bot.on(events.NewMessage(pattern='^/show_timer'))
async def viewTimer(event):
    await event.respond(str(timer))

@bot.on(events.NewMessage(pattern='^/show_message'))
async def viewMessage(event):
    await event.respond(messageToRemain)

@bot.on(events.NewMessage(pattern='^/set_timer'))
async def setTimer(event):
    global timer
    message = event.raw_text.split(' ')
    if len(message) == 2:
        try:
            timer = int(message[1])
            await event.respond("Done")
            logging.info("[Set_Timer]> setting timer to: " + str(timer))
        except Exception as e:
            logging.error("[Set_Timer]>"+str(e))
            await event.respond("Not valid timer.\nexample:\n\nset_timer 15")

@bot.on(events.NewMessage(pattern='^/set_message'))
async def setmessageToRemain(event):
    global messageToRemain
    message = event.raw_text.split(' ')
    if len(message) > 1:
        try:
            messageToRemain = ' '.join(message[1:])
            await event.respond("Done")
            logging.info("[Set_message]> setting the message to: " + messageToRemain)
        except Exception as e:
            logging.error("[Set_message]>"+str(e))
            await event.respond("Not valid message.\nexample:\n\nset_message test here 123")

@bot.on(events.NewMessage(pattern='^/view_usernames'))
async def viewing(event):
    with open(name101+'chat_IDs.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        messageToSend = ""
        list = []
        for row in csv_reader:
            if len(row) == 1 and row[0] != 'name':
                messageToSend += f'{row[0]}\n'
        try:
            await event.respond(messageToSend)
            logging.info('Done Viewing users')
        except Exception as e:
            await event.respond('Nothing is found, insert some usernames firstly.')
            logging.error(str(e))


@bot.on(events.NewMessage(pattern='^/send'))
async def SendToAll(event):
    lst = []
    with open(name101+'chat_IDs.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        messageToSend = ' '.join(event.raw_text.split(' ')[1:])
        c = 0
        for row in csv_reader:
            if len(row) == 1:
                if row[0] not in lst:
                    lst.append(row[0])

    for item in lst[1:]:
        try:
            # await bot.forward_messages(item, messages=event.message.id)
            await bot.send_message(item, messageToSend)
            logging.info("[error]>" + "message sent to: " + item)
        except Exception as e:
            logging.error("[error]>" + str(e))


@bot.on(events.NewMessage(pattern='^/add'))
async def AddByID(event):
    try:
        entity = event.raw_text.split(' ')[1]
        # print(entity, type(entity))
        with open(name101+'chat_IDs.csv', mode='a') as csv_file:
            employee_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            employee_writer.writerow({'name': entity})
        await event.respond("Done")
        logging.info("[add]>"+entity + " add successfully!")
    except IndexError:
        await event.respond("Write in right formula, please.\nexample:\n\n/add @paulo")
        logging.error("[add]>"+"IndexError not correct formula")
    except Exception as e:
        await event.respond("Sorry, not valid")
        logging.error("[add]>" + str(e))

@bot.on(events.NewMessage(pattern='^/clear'))
async def Clear(event):
    reCreat()
    await event.respond("Done")
    logging.info("[clear]>"+"Done clearing!")

@bot.on(events.NewMessage(pattern='^/delete'))


async def delete_id(event):
    lines = []
    idToBeDeleted = event.raw_text.split(' ')[1]
    with open(name101+'chat_IDs.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if len(row) != 1:
                continue
            # print(row[0], idToBeDeleted)
            if row[0] != idToBeDeleted:
                lines.append(row)
    # print(lines[1:])
    reCreat()
    with open(name101+'chat_IDs.csv', 'a') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        for line in lines[1:]:
            if len(line) != 1:
                continue
            writer.writerow({'name': line[0]})
    logging.info("[delete0id]>"+"Done Deleting: " + idToBeDeleted)
    # logging.log(0, "heelloealsld")
    await event.respond("Done")



bot.start()
# bot.log_out()
bot.run_until_disconnected()
