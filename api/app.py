from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL Database connection setup
def get_db_connection():
    connection = mysql.connector.connect(
        host='eshop.cjqcisyogjs1.eu-west-1.rds.amazonaws.com',
        user='admin',
        password='Refactor2025',
        database='eshop'
    )
    return connection

# Endpoint: Top Customers by Spending
@app.route("/top-customers")
def top_customers():
    try:
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("""
            SELECT c.name, SUM(oi.quantity * oi.unit_price) AS total_spent
            FROM customers c
            JOIN orders o ON c.customer_id = o.customer_id
            JOIN order_items oi ON o.order_id = oi.order_id
            WHERE o.status IN ('Shipped', 'Delivered')
            GROUP BY c.customer_id
            ORDER BY total_spent DESC
        """)
        result = cursor.fetchall()
        cursor.close()
        db.close()
        return jsonify(result)
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500



# Root endpoint
@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to the Eshop API',
        'endpoints': {
            'top_customers': '/top-customers'
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
