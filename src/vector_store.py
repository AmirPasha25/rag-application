from data_ingestion import DataIngestion
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

class VectorStoreFAISS:
    def __init__(self, doc):
        # creating faiss index
        self.model = SentenceTransformer("BAAI/bge-m3")
        data_ingest = DataIngestion(doc)
        
        self.embeddings, self.metadata = data_ingest.data_embedding()
        embed_dim = self.embeddings.shape[1]
        self.index = faiss.IndexFlatIP(embed_dim)
        self.index.add(self.embeddings)

    def similarity_search(self, user_query, top_k = 2):
        query_embed = self.model.encode([user_query])
        arr = np.array(query_embed, dtype= "float32")
        faiss.normalize_L2(arr)
        scores, indexes = self.index.search(arr, top_k)
        final_match_list = []
        for idx, score in zip(indexes[0], scores[0]):
            final_match_list.append({
                "id": self.metadata[idx]["id"],
                "text": self.metadata[idx]["text"],
                "score": float(score)
            })
        
        final_text = ""
        for item in final_match_list:
            final_text = item["text"]
        
        return final_text
    
