from flask import Flask, render_template, request, Response, jsonify, redirect, url_for 
import database as dbase
from Product import Product

db =  dbase.connect()

app = Flask(__name__)

@app.route('/')
def home():
    products = db['product']
    productsReceived = products.find()
    return render_template('index.html', products = productsReceived)


@app.route("/Articulos")
def About():
    return "<p>Hola desde el Articulo</p>"


@app.route("/Add")
def viewadd():
    return render_template("Add.html")

#Metodo POST 
@app.route("/AddProduct", methods=["POST"])
def Add():
    products = db["product"]
    name = request.form["name"]
    price = request.form["price"]
    quantity = request.form["quantity"]
    if name and price and quantity:    #si son verdaderos o estan presentes
        product = Product(name , price , quantity)
        products.insert_one(product.collection())
        reponse = jsonify({
            "name" : name,
            "price": price,
            "quantity" : quantity
        })
        return redirect(url_for("home"))
    else:
        return notFound()


# GET , POST , PUT Y DELETE

@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response



if __name__ == "__main__":
    app.run(debug=True, port=5000)
