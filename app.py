from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Menu items with prices
menu = {
    "VR": {"Single": 50, "Full": 90},
    "VN": {"Single": 50, "Full": 90},
    "VM": {"Single": 70, "Full": 110},
    "VMR": {"Single": 70, "Full": 120},
    "VMN": {"Single": 70, "Full": 120},
    "JR": {"Single": 50, "Full": 90},
    "VML": {"Full": 70},
    "CML": {"Full": 100},
    "CFR": {"Single": 80, "Full": 140},
    "CN": {"Single": 80, "Full": 140},
    "DECR": {"Single": 90, "Full": 160},
    "SCR": {"Single": 100, "Full": 180},
    "SCN": {"Single": 100, "Full": 180},
    "DECN": {"Single": 90, "Full": 160},
    "EM": {"Single": 80, "Full": 130},
    "CM": {"Single": 100, "Full": 170},
    "C65": {"Single": 100, "Full": 170},
    "CC": {"Single": 110, "Full": 200},
    "CLP": {"Single": 50, "Full": 100},
    "CLPP": {"Single": 40},
    "ER": {"Single": 70, "Full": 120},
    "EN": {"Single": 70, "Full": 120},
    "EMR": {"Single": 80, "Full": 140},
    "EMN": {"Single": 80, "Full": 140},
    "DER": {"Single": 80, "Full": 140},
    "DEN": {"Single": 80, "Full": 140},
    "ERLL": {"Full": 50},
    "CRLL": {"Full": 80}
}

@app.route('/')
def index():
    return render_template('index.html', menu=menu)

@app.route('/process_order', methods=['POST'])
def process_order():
    item_name = request.form['item_name']
    size = request.form['size']
    quantity = int(request.form['quantity'])
    amount_paid = float(request.form['amount_paid'])
    
    # Calculate total cost based on menu
    cost = menu[item_name][size] * quantity
    message = ""

    # Determine payment status
    if amount_paid == cost:
        message = "Payment successfully done."
    elif amount_paid < cost:
        message = f"Amount yet to be paid: ₹{cost - amount_paid}"
    else:
        message = f"Return change: ₹{amount_paid - cost}"

    order_details = {
        "item_name": item_name,
        "size": size,
        "quantity": quantity,
        "total_cost": cost,
        "message": message
    }
    
    return render_template('confirmation.html', details=order_details)

if __name__ == '__main__':
    app.run(debug=True)
