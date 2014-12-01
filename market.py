''
Created on 30/07/2012

@author: OscarPC
'''
from main.companis import Company
from main.InitialValues import Initial_financial_values, Initial_agent_values
from main.agents import Agents
from time import ctime

class global_market(object):
    def __init__(self):
        self.__agent_market = {}
        self.__company_market = {}
        self.__stock_market = {}
        '''
        inicializamos a las compañias a partir de los valores predefinidos
        '''
        for name in self.__finacial_values.companies:
            self.__companyMarket[name] = Company(name, name, self.__finacial_values.number, self.__finacial_values.price)
            self.__stock_market[name]= self.__company_market[name].getValue()
            
            
        
            
        '''
        inicialiamos a los brokers
        '''
        for id in self.__agent_values.number_agent:
            pass
             
            
    def get_company_market(self):
        return self.__agent_market
    def get_agent_market(self):
        return self.__agent_market 
    def set_stok_market_trans(self, stockValue):
        self.__stockMarketValue[ctime()]= stockValue   
