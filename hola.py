formulario = {"persona1": {"nombre":"Gabriela",
              "apellido":"Pinilla",
              "edad":28,
              "direccion":"tordera"},
               "persona2":{"nombre":"Daniela",
              "apellido":"Caballero",
              "edad":15,
              "direccion":"panama"},
               "persona3":{"nombre":"Marcia",
              "apellido":"Pinilla",
              "edad":38,
              "direccion":"barcelona"}}
#print(formulario["persona2"]["nombre"])
claves = formulario.keys()
for name in claves:
    print(formulario[name]["nombre"])

print(claves)