from neo4j import GraphDatabase

uri = "neo4j://localhost:7687"
username = "neo4j"
password = "123456789"
driver = GraphDatabase.driver(uri, auth=(username, password))

