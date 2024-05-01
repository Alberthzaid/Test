#Esquema / Schema / Objeto

class Product: #Clase del producto
    #Atributos
    def __init__(self, name, price, quantity): #constructor 
        self.name = name
        self.price = price
        self.quantity = quantity
    #Metodos
    def collection(self):
        structure = {
            "Nombre":self.name,
            "Precio":self.price,
            "Cantidad":self.quantity
        }
        return structure