from neo4j import GraphDatabase


uri = "neo4j://127.0.0.1:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "12345678"))

driver.close()  # close the driver object