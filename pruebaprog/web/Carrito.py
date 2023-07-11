class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, obras):
        id = str(obras.id)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "obras_id": obras.id,
                "nombre": obras.nombre,
                "preciou":obras.precio,
                "acumulado": obras.precio,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += obras.precio
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, obras):
        id = str(obras.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restart(self, obras):
        id = str(obras.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= obras.precio
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(obras)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True