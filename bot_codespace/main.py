import telebot
#to avoid sharing api key.. i created a separate python file which consists api key for my bot
from constants import API_KEY
import json

with open('python.json') as file:
    data = json.load(file)

#initializing bot with api key
bot = telebot.TeleBot(API_KEY,parse_mode=None)

#mapping send variable with bot.send_message method
send = bot.send_message

#defining some functions for emojis "just for fun"
def hello(message):
    bot.send_message(message.chat.id,"✋")
def cool(message):
    bot.send_message(message.chat.id,"💻")
def laugh(message):
    send(message.chat.id,"📱")
#kishore

#creating a function to fetch data from json
def fetch(command):
    return data[command]["explanation"] +"🧑‍💻 \n\n" + data[command]["syntax"]+"\n\n"+ data[command]["next"]


#for start command
@bot.message_handler(commands=["start","hello"])
def start(message):
    hello(message)
    result = " Hey there... ✋\n Need to learn new programming language...💻\n\n dont worry I'm here to help you...\n I am a virtual bot Created to help others...🤖\n please Enter the following commands...\n\n /python - to start python  \n /c - to start c \n /cpp - to start c++ \n /java - to start java \n /HTML - to start HTMl"
    send(message.chat.id,result)

#for muruga command "just for testing purpose"
@bot.message_handler(commands=["muruga"])
def muruga(message):
    bot.send_photo(message.chat.id,"https://miro.medium.com/v2/resize:fit:439/1*ZYyXvhYDGvELzYoXYpPLMg.png")

#for python command
@bot.message_handler(commands=["python"])
def python(message):
    bot.send_photo(message.chat.id,"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRh4zu2rGA8O90sKDRweHk7XogaXttx9-uEfQ&usqp=CAU")
    result = '''PYTHON!! \t yay...🍾\n
    /python_introduction - to know about python\n
    /python_hello_world - how print statement works...\n
    /python_comment_line - how to comment a line in python\n
    /python_variables - how to create and use variables\n
    /python_Numeric_types - Numeric types in python\n
    /python_Type_Casting -  To convert one data type to another data type\n
    /python_Strings - what is a string?\n
    /python_String_Slicing-
    /python_Modify_Strings-
    /python_Escape_Characters-
    '''
    send(message.chat.id,result)

#for python_introduction command
@bot.message_handler(commands=["python_introduction"])
def python_hello_world(message,commands):
    print(commands)
    bot.send_photo(message.chat.id,data["python_introduction"]["image"])
    send(message.chat.id,fetch("python_introduction"))

#for python_hello_world command
@bot.message_handler(commands=["python_hello_world"])
def python_hello_world(message):
    bot.send_photo(message.chat.id,data["python_hello_world"]["image"])
    send(message.chat.id,fetch("python_hello_world"))

#for pythoncomment_line command    
@bot.message_handler(commands=["python_comment_line"])
def python_comment_line(message):
    laugh(message)
    send(message.chat.id,fetch("python_comment_line"))

#for pythoncomment_line command    
@bot.message_handler(commands=["python_variables"])
def python_variables(message):
    bot.send_photo(message.chat.id,data["python_variables"]["image"])
    send(message.chat.id,fetch("python_variables"))

#for python_Numeric_types command 
@bot.message_handler(commands=["python_Numeric_types"])
def python_variables(message):
    bot.send_photo(message.chat.id,data["python_Numeric_types"]["image"])
    send(message.chat.id,fetch("python_Numeric_types"))
#for python_Type_Casting command 
@bot.message_handler(commands=["python_Type_Casting"])
def python_variables(message):
    bot.send_photo(message.chat.id,data["python_Type_Casting"]["image"])
    send(message.chat.id,fetch("python_Type_Casting"))

#for python_Strings command 
@bot.message_handler(commands=["python_Strings"])
def python_variables(message):
    bot.send_photo(message.chat.id,data["python_Strings"]["image"])
    send(message.chat.id,fetch("python_Strings"))

#for python_String_Slicing command 
@bot.message_handler(commands=["python_String_Slicing"])
def python_variables(message):
    bot.send_photo(message.chat.id,data["python_String_Slicing"]["image"])
    send(message.chat.id,fetch("python_String_Slicing"))

# #for python_Modify_Slicing command
@bot.message_handler(commands=["python_Modify_Strings"])
def python_variables(message):
    bot.send_photo(message.chat.id,data["python_Modify_Strings"]["image"])
    send(message.chat.id,fetch("python_Modify_Strings"))

#for python_String_Concatenation command
@bot.message_handler(commands=["python_String_Concatenation"])
def python_variables(message):
    bot.send_photo(message.chat.id,data["python_String_Concatenation"]["image"])
    send(message.chat.id,fetch("python_String_Concatenation"))         

#for python_Format_Strings command
@bot.message_handler(commands=["python_Format_Strings"])
def python_variables(message):
    bot.send_photo(message.chat.id,data["python_Format_Strings"]["image"])
    send(message.chat.id,fetch("python_Format_Strings"))

#for python_Escape_Characters command
@bot.message_handler(commands=["python_Escape_Characters"])
def python_variables(message):
    bot.send_photo(message.chat.id,data["python_Escape_Characters"]["image"])
    send(message.chat.id,fetch("python_Escape_Characters"))

#for python_String_Methods command
@bot.message_handler(commands=["python_String_Methods"])
def python_variables(message):
    bot.send_photo(message.chat.id,data["python_String_Methods"]["image"])
    send(message.chat.id,fetch("python_String_Methods"))


#calling bot polling function
bot.polling()

#muruga