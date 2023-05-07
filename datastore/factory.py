from datastore.providers.weaviate_datastore import WeaviateDataStore
from datastore.datastore import DataStore

async def get_datastore() -> DataStore:
    return WeaviateDataStore()
