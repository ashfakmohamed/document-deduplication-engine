from document_deduplication_engine import find_duplicates, jaccard_similarity


def test_detects_near_duplicate_documents():
    matches = find_duplicates(
        {"a": "alpha beta gamma delta", "b": "alpha beta gamma delta", "c": "unrelated text"}
    )
    assert [(item.left_id, item.right_id) for item in matches] == [("a", "b")]


def test_empty_sets_are_equivalent():
    assert jaccard_similarity(set(), set()) == 1.0
