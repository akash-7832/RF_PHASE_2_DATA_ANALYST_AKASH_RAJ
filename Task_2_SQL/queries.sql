-- Total sales by country
SELECT country, SUM(amount) AS total_sales
FROM sales
GROUP BY country;

-- Top products by revenue
SELECT product, SUM(amount) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC;

