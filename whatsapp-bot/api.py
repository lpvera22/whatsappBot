from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from urllib.request import Request, urlopen

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    # if 'citação' in incoming_msg:
    #     # retorne uma citação 
    #     r = requests.get('https://api.quotable.io/random')
    #     if r.status_code == 200:
    #         data = r.json()
    #         quote = f'{data["content"]} ({data["author"]})'
    #     else:
    #         quote = 'Não consegui recuperar uma citação neste momento, desculpe.'
    #     msg.body(quote)
    #     responded = True
    # if 'gato' in incoming_msg or 'gata' in incoming_msg:
    #     # retorne uma foto de gato
    #     msg.media('https://cataas.com/cat')
        # responded = True
    # if not responded:
    #     # msg.body(incoming_msg)
    #     msg.body('Só conheço frases e gatos famosos, desculpe!')
    num_media = int(request.values.get("NumMedia"))
    if num_media>0:
        print('num media',num_media)
        quote=''
        for i in range(num_media+1):
            print(i)
            mediaType= request.values.get('MediaContentType'+str(i), '')
            if mediaType=='text/vcard':
                fileUrl=request.values['MediaUrl'+str(i)]
                quote=quote+str(i)+'-'+fileUrl+'\n'
                print(quote)
                # req= Request(fileUrl,headers={'User-Agent': 'Mozilla/5.0'})
                # webpage = urlopen(req).read().decode("utf-8") 
                # x = webpage.split('\n')

                # print(x)
            msg.body(quote)
            
            
            responded=True
    return str(resp)

if __name__ == '__main__':
   app.run(debug=True)