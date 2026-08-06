import os
import sys

# Add the project root directory to Python's import path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from neo4j import GraphDatabase
from config import Config


class Seeder:

    def __init__(self):
        self.driver = GraphDatabase.driver(
            Config.NEO4J_URI,
            auth=(Config.NEO4J_USERNAME, Config.NEO4J_PASSWORD)
        )

    def close(self):
        self.driver.close()

    def seed_database(self):

        with self.driver.session() as session:

            # Delete old data (Optional)
            session.run("""
                MATCH (n)
                DETACH DELETE n
            """)

            # ----------------------------
            # Create Movies
            # ----------------------------
            session.run("""

            CREATE (:Movie {
                movieId:101,
                title:'Avatar',
                year:2009,
                genre:'Action'
            })

            CREATE (:Movie {
                movieId:102,
                title:'Inception',
                year:2010,
                genre:'Sci-Fi'
            })

            CREATE (:Movie {
                movieId:103,
                title:'Titanic',
                year:1997,
                genre:'Romance'
            })

            CREATE (:Movie {
                movieId:104,
                title:'Interstellar',
                year:2014,
                genre:'Sci-Fi'
            })

            CREATE (:Movie {
                movieId:105,
                title:'The Dark Knight',
                year:2008,
                genre:'Action'
            })

            """)

            # ----------------------------
            # Create Users
            # ----------------------------
            session.run("""

            CREATE (:User {
                userId:1,
                name:'John'
            })

            CREATE (:User {
                userId:2,
                name:'Alice'
            })

            CREATE (:User {
                userId:3,
                name:'David'
            })

            """)

            # ----------------------------
            # WATCHED Relationships
            # ----------------------------
            session.run("""

            MATCH (u:User {userId:1}),
                  (m:Movie {movieId:101})
            CREATE (u)-[:WATCHED]->(m)

            MATCH (u:User {userId:1}),
                  (m:Movie {movieId:102})
            CREATE (u)-[:WATCHED]->(m)

            MATCH (u:User {userId:2}),
                  (m:Movie {movieId:101})
            CREATE (u)-[:WATCHED]->(m)

            MATCH (u:User {userId:2}),
                  (m:Movie {movieId:103})
            CREATE (u)-[:WATCHED]->(m)

            MATCH (u:User {userId:3}),
                  (m:Movie {movieId:102})
            CREATE (u)-[:WATCHED]->(m)

            MATCH (u:User {userId:3}),
                  (m:Movie {movieId:104})
            CREATE (u)-[:WATCHED]->(m)

            """)

            # ----------------------------
            # RATED Relationships
            # ----------------------------
            session.run("""

            MATCH (u:User {userId:1}),
                  (m:Movie {movieId:101})
            CREATE (u)-[:RATED {rating:5}]->(m)

            MATCH (u:User {userId:1}),
                  (m:Movie {movieId:102})
            CREATE (u)-[:RATED {rating:4}]->(m)

            MATCH (u:User {userId:2}),
                  (m:Movie {movieId:103})
            CREATE (u)-[:RATED {rating:5}]->(m)

            MATCH (u:User {userId:3}),
                  (m:Movie {movieId:104})
            CREATE (u)-[:RATED {rating:5}]->(m)

            """)

            print("✅ Database Seeded Successfully!")


if __name__ == "__main__":

    seeder = Seeder()

    seeder.seed_database()

    seeder.close()