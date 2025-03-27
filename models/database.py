import pymssql, pymysql, psycopg2
from pymysql.cursors import DictCursor


class Database:
    def __init__(self, engine, user, password, database, host=None, port=None):
        self.engine = engine
        self.user = user
        self.password = password
        self.database = database
        self.host = host if (host is not None) else "localhost"
        self.port = port if (port is not None) else self.define_port()
        self.connection = self.connect()

    def connect(self):
        match (self.engine):
            case "mysql":
                return pymysql.connect(
                    user=self.user,
                    password=self.password,
                    database=self.database,
                    port=self.port,
                    host=self.host,
                    cursorclass=DictCursor,
                )
            case "sqlserver":
                return pymssql.connect(
                    user=self.user,
                    password=self.password,
                    database=self.database,
                    server=f"{self.host}:{self.port}",
                )
            case "postgresql":
                return psycopg2.connect(
                    user=self.user,
                    password=self.password,
                    dbname=self.database,
                    host=self.host,
                    port=self.port,
                )
            case _:
                return None

    def define_port(self):
        match (self.engine):
            case "mysql":
                return 3306
            case "sqlserver":
                return 1433
            case "postgresql":
                return 5432
            case _:
                return None

    def execute(self, query, args=None, fetchAll=None):
        try:
            cursor = self.connection.cursor() if (self.connection is not None) else None
            with cursor as c:
                c.execute(query, args)
                if fetchAll:
                    return c.fetchall()
                elif fetchAll == False:
                    return c.fetchone()

                self.connection.commit()
                return True
        except Exception as e:
            print("Error! : ", e)
            return False
