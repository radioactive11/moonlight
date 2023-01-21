from loguru import logger
import psycopg2
from psycopg2 import sql

from base import BaseDataLoader
from exceptions import NotConnectedError


class PostgreSQLDataLoader(BaseDataLoader):
    def connect(self, host: str, port: int, user: str, password: str, database: str):
        try:
            self.__conn = psycopg2.connect(
                dbname=database, host=host, port=port, user=user, password=password
            )
            logger.info(f"Connected to PostgreSQL database: {database}")
            self.connected = True
            return True, ""

        except Exception as e:
            logger.critical(
                f"Error {str(e)} connecting to PostgreSQL database: {database}"
            )
            self.connected = False
            return False, str(e)

    def get_headers(self, table_name: str):
        if not self.connected:
            raise NotConnectedError("Not connected to PostgreSQL database")
        cur = self.__conn.cursor()
        cur.execute(
            sql.SQL("SELECT * FROM {} LIMIT 0").format(sql.Identifier(table_name))
        )
        headers = [desc[0] for desc in cur.description]
        cur.close()
        return headers

    def get_data(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM table_name")
        data = cur.fetchall()
        cur.close()
        return data

    def close(self):
        if self.connected:
            logger.info("Closing PostgreSQL connection")
            self.__conn.close()

    def __del__(self):
        self.close()
