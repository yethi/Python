'''
Agents, players or brokeers
'''
from main.InitialValues import Initial_agent_values 
from main.companis.Company import Accion

class Agent_stats(object):
    def __init__(self, value):  
        self.__agent_value = Initial_agent_values()
        self.__id= value
        self.__tipo = self.agent_value.tipo
        self.__activo_liquido = self.agent_value.activo_liquido
        self.__activo_inmovi = {}
        self.__confianza = self.__agent_value.confianza
        self.__maximo_valor_positivo = self.__agentValue.maximo_valor_positivo
        self.__maximo_valor_negativo = self.__agentValue.maximo_valor_negativo
        self.__grado_riesgo = self.__agentValue.grado_riesgo
        self.__grado_psicopata = self.__agentValue.grado_psicopata
         
    def get_id(self):
        return self.__id
    def get_active_liquido(self):
        return self.__activo_liquido
    def get_active_inmovi(self):
        return self.__activo_inmovi

class Agent_actions(object):
    def __init__(self):
        pass
    def insert_accion(self,accion):
        self.__activo_inmovi[accion.get_company()]=accion
    def del_accion(self,key):
        self.__activo_inmovi.pop(key)
    def comprar_accion(self):
        pass
    def vender_accion(self):
        pass
    def calculo_valor_actual(self):
        pass
    


class Broker(Agent_stats, Agent_actions):
    def __init__(self, id):
        Agent_stats.__init__(self, id)

    
    
    

