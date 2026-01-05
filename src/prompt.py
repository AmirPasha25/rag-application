rag_prompt = ''' 
Your task is to take the RAG pipeline’s retrieved text and rewrite it into a clear, standard, and well-structured response. You will be given:
	1.	the user’s question,
	2.	the RAG pipeline’s retrieved answer, and
	3.	this prompt.

Using only the retrieved answer, rephrase the content in clear, human-understandable language. Do not add, remove, or infer any information beyond what is present in the retrieved text. The length of the output should be approximately the same as the retrieved answer.
'''