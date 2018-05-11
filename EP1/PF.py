#import json 

class Carros(): #objeto
    def __init__(self, marca, modelo, versao, preco, categoria, espaco_interno, economia, desempenho, conforto, seguranca, custo_beneficio, desvalorizacao):
        self.marca = marca
        self.modelo = modelo
        self.versao = versao
        self.preco = preco
        self.categoria = categoria
        self.espaco_interno = espaco_interno
        self.economia = economia
        self.desempenho  = desempenho
        self.conforto = conforto 
        self.seguranca = seguranca
        self.custo_beneficio = custo_beneficio
        self.desvalorizacao = desvalorizacao
    pass

carros = {"carros":{}}


carros["carros"][civic.modelo] = Carros("honda","civic","si",160000,"sedä esportivo",3,3,4,3,4,1,3)
 
carros["carros"][up.modelo] = Carros("VW","up","speed", 50000,"subcompacto",4,5,4,2,5,2,2)

print(carros["carros"]["up"].modelo,carros["carros"]["])

# Lendo dic com os carros

#with open("carros.json","r") as dados:
 #   carros = json.load(dados)


#cria uma classe carros com todos o carros e seus atributos dentro, podem ser definidos



#carros["carros"] = "Carros(Honda, Civic, SI,160000,Seda Médio, 3,3,5,4,4,1,2 )"




#with open("carros.json","w") as dados:
 #   lista_alterada = json.dumps(carros,sort_keys=True)
  #  dados.write(lista_alterada)

        
    
 