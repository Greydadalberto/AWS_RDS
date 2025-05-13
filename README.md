# AWS RDS + MySQL + Flask API Project (Eshop)

This beginner-friendly project demonstrates how to:

* Set up a **MySQL database** on **AWS RDS**
* Create tables and insert data using SQL scripts
* Query the database
* Build a simple **Flask API** to expose your data
* Push everything to **GitHub**

---

## 📁 Project Structure

```
AWS_RDS/
|
|├— create_tables.sql       # SQL script to create tables
|├— insert_data.sql         # SQL script to insert sample data
|├— query_scripts.sql       # SQL queries for reporting
|
|├— app.py                  # Flask app with endpoints
|├— requirements.txt        # Python dependencies
|
|└— screenshots/            # Screenshots of SQL results
    └— top_customers.png
       monthly_sales.png
       products_never_ordered.png
       avg_order_value_country.png
       frequent_buyers.png

README.md               # This file
```

---

## ✅ Part 1: AWS RDS Setup

1. Log in to AWS Console.
2. Go to **RDS > Create Database**.
3. Choose:

   * **Engine**: MySQL
   * **DB Name**: `eshop`
   * **Username**: `admin`
   * **Password**: `your_password_here`
4. Allow public access and add your IP in the security group.

---

## 💄 Part 2: Create Tables & Insert Data

1. Open a terminal and connect to your RDS DB:

```bash
mysql -h your-endpoint.rds.amazonaws.com -u admin -p
```

2. Select your database:

```sql
USE eshop;
```

3. Run scripts:

```sql
source create_tables.sql;
source insert_data.sql;
```

---

## 🔍 Part 3: SQL Query Results

### 1. ✨ Top Customers by Spending

```sql
SELECT c.name, SUM(oi.quantity * oi.unit_price) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
WHERE o.status IN ('Shipped', 'Delivered')
GROUP BY c.customer_id
ORDER BY total_spent DESC;
```

**Result:**

```
+---------------+--------------+
| name          | total_spent  |
+---------------+--------------+
| Alice Smith   | 1691.00      |
| Charlie Zhang | 1200.00      |
+---------------+--------------+
```

### 2. 📅 Monthly Sales Report (Shipped/Delivered)

```sql
SELECT MONTH(order_date) AS month, SUM(oi.quantity * oi.unit_price) AS total_sales
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
WHERE o.status IN ('Shipped', 'Delivered')
GROUP BY MONTH(order_date);
```

**Result:**

```
+--------+-------------+
| month  | total_sales |
+--------+-------------+
| 11     | 1371.00     |
| 12     | 320.00      |
+--------+-------------+
```

### 3. ❌ Products Never Ordered

```sql
SELECT * FROM products
WHERE product_id NOT IN (
  SELECT DISTINCT product_id FROM order_items
);
```

**Result:**

```
(No products left un-ordered)
```

### 4. 🌎 Average Order Value by Country

```sql
SELECT c.country, AVG(order_total) AS avg_order_value
FROM (
  SELECT o.order_id, o.customer_id,
         SUM(oi.quantity * oi.unit_price) AS order_total
  FROM orders o
  JOIN order_items oi ON o.order_id = oi.order_id
  WHERE o.status IN ('Shipped', 'Delivered')
  GROUP BY o.order_id
) t
JOIN customers c ON c.customer_id = t.customer_id
GROUP BY c.country;
```

**Result:**

```
+---------+------------------+
| country | avg_order_value  |
+---------+------------------+
| USA     | 845.50           |
+---------+------------------+
```

### 5. ⭐ Frequent Buyers (More Than One Order)

```sql
SELECT c.name, COUNT(*) AS num_orders
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_id
HAVING COUNT(*) > 1;
```

**Result:**

```
+-------------+-------------+
| name        | num_orders |
+-------------+-------------+
| Alice Smith | 2          |
+-------------+-------------+
```

Screenshots of these results are saved in the `/screenshots` directory.

---

## 🌐 Part 4: Flask API

1. From the project folder:

```bash
cd AWS_RDS
python3 app.py
```

2. Access in your browser: [http://127.0.0.1:5000](http://127.0.0.1:5000)

### API Endpoints:

| Endpoint         | Description               |
| ---------------- | ------------------------- |
| `/`              | Welcome message           |
| `/top-customers` | Top customers by spending |

### Hosted API (Optional)

If deployed, your endpoint will look like:

```
http://your-ec2-ip:5000/top-customers
```

Ask for help if you'd like to deploy this on EC2 or use Docker.

---

## 🗲 Requirements

`requirements.txt`:

```
Flask
mysql-connector-python
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 🚀 GitHub Setup

```bash
git init
git remote add origin https://github.com/Greydadalberto/AWS_RDS.git
git checkout -b main
git add .
git commit -m "Initial commit"
git push -u origin main
```

---

## 🤝 Author

**Derrick Alberto Darku**
Amalitech DevOps Trainee
Email: [derrick.alberto-darku@amalitechtraining.org](mailto:derrick.alberto-darku@amalitechtraining.org)

---

## 📚 Keywords

