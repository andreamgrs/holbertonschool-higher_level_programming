from flask import Flask, render_template, request
import json
import io, csv
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open("items.json", "r") as file:
            data = json.load(file)
            items = data.get('items', [])  #if items doesnt exist pass an empty list
        return render_template('items.html', items=items)
    except FileNotFoundError:
        return "No items found"
    
@app.route('/products')
def products():
    type_source = request.args.get('source') #return json or csv 
    product_id = request.args.get('id', type=int)
    if product_id:
        with open("products.json", "r") as file:
            data = json.load(file)
            products_with_id = [] #new list
            for product in data:
                if product['id'] == product_id:
                    products_with_id.append(product)
            if not products_with_id:
                return render_template('product_display.html', error="Product not found")
            return render_template('product_display.html', products=products_with_id)
    elif type_source == 'json':
        with open("products.json", "r") as file:
            data = json.load(file)
        return render_template('product_display.html', products=data)
    elif type_source == 'csv':
        with open("products.csv", "r", newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader) #Convert the DictReader object to a list of dictionaries
            print(data)
        return render_template('product_display.html', products=data)
    #for database sql
    elif type_source == 'sql':
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        products = cursor.fetchall()
        products_list = []
        for product in products:
            product_name = { #This is necessary so the html can identify the object
                'name': product[1],
                'category': product[2],
                'price': product[3]
            }
            products_list.append(product_name)
        print(products_list)
        conn.close()
        return render_template('product_display.html', products=products_list)
    else:
        return render_template('product_display.html', error="Wrong source")


if __name__ == '__main__':
    app.run(debug=True, port=5000)