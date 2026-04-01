class Inventario:
    def __init__(self):
        self.productos = {}
        
    def agregar_producto(self, nombre, cantidad):
        # Refactor: suma a lo existente en lugar de reemplazar
        self.productos[nombre] = self.productos.get(nombre, 0) + cantidad

    def obtener_inventario(self):
        return self.productos
    
    def actualizar_stock(self, nombre, nueva_cantidad):
        if nombre not in self.productos:
            raise KeyError("Producto inexistente")
        self.productos[nombre] = nueva_cantidad

    def buscar_producto(self, nombre):
        # Refactor: manejo de productos no encontrados
        return self.productos.get(nombre, "No encontrado")