from utils.db import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45))
    categoria = db.Column(db.String(45))
    precio = db.Column(db.String(45))
    stock = db.Column(db.Integer)

    def __init__(self, nombre, categoria, precio, stock):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock
