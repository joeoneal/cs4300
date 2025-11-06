import pandas as pd
import numpy as np
from client_and_metrics import GeminiClient, MetricHelpers
import time

# ----------------- data loading ------------------------- #
df = pd.read_csv("rag_sample_queries_candidates.csv")
df.sort_values(["query_id", "baseline_rank"], inplace=True)
# -------------------------------------------------------- #

# ------------------------- llm querying logic --------------------------------- #
def query_llm(df: pd.DataFrame, query: str):
    client = GeminiClient()
    llm_column = 'llm_score'
    df[llm_column] = pd.NA
    max_retries = 3

    for index, row in df.iterrows():
        query_text = row['query_text']
        candidate_text = row['candidate_text']
        item = (f"Query: {query_text}\nCandidate: {candidate_text}")
        retries = 0
        llm_score = pd.NA
        while retries <= max_retries:
            try:
                llm_score = client.generate_answer(f'{query}\n{item}')
                print(llm_score)
                break
            except Exception as e:
                retries +=1
                
                if retries >= max_retries:
                    print(f"Error: max retries reached for index {index}. Skipping. Error: {e}")
                    break
                sleep_time = 2**retries
                print(f"Rate limit or API error detected. Retrying in {sleep_time:.2f} seconds... (Attempt {retries}/{max_retries})")
                time.sleep(sleep_time)

        df.loc[index, llm_column] = llm_score

    return df 
# ------------------------------------------------------------------------ #

        
# --------------------- query --------------------------------------------------- #
query2 = ''' 
You are a search relevance evaluator. Your task is to rate the relevance of a candidate passage to a user's query on a scale from 0 to 5.

**Relevance Scale:**
A score of 5 means that the passage is a direct, comprehensive, and correct answer to the query.
A score of 0 means that the passage is completely off-topic, incorrect, or nonsensical.
The other three scores are a gradient between them. 

**Example:**
Query: What is the capital of France?
Candidate: Paris is the capital and most populous city of France.
Rating: 5

Please respond with a single integer rating only.

**Your Task:**
'''

query1 = ''' 
You are a search relevance evaluator. Your task is to rate the relevance of a candidate passage to a user's query on a scale from 0 to 5.

**Relevance Scale:**
5: The passage is a direct, comprehensive, and correct answer to the query.
4: The passage is a correct and direct answer, but may be incomplete.
3: The passage does not directly answer the query, but describes a core component or a closely related concept.
2: The passage is on-topic, but is not useful for answering the query.
1: The passage is only tangentially related to the query's topic.
0: The passage is completely off-topic, incorrect, or nonsensical.

**Example:**
Query: What is the capital of France?
Candidate: Paris is the capital and most populous city of France.
Rating: 5

Please respond with a single integer rating only.

**Your Task:**
'''
# ------------------------------------------------------------------------------- #

# ----------------- new df with ai scores, reranked ---------------------- #
df = query_llm(df, query1)
reranked = df.sort_values(["query_id", "llm_score"], ascending=[True, False])
# ------------------------------------------------------------------------ #

# ----------------- print new metrics ---------------------- #

llm_results = []
K = 3

for qid, group in reranked.groupby("query_id"):
    labels = group["gold_label"].tolist()
    p = MetricHelpers.precision_at_k(labels, K)
    r = MetricHelpers.recall_at_k(labels, K)
    n = MetricHelpers.ndcg_at_k(labels, K)
    llm_results.append({"query_id": qid, f"precision@{K}": p, f"recall@{K}": r, f"nDCG@{K}": n})

llm_metrics = pd.DataFrame(llm_results)


print("\n-----------------------------------------------------")
print("LLM Reranked Metrics:")
print(llm_metrics.round(3))
print("\nAverage llm metrics:")
print(llm_metrics[[f"precision@{K}", f"recall@{K}", f"nDCG@{K}"]].mean().round(3))
# --------------------------------------------------------- #

# ---------------------------- export ----------------------------- #
reranked['llm_rank'] = reranked.groupby('query_id').cumcount() + 1
output_df = reranked[['query_id', 'candidate_id', 'llm_score', 'llm_rank']]
output_df.to_csv("results.csv", index=False)

print("\n--- Export Summary ---")
print("Successfully exported the following data to results.csv:")
# ---------------------------------------------------------------- #