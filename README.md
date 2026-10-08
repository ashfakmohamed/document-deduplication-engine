# Document Deduplication Engine

An explainable near-duplicate detector using normalized word shingles and Jaccard similarity.

## Highlights

- Configurable shingle size and match threshold
- Stable pair ordering and explicit similarity scores
- Useful for ingestion pipelines and knowledge-base cleanup
- Dependency-free implementation with tests and CI

```python
from document_deduplication_engine import find_duplicates

matches = find_duplicates(documents, threshold=0.85)
```

For very large corpora, combine this approach with MinHash or locality-sensitive hashing.

No license has been selected; all rights are reserved.
