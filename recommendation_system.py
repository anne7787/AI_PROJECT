# Crear un sistema de recomendación simple usando Python    

# Sistema simple de recomendación de libros 

def recomendar_libros(usuario):
    recomendaciones = {
        "Ana": ["Cien años de soledad", "El amor en los tiempos del cólera"],
        "Luis": ["1984", "Rebelión en la granja"],  
        "Pedro": ["El principito", "Momo"]
    }
    return recomendaciones.get(usuario, ["Libro no disponible"])

usuario = input("Ingresa tu nombre: ")
print("Te recomendamos estos libros:", recomendar_libros(usuario))

# haz una recomendación de libros usando listas 
    
# Sistema simple de recomendación de libros usando GitHub Copilot

def recomendar_libros(usuario):
    recomendaciones = {
        "Ana": ["Cien años de soledad", "El amor en los tiempos del cólera"],
        "Luis": ["1984", "Rebelión en la granja"],
        "Pedro": ["El principito", "Momo"]
    }
    return recomendaciones.get(usuario, ["Libro no disponible"])

usuario = input("Ingresa tu nombre: ")
print("Te recomendamos estos libros:", recomendar_libros(usuario))
