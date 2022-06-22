from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.product import Product
from utils.db import db

products = Blueprint('products', __name__)

@products.route("/")
def index():
    products = Product.query.all()
    return render_template('index.html', products = products)

@products.route("/new", methods=['POST'])
def add_product():
    nombre = request.form['nombre']
    categoria = request.form['categoria']
    precio = request.form['precio']
    stock = request.form['stock']
    new_product = Product(nombre, categoria, precio, stock)
    db.session.add(new_product)
    db.session.commit()
    flash("Producto AGREGADO con exito")
    return redirect(url_for('products.index'))

@products.route('/update/<id>', methods=["POST", "GET"])
def update(id):
    product = Product.query.get(id)
    if request.method == "POST":
        product.nombre = request.form["nombre"]
        product.categoria = request.form["categoria"]
        product.precio = request.form["precio"]
        product.stock = request.form["stock"]
        db.session.commit()
        return redirect(url_for("products.index"))
    flash("Producto ACTUALIZADO con exito")
    return render_template("update.html", product = product)

@products.route('/delete/<id>')
def delete(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    flash("Producto DEPURADO con exito")
    return redirect('/')

@products.route("/about")
def about():
    return render_template('about.html')