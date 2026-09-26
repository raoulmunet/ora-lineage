INSERT INTO dwh.customer_dim (customer_id, customer_name)
SELECT c.customer_id, c.customer_name
FROM crm.customers c;
