"""Near-duplicate document detection."""

from .core import DuplicatePair, find_duplicates, jaccard_similarity, shingles

__all__ = ["DuplicatePair", "find_duplicates", "jaccard_similarity", "shingles"]
