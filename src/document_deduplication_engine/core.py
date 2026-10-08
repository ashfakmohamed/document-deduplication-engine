import re
from dataclasses import dataclass
from itertools import combinations


@dataclass(frozen=True)
class DuplicatePair:
    left_id: str
    right_id: str
    similarity: float


def shingles(text: str, size: int = 3) -> set[str]:
    if size < 1:
        raise ValueError("shingle size must be positive")
    words = re.findall(r"[a-z0-9]+", text.casefold())
    if not words:
        return set()
    if len(words) < size:
        return {" ".join(words)}
    return {" ".join(words[index : index + size]) for index in range(len(words) - size + 1)}


def jaccard_similarity(left: set[str], right: set[str]) -> float:
    union = left | right
    return len(left & right) / len(union) if union else 1.0


def find_duplicates(
    documents: dict[str, str], threshold: float = 0.8, shingle_size: int = 3
) -> list[DuplicatePair]:
    if not 0 <= threshold <= 1:
        raise ValueError("threshold must be between zero and one")
    signatures = {key: shingles(text, shingle_size) for key, text in documents.items()}
    matches: list[DuplicatePair] = []
    for left_id, right_id in combinations(sorted(documents), 2):
        score = jaccard_similarity(signatures[left_id], signatures[right_id])
        if score >= threshold:
            matches.append(DuplicatePair(left_id, right_id, round(score, 4)))
    return matches
