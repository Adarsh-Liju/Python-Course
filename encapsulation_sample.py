class Mobile:
    def __init__(self,company,software):
        self.__company=company
        self.__software=software
    def get_company(self):
        return self.__company
    def get_software(self):
        return self.__software
    def set_company(self,a):
        self.__company=a
    def set_software(self,b):
        self.__software=b
ala=Mobile("on","ox")
ala.set_software("OxygenOs")
ala.set_company("OnePlus")
print(ala.get_company())
print(ala.get_software())
