'''
Created on 30/07/2012

@author: OscarPC
'''
from time import ctime, time
from main import InitialValues
from main.InitialValues import Initial_financial_values
from random import random



class stock(object):
    def __init__(self, company, id, number, price):
        self._number = number
        self._owener = id
        self._price = price
        self._company = company

class financial_inform(object):
    def __init__(self, ai, ac, pl, pc, ing, cs,amo):
        self._activo_inm = ai
        self._activo_cir = ac
        self._pasivo_lar = pl
        self._pasivo_cor = pc
        self._ingresos = ing
        self._costs = cs
        self._amortiza = amo
        self._analisis = dict (EVA = self.__ingresos-self.__costs-self.__amortiza,
                                r_fondo_maniobra = 100*((self.__activo_cir-self.__pasivo_cor)/self.__pasivo_lar), 
                                r_tesoreria = 100*((self.__activo_cir+self._ingresos)/self.__pasivo_cor),
                                r_endeudamiento = 100*(self.__activo_cir+self.__activo_inm)/self.__pasivo_lar,
                                r_acido = 100*self.__activo_cir/self.__pasivo_cor
                               )
    def analisis(self):
        return self.__analisis
        
class Company(object):
    def __init__(self, namec, numberc, pricec):
        self.__name = namec
        self.__stock = stock(company = namec, id =namec, number = numberc, price=pricec)
        self.__finacial_inform={}
        self.__finacial_inform [time()]=financial_inform(Initial_financial_values.activo_inm,
                                                          Initial_financial_values.activo_cir,
                                                          Initial_financial_values.pasivo_lar,
                                                          Initial_financial_values.pasivo_cor,
                                                          Initial_financial_values.ingresos,
                                                          Initial_financial_values.costes,
                                                          Initial_financial_values.amortiza
                                                         )
    def get_fechas_informes(self):
        return self.__finacial_inform.key()
    def add_informe(self, date):
        
        ''' 
        figure out the last date
        '''
        list_fechas = self.__finacial_inform.keys()
        list_fechas_order = list_fechas.sort()
        fecha_anterior = list_fechas_order[-1]
        
        '''
        new account year:
            frist, it was good (>0.5) or bad year, improve = generate better range of
            bad year company less money =  0.9
            good year company improve, more money= 1.1  
            then change the value 
        '''
        
        if random.random() < 0.5:
            value = 0.9
        else:
            value = 1.1
        
        self.__finacial_inform[date] = financial_inform(value*self.__finacial_inform[fecha_anterior]._activo_inm,
                                                         value*self.__finacial_inform[fecha_anterior]._activo_cir,
                                                         value*self.__finacial_inform[fecha_anterior]._pasivo_lar,
                                                         value*self.__finacial_inform[fecha_anterior]._pasivo_cor,
                                                         value*self.__finacial_inform[fecha_anterior]._ingresos,
                                                         value*self.__finacial_inform[fecha_anterior]._costes,
                                                         value*self.__finacial_inform[fecha_anterior]._amortia,                          
                                                        )
    def get_analisis(self, date):
        return self.__finalcial_inform[date].analisis
        
            
        
        
        
        
        
   
    
    
    
    
