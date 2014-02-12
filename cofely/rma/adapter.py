from plone.app.users.browser.personalpreferences import UserDataPanelAdapter


class EnhancedUserDataPanelAdapter(UserDataPanelAdapter):
    """
    """
    def get_companyName(self):
        return self.context.getProperty('companyName', '')
    def set_companyName(self, value):
        return self.context.setMemberProperties({'companyName': value})
    companyName = property(get_companyName, set_companyName)

    def get_companyPhone(self):
        return self.context.getProperty('companyPhone', '')
    def set_companyPhone(self, value):
        return self.context.setMemberProperties({'companyPhone': value})
    companyPhone = property(get_companyPhone, set_companyPhone)

    def get_companyFax(self):
        return self.context.getProperty('companyFax', '')
    def set_companyFax(self, value):
        return self.context.setMemberProperties({'companyFax': value})
    companyFax = property(get_companyFax, set_companyFax)

    def get_deliveryStreet(self):
        return self.context.getProperty('deliveryStreet', '')
    def set_deliveryStreet(self, value):
        return self.context.setMemberProperties({'deliveryStreet': value})
    deliveryStreet = property(get_deliveryStreet, set_deliveryStreet)

    def get_deliveryPostalcode(self):
        return self.context.getProperty('deliveryPostalcode', '')
    def set_deliveryPostalcode(self, value):
        return self.context.setMemberProperties({'deliveryPostalcode': value})
    deliveryPostalcode = property(get_deliveryPostalcode, set_deliveryPostalcode)

    def get_deliveryCity(self):
        return self.context.getProperty('deliveryCity', '')
    def set_deliveryCity(self, value):
        return self.context.setMemberProperties({'deliveryCity': value})
    deliveryCity = property(get_deliveryCity, set_deliveryCity)

    def get_deliveryCountry(self):
        return self.context.getProperty('deliveryCountry', '')
    def set_deliveryCountry(self, value):
        return self.context.setMemberProperties({'deliveryCountry': value})
    deliveryCountry = property(get_deliveryCountry, set_deliveryCountry)
