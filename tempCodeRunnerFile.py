cursor.execute('''
            CREATE TABLE IF NOT EXISTS customer
            (username VARCHAR(20),
            password VARCHAR(20),
            name VARCHAR(20),
            age INTEGER,
            city VARCHAR(20)),
            account_number INTEGER,
            status BOOLEAN)
                   ''')
