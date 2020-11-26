
# Importar bibliotecas necessárias

import json
# A Biblioteca json pode analisar Strings JSON ou arquivos. 
# A biblioteca analisa o JSON em um dicionário ou numa lista Python. 
# Também pode converter dicionários ou listas Python em Strings JSON.

from tweepy import OAuthHandler, Stream, StreamListener
# Tweepy é um pacote Python de código aberto que oferece uma maneira muito conveniente de acessar a API do Twitter com Python. 
# O Tweepy inclui um conjunto de classes e métodos que representam os modelos do Twitter e os endpoints da API, 
# e trata de forma transparente vários detalhes de implementação, como: Codificação e decodificação de dados.

from datetime import datetime
# O módulo denominado datetime é utilizado para trabalhar com datas e horas.
# Uma das classes definidas no módulo datetime é a classe datetime.

# Cadastrar as chaves de acesso do Twitter

# API Key
consumer_key = "cRtzmbxtYZEEI4YciMRZHbKsc"
# API secret key
consumer_secret = "raFbMTcyRK3DmOMcuXD5k8vRsrqk51w6IbVLxNcMr8NSDhs6s5"
# Access token
access_token = "1330566070759985154-OdxvY5s8T0i69BpUJ1vJxXCZHyPURH"
#Access token secret
access_token_secret = "ZrfYTVjDa2OTsA6KTuPUdgXxjVvMaJXx6ZJ9lSzALSheT"

# Definir um arquivo de saída para armazenar os tweets coletados

# Usando o modulo datetime vamos definir a data e hora atual, 
# para isso usamos o método now () criando um objeto datetime contendo a data e hora atuais.
data_hoje = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
# Vamos atribuir os Tweets coletados a um arquivo usando out
out = open(f"collected_tweets_{data_hoje}.txt","w")

# Implementar uma classe para conexão com o Twitter

class MyListener(StreamListener):

    def on_data(self,data):
        #print(data)
        itemString = json.dumps(data)
        out.write(itemString +"\n")
        return True

    def on_error(self,status):
        print(status)

# Implementado nossa Função Main

if __name__ == "__main__":
    l = MyListener()
    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)

    stream = Stream(auth,l)
    stream.filter(track=["Trump"])