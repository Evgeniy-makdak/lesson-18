from sqlite3 import OperationalError

import psycopg2


def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


connection = create_connection(
    "postgres", "postgres", "Swaq32123", "127.0.0.1", "5432"
)


def create_database(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


create_database_query = "CREATE DATABASE main_animals"
create_database(connection, create_database_query)


def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")

create_shelter_info_table = """
CREATE TABLE IF NOT EXISTS shelter_info_table (
  id SERIAL PRIMARY KEY,
  id_shelter_info integer NOT NULL, 
  fc_animal_id integer NOT NULL,
  fc_id_outcome_subtype integer NOT NULL,
  outcom_month integer NOT NULL,
  outcom_year integer NOT NULL,
  fc_outcom_type integer NOT NULL,
  age_upon_outcom VARCHAR(255) NOT NULL,
)
"""

execute_query(connection, create_shelter_info_table)


create_animal_dict_table = """
CREATE TABLE IF NOT EXISTS animal_dict (
  id SERIAL PRIMARY KEY,
  animal_id VARCHAR(255) NOT NULL, 
  fc_animal_type integer NOT NULL,
  name VARCHAR(255),
  fc_breed integer NOT NULL,
  fc_color1 integer NOT NULL,
  fc_color2 integer,
  date_of_birth DATETIME
)
"""

execute_query(connection, create_animal_dict_table)

create_outcom_subtype_table = """
CREATE TABLE IF NOT EXISTS outcom_subtype_table (
  id SERIAL PRIMARY KEY,
  id_outcom_subtype integer NOT NULL , 
  name_outcom_subtype VARCHAR(255),
)
"""

execute_query(connection, create_outcom_subtype_table)

create_type_dict_table = """
CREATE TABLE IF NOT EXISTS type_dict_table (
  id SERIAL PRIMARY KEY,
  id_type integer NOT NULL , 
  name_type VARCHAR(255),
)
"""

execute_query(connection, create_type_dict_table)

create_breed_dict_table = """
CREATE TABLE IF NOT EXISTS breed_dict_table (
  id SERIAL PRIMARY KEY,
  id_breed integer NOT NULL , 
  name_breed VARCHAR(255),
)
"""

execute_query(connection, create_breed_dict_table)

create_colour_dict_table = """
CREATE TABLE IF NOT EXISTS colour_dict_table (
  id SERIAL PRIMARY KEY,
  id_colour integer NOT NULL , 
  name_colour VARCHAR(255),
)
"""

execute_query(connection, create_colour_dict_table)
