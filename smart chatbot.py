from newspaper import Article
import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings
warnings.filterwarnings('ignore')

nltk.download('punkt', quiet=True)

#Get The Article
article = Article('https://github.com/gunthercox/chatterbot-corpus/blob/master/chatterbot_corpus/data/english/ai.yml','https://github.com/gunthercox/chatterbot-corpus/blob/master/chatterbot_corpus/data/english/conversations.yml')
article.download()
article.parse()
article.nlp()
corpus = article.text

#Print Article
print(corpus)


#Tokenization
text = corpus
sentence_list = nltk.sent_tokenize(text) #Create list of sentences

#Print List Of Sentences
#print(sentence_list)

#Random Greeting Response Function
def greeting_response(text):
    text = text.lower()

    #Bots greeting response
    bot_greetings = ['Howdy!', 'Hi!', 'Hello!', 'Greetings!']

    #User greeting
    user_greetings = ['hi', 'hey', 'hello', 'greetings', 'wassup']

    for word in text.split():
        if word in user_greetings:
            return random.choice(bot_greetings)


def index_sort(list_var):
    lenght = len(list_var)
    list_index = list(range(0, lenght))

    x = list_var
    for i in range(lenght):
        for j in range(lenght):
            if x[list_index[i]] > x[list_index[j]]:
                #Swap
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp

    return list_index

#Bots Response
def bot_response(user_input):
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_response = ''
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(cm[-1], cm)
    similarity_scores_list = similarity_scores.flatten()
    index = index_sort(similarity_scores_list)
    index = index[1:]
    response_flag = 0

    j = 0
    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.0:
            bot_response = bot_response+' '+sentence_list[index[i]]
            response_flag = 1
            j = j+1
        if j > 2:
            break

        if response_flag == 0:
            bot_response = bot_response+' '+"I apologize, I don't understand."
        sentence_list.remove(user_input)

        return bot_response

#Start the chat
print('Bot: Hi I am a Smart Bot. To exit, type [bye].') 

exit_list = ['exit', 'see you later', 'bye', 'quit', 'break', 'stop']


while(True):
    user_input = input()
    if user_input.lower() in exit_list:
        print('Bot: Chat with you later, and remember... stay safe!')
        break
    else:
        if greeting_response(user_input) != None:
            print('Bot: '+greeting_response(user_input))
        else:
            print('Bot: '+bot_response(user_input))

            




 

    
    
