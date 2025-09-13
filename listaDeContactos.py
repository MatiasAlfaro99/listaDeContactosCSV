import csv
import os

filename = "Contactos.csv"

# Crear archivo si no existe
if not os.path.exists(filename):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Nombre", "Teléfono", "Correo electrónico"])

# Función para agregar contacto
def agregarContacto():
    nombre = input("Nombre: ").strip()
    telefono = input("Teléfono: ").strip()
    email = input("Correo electrónico: ").strip()

    # Verificar si el contacto ya existe
    with open(filename, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Nombre"].lower() == nombre.lower():
                print("El contacto ya existe")
                return

    # Agregar contacto
    with open(filename, 'a', newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([nombre, telefono, email])
        print("Contacto añadido con éxito")

# Función para ver todos los contactos
def verContacto():
    with open(filename, 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

        if len(rows) < 2:
            print("No se encontraron contactos")
            return

        print("\nTus contactos:\n")
        for row in rows[1:]:  # Saltar encabezados
            print(f"{row[0]} | {row[1]} | {row[2]}")
        print()

# Función para buscar un contacto por nombre
def buscarContacto():
    busqueda = input("Ingresa el nombre a buscar: ").strip().lower()
    resultadoBusqueda = False

    with open(filename, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)

        # Normalizar encabezados: quitar espacios al inicio/final
        fieldnames = [name.strip() for name in reader.fieldnames]

        # Recorrer cada fila
        for row in reader:
            # Crear diccionario seguro, usando encabezados normalizados
            contacto = {field.strip(): row.get(field.strip(), "") for field in fieldnames}

            nombre = contacto.get("Nombre", "")
            telefono = contacto.get("Teléfono", "")
            correo = contacto.get("Correo electrónico", "")

            if busqueda in nombre.lower():
                print(f"{nombre} | 📲 {telefono} | ✉️ {correo}")
                resultadoBusqueda = True

    if not resultadoBusqueda:
        print("No se encontró el contacto")


# Menú principal
def main():
    while True:
        print("\nLista de contactos")
        print("1. Agregar contacto")
        print("2. Ver todos los contactos")
        print("3. Buscar contacto")
        print("4. Salir")

        eleccion = input("Elige una opción (1-4): ").strip()

        if eleccion == "1":
            agregarContacto()
        elif eleccion == "2":
            verContacto()
        elif eleccion == "3":
            buscarContacto()
        elif eleccion == "4":
            print("Hasta luego!")
            break
        else:
            print("Opción incorrecta")

if __name__ == "__main__":
    main()
