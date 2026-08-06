from neo4j import GraphDatabase
from config import Config

driver = GraphDatabase.driver(
    Config.NEO4J_URI,
    auth=(Config.NEO4J_USERNAME, Config.NEO4J_PASSWORD)
)

try:
    driver.verify_connectivity()
    print("✅ Connected to CognoDB successfully!")
except Exception as e:
    print("❌ Connection failed:", e)
finally:
    driver.close()