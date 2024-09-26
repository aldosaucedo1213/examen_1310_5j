print(" sucursal Aldo saucedo 22308051281310")
# zona de clase 
class Datos1310:
    # el constructor
    def __init__(self,horario,horario2):
        self.horario=horario
        self.horario2=horario2
    def mostrar_Datos(self):
        print(f" horario: {self.horario} va, horario {self.horario2}")
    def mi_lista(self):
        celulares1310=["numero", "email", "nombre"]
        print (celulares1310)
        for cel in celulares1310:
            print(cel)
    def diccionario(self):
        slo =	{
    "ubicacion": "calle pistache",
    "horario": "de 10am a 2 pm",
    "telefono": 65645609
}
        print(slo)
        for x,y in slo.items():
            print(x,y) 
    def mi_set(self):
        tamales1310 = {"tamal de rojo", "tamal de verde", "tamal de rajas"}
        print(tamales1310)
        for x in tamales1310:
            print(x) 
    def mi_tupla(self):
        nombre1310 = (" tamales el p", " gracias por su confiansa", "calidad de 10 años")
        print(nombre1310)
        for p in nombre1310:
            print(p) 
# creacion de objeto
info=Datos1310(10,2)
# utilizando el obj.
info.mostrar_Datos()
print(" Lista de usuarios Aldo saucedo")
info.mi_lista()
print(" Lista de ubicacion")
info.diccionario()
print(" Lista menu")
info.mi_set()
print(" Lista de eslogan ")
info.mi_tupla()



    
