from flask import Flask, request, jsonify
import math

app = Flask(__name__)

def calculate_emi(amount, interest, tenure):
    r = interest / 100  
    emi = (amount * r * (1 + r)**tenure) / ((1 + r)**tenure - 1)
    return emi

@app.route('/calculate_emi', methods=['POST'])
def calculate():
    data = request.json
    amount = data.get("amount", 50000)  
    interest = data.get("interest", 5)
    

    emi = calculate_emi(amount, interest, tenure)
    
    return jsonify({"emi": emi})

if __name__ == "__main__":
    app.run(debug=True)
