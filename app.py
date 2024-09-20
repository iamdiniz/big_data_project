from neo4j import GraphDatabase

uri = "neo4j://localhost:7687"
username = "neo4j"
password = "123456789"
driver = GraphDatabase.driver(uri, auth=(username, password))

def create(tx, name): # tx é uma transação em Cypher, que é a linguagem de consulta do neo4j
    tx.run("CREATE (n:Person {name: $name})", name=name)

with driver.session() as session: # abrir uma sessão para executar a operação create.
    session.write_transaction(create, "Guilherme") # session representa a conexão