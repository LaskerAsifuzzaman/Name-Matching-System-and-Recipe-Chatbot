from rapidfuzz import process, fuzz
from .data import NAMES

def find_similar_names(query: str, top_k: int = 5):
    results = process.extract(
        query,
        NAMES,
        scorer=fuzz.WRatio,
        limit=top_k
    )

    best_match = results[0]

    return {
        "input": query,
        "best_match": {
            "name": best_match[0],
            "score": best_match[1]
        },
        "other_matches": [
            {"name": name, "score": score}
            for name, score, _ in results[1:]
        ]
    }
