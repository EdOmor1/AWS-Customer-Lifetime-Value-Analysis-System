import pymysql

# Aurora database configuration
db_host = 'your_db_host'
db_username = 'your_db_username'
db_password = 'your_db_password'
db_name = 'your_db_name'

def store_structured_data(data):
    connection = pymysql.connect(host=db_host, user=db_username, password=db_password, db=db_name)
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO ltv_data (user_id, event_type, value, timestamp) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (data['user_id'], data['event_type'], data['value'], data['timestamp']))
        connection.commit()
    finally:
        connection.close()
        print("Data stored in Aurora")

# Example usage
if __name__ == "__main__":
    sample_data = {
        'user_id': 'user_id_example',
        'event_type': 'purchase',
        'value': 100,
        'timestamp': int(time.time())
    }
    store_structured_data(sample_data)
