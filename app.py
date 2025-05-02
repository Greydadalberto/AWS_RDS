from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL Database connection setup
def get_db_connection():
    connection = mysql.connector.connect(
        host='eshop.cjqcisyogjs1.eu-west-1.rds.amazonaws.com',
        user='yourusername',
        password='yourpassword',
        database='eshop'
    )
    return connection

# Endpoint: Top Customers by Spending
@app.route('/top-customers', methods=['GET'])
def top_customers():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        query = '''
        SELECT c.customer_id, c.name, SUM(oi.quantity * oi.unit_price) AS total_spent
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id
        JOIN order_items oi ON o.order_id = oi.order_id
        WHERE o.status IN ('Shipped', 'Delivered')
        GROUP BY c.customer_id, c.name
        ORDER BY total_spent DESC
        '''
        cursor.execute(query)
        results = cursor.fetchall()
        return jsonify({
            'status': 'success',
            'data': results,
            'count': len(results)
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500
    finally:
        cursor.close()
        connection.close()

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
