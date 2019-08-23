import time
texto="Hola.Como te llamas?"
print (texto)
nombre = input("")
print("Y tu apellido",nombre + "?")
apellido = input("")
print("Me alegra conocerte",nombre,apellido + "!!!")
time.sleep(1)
print("Puedo hacerte unas preguntas",nombre + "?")
siono = input("")
if (siono == "Si"or siono =="si"or siono =="SI"or siono =="Bueno"or siono =="BUENO"or siono =="bueno"or siono =="okay"or siono =="OKAY"or siono =="Okay"or siono =="ok"or siono =="ok"or siono =="OK"):
    print("Okay, aqui vamos")
    time.sleep(1)
    print("Que día naciste?(00)")
    día = input("")
    print("En que mes?(00)")
    mes = input("")
    print("Y en que año?(0000)")
    año = input("")

else:
    print("Bueno no pasa nada, sera en otro momento")




time.sleep(15)
