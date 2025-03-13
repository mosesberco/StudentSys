import mysql.connector

# Example of creating a connection to the database
def create_connection():
    conn = mysql.connector.connect(
        host="your_database_host",
        user="your_username",
        password="your_password",
        database="your_database"
    )
    return conn

# Generic function to create a table
def create_table(table_name, columns):
    """
    Create a table in the database.

    Args:
        table_name (str): The name of the table to be created.
        columns (dict): A dictionary where keys are column names, and values are column types (e.g., {"id": "INT", "name": "VARCHAR(100)"})

    Returns:
        None
    """
    conn = create_connection()
    cursor = conn.cursor()

    # Prepare column definitions for SQL query
    column_defs = ", ".join([f"{col} {type}" for col, type in columns.items()])

    # Create table SQL query
    create_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_defs})"

    try:
        cursor.execute(create_query)
        conn.commit()
        print(f"Table '{table_name}' created successfully.")
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")
    finally:
        cursor.close()
        conn.close()

# Example usage:
create_table('students', {
    'id': 'INT PRIMARY KEY AUTO_INCREMENT',
    'name': 'VARCHAR(100)',
    'email': 'VARCHAR(100)',
    'age': 'INT'
})
