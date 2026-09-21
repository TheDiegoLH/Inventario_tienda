# ================================================
# CLASE InventarioTienda
# ================================================
class InventarioTienda:
    def __init__(self, nombre_tienda):
        self.nombre_tienda = nombre_tienda
        self._productos = []  # lista de diccionarios

    # -------------------------------
    # Métodos de instancia
    # -------------------------------
    def agregar_producto(self, nombre, precio, cantidad):
        if not nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacío")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")

        # Buscar si ya existe
        for producto in self._productos:
            if producto["nombre"].lower() == nombre.lower():
                producto["cantidad"] += cantidad
                return

        # Si no existe, agregar nuevo
        self._productos.append({
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        })

    def vender_producto(self, nombre, cantidad):
        for producto in self._productos:
            if producto["nombre"].lower() == nombre.lower():
                if producto["cantidad"] < cantidad:
                    raise ValueError(
                        f"No hay suficiente stock de '{nombre}'. Disponible: {producto['cantidad']}"
                    )
                producto["cantidad"] -= cantidad
                return
        raise ValueError(f"El producto '{nombre}' no se encuentra en el inventario")

    def mostrar_inventario(self):
        if not self._productos:
            print("El inventario está vacío.")
        else:
            print("\n--- Inventario ---")
            for p in self._productos:
                print(f"{p['nombre']} - Precio: ${p['precio']} - Cantidad: {p['cantidad']}")

    def producto_mas_caro(self):
        if not self._productos:
            return None
        return max(self._productos, key=lambda p: p["precio"])

    # -------------------------------
    # Propiedades
    # -------------------------------
    @property
    def total_productos(self):
        return len(self._productos)

    @property
    def valor_total_inventario(self):
        return sum(p["precio"] * p["cantidad"] for p in self._productos)

    @property
    def productos_bajo_stock(self):
        return [p for p in self._productos if p["cantidad"] <= 5]

    # -------------------------------
    # Menú interactivo
    # -------------------------------
    def ejecutar(self):
        while True:
            print(f"\n=== Inventario de {self.nombre_tienda} ===")
            print("1. Agregar producto")
            print("2. Vender producto")
            print("3. Mostrar inventario")
            print("4. Producto más caro")
            print("5. Mostrar estadísticas")
            print("6. Productos con bajo stock")
            print("7. Salir")

            opcion = input("Elige una opción: ")

            try:
                if opcion == "1":
                    nombre = input("Nombre del producto: ")
                    precio = float(input("Precio: "))
                    cantidad = int(input("Cantidad: "))
                    self.agregar_producto(nombre, precio, cantidad)
                    print("Producto agregado correctamente.")

                elif opcion == "2":
                    nombre = input("Nombre del producto: ")
                    cantidad = int(input("Cantidad a vender: "))
                    self.vender_producto(nombre, cantidad)
                    print("Venta realizada correctamente.")

                elif opcion == "3":
                    self.mostrar_inventario()

                elif opcion == "4":
                    producto = self.producto_mas_caro()
                    if producto:
                        print(f"Producto más caro: {producto['nombre']} - ${producto['precio']}")
                    else:
                        print("Inventario vacío.")

                elif opcion == "5":
                    print(f"Total de productos: {self.total_productos}")
                    print(f"Valor total del inventario: ${self.valor_total_inventario}")

                elif opcion == "6":
                    bajos = self.productos_bajo_stock
                    if bajos:
                        print("Productos con bajo stock:")
                        for p in bajos:
                            print(f"{p['nombre']} - Cantidad: {p['cantidad']}")
                    else:
                        print("No hay productos con bajo stock.")

                elif opcion == "7":
                    print("Saliendo del sistema...")
                    break

                else:
                    print("Opción inválida. Intenta de nuevo.")

            except ValueError as e:
                print(f"Error: {e}")

# ================================================
# PROGRAMA PRINCIPAL
# ================================================
if __name__ == "__main__":
    tienda = InventarioTienda("Mi Tienda")
    tienda.ejecutar()
