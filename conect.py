from pymilvus import connections

def connect_to_milvus(alias, host, port):
    try:
        connections.connect(
            alias=alias,
            user='username',
            password='password',
            host=host,
            port=port
        )
        print(f"Connected to Milvus at {host}:{port} with alias '{alias}'")
    except Exception as e:
        print(f"Failed to connect to Milvus at {host}:{port} with alias '{alias}': {str(e)}")

# Colling the function to connect to the milvus server
connect_to_milvus("default", "localhost", "19530")