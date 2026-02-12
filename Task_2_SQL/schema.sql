CREATE TABLE sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    sales_person VARCHAR(100),
    country VARCHAR(50),
    product VARCHAR(100),
    amount DECIMAL(10,2),
    boxes_shipped INT,
    sale_date DATE
);

