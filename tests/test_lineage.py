from ora_lineage import table_lineage,simple_column_lineage

SQL="""INSERT INTO dwh.customer_dim (customer_id, customer_name)
SELECT c.customer_id, c.customer_name
FROM crm.customers c;"""

def test_table_lineage():
    e=table_lineage(SQL)
    assert e[0].source=="CRM.CUSTOMERS"
    assert e[0].target=="DWH.CUSTOMER_DIM"

def test_column_lineage():
    e=simple_column_lineage(SQL)
    assert e[0].target=="DWH.CUSTOMER_DIM.CUSTOMER_ID"
