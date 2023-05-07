from typing import List, Tuple
from sentence_transformers import SentenceTransformer
import asyncio

model = SentenceTransformer('multi-qa-mpnet-base-dot-v1')

def get_embedding(sentence: str) -> Tuple[str, List[float]]:
    return (sentence, model.encode(sentence).tolist())

def get_embeddings(sentences: List[str]) -> List[List[float]]:
    result: List[List[float]] = [get_embedding(sentence)[1] for sentence in sentences]
    return result

async def get_embedding_array(sentences: List[str]) -> List[Tuple[str, List[float]]]:
    result: List[Tuple[str, List[float]]] = await asyncio.gather(*[get_embedding(sentence) for sentence in sentences])
    return result