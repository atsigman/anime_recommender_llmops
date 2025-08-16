from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq

from src.prompt_template import get_anime_prompt


class AnimeRecommender:
    def __init__(self, retriever, api_key: str, model_name: str) -> None:
        self.llm = ChatGroq(
            api_key=api_key,
            model_name=model_name,
            temperature=0
        )

        self.prompt = get_anime_prompt()

        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True
        )

    def get_recommendation(self, query: str) -> str:
        res = self.qa_chain({"query": query})
        return res["result"]