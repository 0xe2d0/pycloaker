from pycloaker.funcs import *


class PyCloaker:
    def __init__(self,humanRedirect,botRedirect):

        self.ipAddresses = []
        self.cityNames = []
        self.countryNames = []

        self.humanRedirect = humanRedirect
        self.botRedirect = botRedirect


    
    def blockedCities(self,cityNames):
        self.cityNames = cityNames
        return True
    
    def blockedCountries(self,countryNames):
        self.countryNames = countryNames
        return True
    
    def blockedIpAddresses(self,ipAddresses):
        self.ipAddresses = ipAddresses
        return True
    

    def cloak(self,ip,userAgent):
        check = mainFunc(
            ip,
            userAgent,
            blockedIpAddresses=self.ipAddresses,
            blockedCities=self.cityNames,
            blockedCountries=self.countryNames
        )

        if check == True:
            return self.humanRedirect
        else:
            return self.botRedirect

        
