AWS_RDS

# AWS RDS MySQL Project

This project demonstrates how to set up a MySQL database on AWS RDS, populate it with sample data, run SQL queries, and build a simple Flask API to expose query results.

---

## 📁 Project Structure
AWS_RDS/
│
├── app.py # Flask API for executing queries
├── db_setup.sql # SQL script to create tables and insert data
├── queries.sql # SQL script containing advanced queries
├── requirements.txt # Python package dependencies
├── README.md # This documentation
├── /screenshots # Screenshots of query results
└── /api_docs # API documentation


---

## ✅ Steps Taken

### 1. **Create RDS MySQL Instance**
- Launched a MySQL DB instance on AWS RDS.
- Created database named: `eshop`.
- Saved endpoint, username, and password for later use.

### 2. **Connect to RDS from CLI**
```bash
mysql -h eshop.cjqcisyogjs1.eu-west-1.rds.amazonaws.com -P 3306 -u admin -p

# AWS RDS MySQL Exercise: E-Shop Analytics

## Overview
This project demonstrates how to set up a MySQL database using AWS RDS, populate it with e-commerce data, and run analytical SQL queries.

## Setup

1. **AWS RDS Setup**:
   - MySQL 8.x
   - Public access enabled
   - Database name: `eshop`

2. **Tables and Data**:
   - Four tables: `customers`, `products`, `orders`, `order_items`
   - Data inserted via SQL scripts

## SQL Queries

1. **Top Customers by Spending** – Aggregates total spend per customer.
2. **Monthly Sales Report** – Shows monthly sales for shipped/delivered orders.
3. **Products Never Ordered** – Lists products with no sales.
4. **Average Order Value by Country** – Average spend per order grouped by country.
5. **Frequent Buyers** – Customers with more than one order.

All queries can be found in `sql/queries.sql`.

## Screenshots

All screenshots of query results are available in the `screenshots/` directory.

## Optional API

A basic API exposing each SQL query is available in the `api/` folder (optional). See `api-docs/endpoints.md` for documentation.

## How to Run

1. Connect to your RDS instance using MySQL client.
2. Run `create_tables.sql` and `insert_data.sql`.
3. Run queries from `queries.sql`.

## Author

[GreydadAlberto]  
[5/5/25]

