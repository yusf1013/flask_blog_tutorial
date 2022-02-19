from sqlalchemy import create_engine, text

conn_str = "mysql://root:iit123@localhost/blogdb"
engine = None
conn = None


def initialize_db():
    global engine
    global conn

    engine = create_engine(conn_str, echo=True)
    conn = engine.connect()

    # comment this out if you don't want to reset database everytime
    sql_execute_file("./schema.sql")


def sql_raw_query(query, data):
    if not data:
        return conn.execute(text(query))
    else:
        return conn.execute(text(query), data)


def sql_execute_file(file_path):
    file = open(file_path)
    queries = file.read().strip()
    queries = queries.split(";")
    for query in queries:
        if query:
            sql_raw_query(query)
