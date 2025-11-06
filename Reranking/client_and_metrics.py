# File: gemini_client.py

import dotenv
import os
from smolagents import OpenAIServerModel
import pandas as pd
import numpy as np
import time

class GeminiClient:

    def __init__(self, model_id: str = "gemini-2.5-flash"):
        dotenv.load_dotenv()
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise Exception("GEMINI_API_KEY needs to be set in .env.")
        
        self.model_id = model_id
        self.model = OpenAIServerModel(
            model_id=self.model_id,
            api_base="https://generativelanguage.googleapis.com/v1beta/openai/",
            api_key=self.api_key,
            timeout = 20.0
        )

    def generate_answer(self, prompt: str) -> str:
        messages = [{
            "role": "user", 
            "content": prompt  
        }]
        
        try:
            answer = self.model.generate(messages=messages)
            return answer.content
        except Exception as e:
            print(f"Error during model generation: {e}")
            return None

class MetricHelpers:

    @staticmethod
    def precision_at_k(labels, k):
        """labels: list/array of 0/1 relevance sorted by baseline rank"""
        topk = labels[:k]
        return np.sum(topk) / len(topk)

    @staticmethod
    def recall_at_k(labels, k):
        """Recall = retrieved relevant / total relevant"""
        total_relevant = np.sum(labels)
        if total_relevant == 0:
            return np.nan  # undefined
        topk = labels[:k]
        return np.sum(topk) / total_relevant

    @staticmethod
    def ndcg_at_k(labels, k):
        """Compute nDCG@k with binary relevance (0/1)."""
        labels = np.array(labels)
        k = min(k, len(labels))
        gains = (2 ** labels[:k] - 1)
        discounts = 1 / np.log2(np.arange(2, k + 2))
        dcg = np.sum(gains * discounts)

        # Ideal DCG: sorted by true relevance
        ideal = np.sort(labels)[::-1]
        ideal_gains = (2 ** ideal[:k] - 1)
        idcg = np.sum(ideal_gains * discounts)
        return 0.0 if idcg == 0 else dcg / idcg




# if __name__ == "__main__":
#     try:
#         client = GeminiClient() 
        
#         prompt = "Which is warmer? Blue or red?"
#         print(f"Sending prompt: '{prompt}'")
        
#         answer_content = client.generate_answer(prompt)
        
#         if answer_content:
#             print(f"\nModel returned answer: {answer_content}")

#     except Exception as e:
#         print(f"An error occurred: {e}")