import psycopg2
from psycopg2 import OperationalError

try:
    conn=psycopg2.connect (
        host="localhost",
        database="postgres",
        user="postgres",
        password="Dinuk"
    )
    print("Successful connection")
except OperationalError as e:
    print("Connection error")