#rule based ai chat box

import datetime
import time

name=input("wlecome,enter your name")
presentHour=datetime.datetime.now().hour
if 5<= presentHour <=11:
   print("Good morning ",name)
elif 11<= presentHour <=17:
   print("Good afternoon ",name)
elif 17<= presentHour <=20:
   print("Good evening ",name)
else:
   print("Good night ",name) 




print("Namaste! Welcome to Rule Based ChatBot")
print("You can ask me basic questions, type 'bye' to exit.")
responses={
    "hello":"hi , Welcome.How can I help you.?",
    "how are you":"I am fine, Thank you for asking.",
    "who are you":"I am a smart rule based chatbot created by Harsh.",
    "motivate me":"You are capable of amazing things. Believe in yourself and keep pushing forward!",
    "happy":"Great! Keep spreading positivity and joy.",
    "what is functions":"Functions are blocks of code that perform a specific task and can be reused throughout a program.",
    "what is class":"A class is a blueprint for creating objects in object-oriented programming. It defines the properties and behaviors that the objects created from it will have.",
}
def getResponseBot(userQuestion):
    userQuestion = userQuestion.lower().strip()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]
        
    return "I'm sorry, I don't understand that. Can you please rephrase your question?"
while True:
  user_input=input("Please enter your message: ")
  if "bye" in user_input.lower():
    print("Goodbye! Have a great day!")
    break
  reply=getResponseBot(user_input)
  print("Bot response: ", reply)
