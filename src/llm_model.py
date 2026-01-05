# -----Using OpenAI from Langchain------
from vector_store import VectorStoreFAISS
from langchain_openai import ChatOpenAI
from langchain.messages import SystemMessage, HumanMessage
from prompt import rag_prompt
from dotenv import load_dotenv
import os


class OpenAIModel:
    def __init__(self, document, user_input, openai_model = "gpt-5-nano", openai_temperature = 0.2):
        self.user_input = user_input
        result = VectorStoreFAISS(document)
        self.rag_retrived_content = result.similarity_search(self.user_input)
        load_dotenv()
        key = os.getenv("OPENAI_API_KEY")
        self.llm = ChatOpenAI(model = openai_model,
               temperature= openai_temperature,
               api_key=key) 
        
    def processing(self):
        message = [SystemMessage(content=rag_prompt),
                   HumanMessage(content=self.rag_retrived_content),
                   HumanMessage(content=self.user_input)]
        result = self.llm.invoke(message)
        return result.content
        
key = OpenAIModel()
print(key.processing())

