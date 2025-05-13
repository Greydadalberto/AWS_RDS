-- 1. Top Customers by Spending
SELECT c.name, SUM(oi.quantity * oi.unit_price) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
WHERE o.status IN ('Shipped', 'Delivered')
GROUP BY c.customer_id
ORDER BY total_spent DESC;

-- 2. Monthly Sales Report (Shipped/Delivered Only)
SELECT 
    DATE_FORMAT(o.order_date, '%Y-%m') AS month,
    SUM(oi.quantity * oi.unit_price) AS total_sales
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
WHERE o.status IN ('Shipped', 'Delivered')
GROUP BY month
ORDER BY month;

-- 3. Products Never Ordered
SELECT p.name
FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id
WHERE oi.product_id IS NULL;

-- 4. Average Order Value by Country
SELECT c.country, AVG(order_total) AS avg_order_value
FROM (
    SELECT o.order_id, c.country, SUM(oi.quantity * oi.unit_price) AS order_total
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    JOIN order_items oi ON o.order_id = oi.order_id
    WHERE o.status IN ('Shipped', 'Delivered')
