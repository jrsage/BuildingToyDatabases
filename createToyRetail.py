import sqlite3

conn = sqlite3.connect('toyRetail.db')
c = conn.cursor()

#Tax Table
c.execute('''
    CREATE TABLE tax (
        taxID int PRIMARY KEY,
        state varchar(2),
        taxRate decimal(5,5)
    );
''')

#Item Table
c.execute('''
    CREATE TABLE item (
        itemID int PRIMARY KEY,
        type varchar,
        color varchar,
        size varchar(4),
        price decimal(7,2),
        margin decimal(7,2)
    );
''')

#Store Table
c.execute('''
    CREATE TABLE store (
        storeID int PRIMARY KEY,
        district int,
        region int,
        address varchar,
        state varchar(2),
        zip int(5),
        phone varchar(12)
    );
''')

#Customer Table
c.execute('''
    CREATE TABLE customer(
        customerID PRIMARY KEY,
        fName varchar,
        lName varchar,
        birthday varchar(10),
        address varchar,
        state varchar(2),
        zip int(5),
        phone varchar(12),
        isLoyalty int(1)
    );
''')

#Sales Table
c.execute('''
    CREATE TABLE sales(
        salesID int PRIMARY KEY,
        storeID int,
        customerID int,
        paymentType varchar,
        transactionTotal decimal (7,2),
        taxTotal decimal (7,2),
        marginValue decimal (7,2)
    );
''')

conn.commit()
conn.close()
