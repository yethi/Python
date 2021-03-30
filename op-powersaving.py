#!/usr/bin/python
#################################################################################
# Check the powersaving status for HP nodes op-powersaving.sy                  #
# For GEN 10 or other                                                           #
#################################################################################


from pathlib import Path
import os, sys
import xml.etree.ElementTree as ET
CONREP_PATH='/tmp/conrep_current.dat'


class validation_powersaving:
        def __init__(self,path):
                HW=os.popen('sudo facter hw_model').read()
                if Path(path):
                        rm='sudo rm -rf '+path
				                        os.system(rm)
                creation='sudo conrep -s -f '+path
                os.system(creation)
                self.__check=''

                if 'Gen10' in HW:
                        self.__VAR = { "Thermal_Shutdown":"Enabled","ASR_Status":"Disabled","Power_Regulator":"Static_High_Performance_Mode","Thermal_Configuration":"Optimal_Cooling","Intel_Hyper-Threading":"Enabled","Redundant_Power_Supply_Mode":"Balanced_Mode","Intel_Turbo_Boost_Technology":"Enabled","Energy_Efficient_Turbo":"Disabled","Power-On_Delay":"No_Delay","Minimum_Processor_Idle_Power_Core_C-State":"No_C-states","Minimum_Processor_Idle_Power_Package_C-State":"No_Package_State","Energy/Performance_Bias":"Maximum_Performance","Collaborative_Power_Control":"Disabled","Workload_Profile":"General_Power_Efficient_Compute","Custom_POST_Message":"TCDN-v8"}
                else:
                        self.__VAR = {"HP_Power_Regulator":"HP_Static_High_Performance_Mode","Power-On_Delay":"No_Delay","HP_Power_Profile":"Maximum_Performance","Intel_QPI_Link_Power_Management":"Disabled","Intel_Minimum_Processor_Idle_Power_State":"No_C-States","Intel_Minimum_Processor_Idle_Power_Package_State":"No_Package_State","Intel_PCI_Express_Generation_20_Support":"Force_PCI-E_Generation_2","Memory_Speed_with_2_DIMMs_per_Channel":"1333MHz_Maximum","Collaborative_Power_Control":"Disabled","Energy_Performance_Bias":"Maximum_Performance"}


        def check_PS(self):
                tree = ET.parse(path)
                root = tree.getroot()
                check =''
                for tag,value in self.__VAR.items():
                        state = False;
                        for element in root:
                                if tag in element.get('name') and value in element.text:
                                        state = True
                        if state:
                                check = check + tag+': Correct\n'
                        else:
                                check = check + tag+': Incorrect\n'


                return check


check = validation_powersaving(CONREP_PATH)
print(check.check_PS())