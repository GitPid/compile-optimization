from langchain_community.embeddings import OllamaEmbeddings 

embeddings= OllamaEmbeddings(
    model="nomic-embed-text:v1.5",
    base_url="http://localhost:11434"  # Ollama 服务的默认地址
)

# 单个文本转向量
query = "我喜欢你"
query_vector = embeddings.embed_query(query)
print(f"Query 向量维度: {len(query_vector)}")
print(f"Query 向量前10维: {query_vector[:10]}\n")

# 批量文本转向量
documents = ["我喜欢你", "我稀饭你", "晚上吃啥"]
doc_vectors = embeddings.embed_documents(documents)

for i, vec in enumerate(doc_vectors):
    print(f"文档 {i+1} 向量维度: {len(vec)}")
    print(f"文档 {i+1} 向量前10维: {vec[:10]}\n")

