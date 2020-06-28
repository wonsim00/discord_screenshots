class cached:
    def __init__(self, variable):
        self.__variable = variable
    
    def __get__(self, instance, owner):
        return self.__variable