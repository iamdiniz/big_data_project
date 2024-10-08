from neo4j import GraphDatabase

uri = "neo4j://localhost:7687"
username = "neo4j"
password = "123456789"
driver = GraphDatabase.driver(uri, auth=(username, password))

# def create(tx, name): # tx é uma transação em Cypher, que é a linguagem de consulta do neo4j
#     tx.run("CREATE (n:Person {name: $name})", name=name)

# with driver.session() as session: # abrir uma sessão para executar a operação create.
#     session.write_transaction(create, "Darlan") # session representa a conexão

def get_person(tx, name):
    result = tx.run("MATCH (n:Person {name: $name}) RETURN n.name AS name", name=name)
    return [record["name"] for record in result]

with driver.session() as session:
    names = session.read_transaction(get_person, "Guilherme")
    print(names)

def update_person(tx, old_name, new_name):
    tx.run("MATCH (n:Person {name: $old_name}) "
           "SET n.name = $new_name", old_name=old_name, new_name=new_name)

with driver.session() as session:
    session.write_transaction(update_person, "Guilherme", "Diniz")
    print("Nome atualizado!")

# def delete_person(tx, name):
#     tx.run("MATCH (n:Person {name: $name}) "
#            "DELETE n", name=name)

# with driver.session() as session:
#     session.write_transaction(delete_person, "Diniz")
#     print("Pessoa deletada!")

# def create_friendship(tx, person1_name, person2_name):
#     tx.run("MATCH (a:Person {name: $person1_name}), (b:Person {name: $person2_name}) "
#            "CREATE (a)-[:AMIGO_DE]->(b)", person1_name=person1_name, person2_name=person2_name)

# with driver.session() as session:
#     session.write_transaction(create_friendship, "Darlan", "Eduarda")
#     print("Relacionamento AMIGO_DE criado!")