import random
import math

class Empresa:
    def __init__(self):
        """Inicializa la clase Empresa con una lista de trabajadores y una lista de sueldos iniciales en cero."""
        self.trabajadores = [
            "Juan Pérez", "María García", "Carlos López", "Ana Martínez",
            "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez",
            "Isabel Gómez", "Francisco Díaz", "Elena Fernández"
        ]
        self.sueldos = [0] * len(self.trabajadores)

    def asignar_sueldos_aleatorios(self):
        """Asigna sueldos aleatorios a los trabajadores.
        Los sueldos son números enteros entre 300,000 y 2,500,000."""
        self.sueldos = [random.randint(300000, 2500000) for _ in self.trabajadores]
        print("Sueldos asignados exitosamente.")

    def clasificar_sueldos(self):
        """Clasifica los sueldos en 'Bajo', 'Medio' y 'Alto' y muestra la clasificación para cada trabajador."""
        for trabajador, sueldo in zip(self.trabajadores, self.sueldos):
            clasificacion = self.clasificar_sueldo(sueldo)
            print(f"{trabajador}: ${sueldo:,} - {clasificacion}")

    def clasificar_sueldo(self, sueldo):
        """Clasifica un sueldo individual en 'Bajo', 'Medio' o 'Alto'."""
        if sueldo < 500000:
            return "Bajo"
        elif sueldo < 1500000:
            return "Medio"
        else:
            return "Alto"

    def ver_estadisticas(self):
        """Muestra estadísticas sobre los sueldos, incluyendo el más alto, el más bajo, el promedio y la media geométrica."""
        if not self.sueldos:
            print("No se han asignado sueldos aún.")
            return
       
        max_sueldo = max(self.sueldos)
        min_sueldo = min(self.sueldos)
        promedio_sueldo = sum(self.sueldos) / len(self.sueldos)
        media_geometrica = self.calcular_media_geometrica(self.sueldos)

        print(f"Sueldo más alto: ${max_sueldo:,}")
        print(f"Sueldo más bajo: ${min_sueldo:,}")
        print(f"Promedio de sueldos: ${promedio_sueldo:,.2f}")
        print(f"Media geométrica: ${media_geometrica:,.2f}")

    def calcular_media_geometrica(self, sueldos):
        """Calcula la media geométrica de una lista de sueldos.
        Maneja excepciones en caso de datos no válidos."""
        try:
            return math.exp(sum(math.log(s) for s in sueldos if s > 0) / len(sueldos))
        except ValueError as e:
            print(f"Error al calcular la media geométrica: {e}")
            return float('nan')

    def reporte_sueldos(self):
        """Genera un reporte detallado para cada trabajador con el sueldo base, descuentos y sueldo líquido."""
        if not self.sueldos:
            print("No se han asignado sueldos aún.")
            return
       
        for trabajador, sueldo in zip(self.trabajadores, self.sueldos):
            descuento_salud = sueldo * 0.07
            descuento_afp = sueldo * 0.12
            sueldo_liquido = sueldo - descuento_salud - descuento_afp
            print(f"{trabajador}:")
            print(f"  Sueldo Base: ${sueldo:,}")
            print(f"  Descuento Salud (7%): ${descuento_salud:,.2f}")
            print(f"  Descuento AFP (12%): ${descuento_afp:,.2f}")
            print(f"  Sueldo Líquido: ${sueldo_liquido:,.2f}")
            print()

def obtener_opcion_menu() -> int:
    """Solicita al usuario que seleccione una opción del menú y valida que sea una opción válida (1-5)."""
    while True:
        try:
            opcion = int(input("Seleccione una opción (1-5): "))
            if 1 <= opcion <= 5:
                return opcion
            else:
                print("Por favor, seleccione una opción válida entre 1 y 5.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entre 1 y 5.")

def mostrar_menu():
    """Muestra el menú del programa y permite al usuario seleccionar una opción para ejecutar la función correspondiente."""
    empresa = Empresa()

    while True:
        print("\nMenu:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
       
        opcion = obtener_opcion_menu()

        if opcion == 1:
            empresa.asignar_sueldos_aleatorios()
        elif opcion == 2:
            empresa.clasificar_sueldos()
        elif opcion == 3:
            empresa.ver_estadisticas()
        elif opcion == 4:
            empresa.reporte_sueldos()
        elif opcion == 5:
            print("Gracias por usar el programa. ¡Hasta luego!")
            break

if __name__ == "__main__":
    mostrar_menu()
