from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from tkinter import*

my_bot = ChatBot(
    "my_bot",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
    )
corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english')
my_bot = ChatBot(name='TanBan',read_only = True, logic_adapters = ['chatterbot.logic.BestMatch','chatterbot.logic.TimeLogicAdapter','chatterbot.logic.MathematicalEvaluation'])
'''
print("Talk to Bot")
while True:
    query=input()
    if query=='bye':
        break
    answer=my_bot.get_response(query)
    print("bot : ", answer)
'''
main = Tk()

main.geometry("500x650")

main.title("ChatBot")

img = PhotoImage(file=" ")

photoL= Label(main,image=img)

photoL.pack(pady=5)

def ask_from_bot():
    query = textf.get()
    answer_from_bot= my_bot.get_response(query)
    msag.insert(END,'You: '+query)
    msag.insert(END,'bot: '+ str(answer_from_bot))
    textf.delete(0,END)
    msag.yview(END)

frame=Frame(main)

sc= Scrollbar(frame)

msag=Listbox(frame,width=80,height=20, yscrollcommand=sc.set)

sc.pack(side=RIGHT,fill=Y)

msag.pack(side=LEFT,fill=BOTH,pady=10)

frame.pack()

textf=Entry(main,font=('Verdana',20))
textf.pack(fill=X,pady=10)

btn= Button(main,text="Send Message",font=("Verdana",20),command=ask_from_bot)
btn.pack()

def enter_function(event):
    btn.invoke()

main.bind('<Return>', enter_function)


main.mainloop()
