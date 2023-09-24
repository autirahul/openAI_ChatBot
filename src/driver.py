from neo4j import GraphDatabase

host = 'bolt://localhost:7687'
user = 'neo4j'
password = 'neo4j'
driver = GraphDatabase.driver(host, auth=(user, password))


def read_query(query, params={}):
        with driver.session() as session:
            try:
                result = session.run(query, params)
                response = [r.values()[0] for r in result]
                if response == []:
                        return "Either there is no result found for your question Or please help me with additional context."
                return response
            except Exception as inst:
                if "MATCH" in query:
                    return "Either there is no result found for your question Or please help me with additional context!"
                else:
                    return query
    
