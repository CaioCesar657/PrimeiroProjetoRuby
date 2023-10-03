import pip #Importa modulo para instalação de pacotes externos.
import subprocess #Importa o modulo do subprocesso para instalação via pip de ferramentas adicionais.
import sys #Importa o modulo do sitema para obter caminhos e outras informações do sitema.
import json #Importa modulo json para retornar os dados.
import re #Importa Regex para formatação.
def install(package): #Função para pacotes adicionais dentro do próprio codigo através do instalador pip.
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    install('requests')  #Instala o pacote requests(para modulo internet).
import requests as Web #Importa o pacote requests com a palavra-chave Web.
print("Acessando a página...") #1° Passo acessando a página.
respostaInternet = Web.get('https://scodbrasil.com/teste') #Utiliza da função get para capturar informações do servidor Web.
valorInternet = Web.get('https://scodbrasil.com/teste_detalhes') #Utiliza da função get para capturar informações sobre o Valor.
conteudoWeb = respostaInternet.text #Transforma o conteudo para Texto.
valorWeb = valorInternet.text #Transforma os valores para Texto.
print("") #Espaço para padronização.
print("Capturando os dados de contato e de debito e valores...") #2° Passo Capturando os dados de contato e de débito.
formatoWeb=re.sub('<[^>]*>', '', conteudoWeb) #Formata o texto Web para JSON sem Tags.
formatoValorWeb=re.sub('<[^>]*>', '', valorWeb) #Formata os valores para JSON sem Tags.
padrãoContato =r'^.*?(\b(?:E-mail)\b.*(?:(?!\n[ \t]*$)\n.*)*)' #Seleciona apenas o texto de informações de contato.
padrãoDebito =r'^.*?(\b(?:Ano)\b.*(?:(?!\n[ \t]*$)\n.*)*)' #Seleciona apenas o texto para dados de débito.
textoContato=re.findall(padrãoContato,formatoWeb,re.M) #Padroniza o texto de contato.
textoDebito=re.findall(padrãoDebito,conteudoWeb,re.M) #Padroniza o texto de débito.
textoValor=re.findall(padrãoDebito,formatoValorWeb,re.M) #Padroniza o texto de valor.
formatoContato = '\n'.join([str(i) for i in  textoContato]) #Formata os dados de contato transformando-o em String e com espaçamentos necessarios.
formatoDebito = '\n'.join([str(i) for i in  textoDebito]) #Formata os dados de débito transformando-o em String e com devidos espaçamentos.
formatoValor = '\n'.join([str(i) for i in  textoValor]) #Formata os valores transformando-o em String e com devidos espaçamentos.
formatadoDebito=re.sub('<[^>]*>', '', str(formatoDebito)) #Formata o texto dos dados de débito para JSON sem Tags.
formatadoValor=re.sub('<[^>]*>', '', str(formatoValor)) #Formata os valores para JSON sem Tags.
print("") #Espaço para padronização.
print("Mostrando dados Capturados...") #Imprime na tela os dados de contato e de debito.
print(formatoContato) #Mostra os dados de contato.
print(formatadoDebito) #Mostra os dados de débito.
print(formatadoValor) #Mostra os dados de valores.
print("Criando Json...") #4° Passo Cria e retona o Json com os dados.
data = {} #Define as Informações para Data em lista para o Json.
todosDados = {} #Define as Informações para todos os Dados em lista para o Json.
todosDados['Total'] = [] #Cria a lista todos os Dados vazia.
data['Contato'] = [textoContato] #Adiciona os dados de Contato da lista de contato.
data['Debito'] = [textoDebito] #Adiciona os dados de Débito da lista de débito.
data['Valores'] = [textoValor] #Adiciona os Valores da lista de valores.
todosDados['Total'] = data['Contato'] + data['Debito'] + data['Valores'] #Adiciona as listas a lista geral de Dados.
with open('todosDados.txt', 'w') as outfile: #Exporta como Json uma lista contendo todos os dados.
    json.dump(data, outfile)