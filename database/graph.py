from neo4j import GraphDatabase
from config import Config


class GraphDB:

    def __init__(self):
        self.driver = GraphDatabase.driver(
            Config.NEO4J_URI,
            auth=(
                Config.NEO4J_USERNAME,
                Config.NEO4J_PASSWORD
            )
        )

    def close(self):
        self.driver.close()

    def execute_query(self, query, parameters=None):

        with self.driver.session() as session:

            result = session.run(query, parameters or {})

            return [record.data() for record in result]


graph = GraphDB()