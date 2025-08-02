show databases;

use online_retail;

describe transactions;

select * from transactions;

-- Calculate total number of transactions:
SELECT count(*) from transactions;

-- Determine total transactions per category
SELECT
    prod_cat_code,
    COUNT(*) AS total_transactions
FROM
    transactions
GROUP BY
    prod_cat_code
ORDER BY
    total_transactions DESC;

-- Find sum of product quantity 
SELECT
    prod_cat_code,
    SUM(QTY) AS total_product_quantity
FROM
    transactions
GROUP BY
    prod_cat_code
ORDER BY
    total_product_quantity DESC;


-- Identify first and latest transaction dates
SELECT
    MIN(tran_date) AS first_transaction_date,
    MAX(tran_date) AS latest_transaction_date
FROM
    transactions;

-- Calculate sum of transactions per date
SELECT
    DATE(tran_date) AS transaction_date,
    SUM(total_amt) AS total_daily_transactions
FROM
    transactions
GROUP BY
    tran_date
ORDER BY
    tran_date;

-- Total Sales revenue
SELECT SUM(total_amt) AS total_revenue FROM transactions;

-- Total tax collected 
SELECT SUM(Tax) AS total_tax_collected FROM transactions;

-- Monthly sales trend
SELECT DATE_FORMAT(tran_date, '%Y-%m') AS month, SUM(total_amt) AS monthly_sales
FROM transactions
GROUP BY month
ORDER BY month;

-- Number of unique customers 
SELECT COUNT(DISTINCT cust_id) AS total_customers FROM transactions;

-- Peak transaction date
SELECT tran_date, COUNT(*) AS num_transactions
FROM transactions
GROUP BY tran_date
ORDER BY num_transactions DESC
LIMIT 1;

