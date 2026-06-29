from agents import create_critique_chain


def test_approves_minimal_draft_without_calling_llm():
    critique = create_critique_chain()
    result = critique({"main_task": "x", "draft": "too short", "revision_number": 0})
    assert "APPROVED" in result.upper()


def test_approves_after_max_revisions_without_calling_llm():
    critique = create_critique_chain()
    long_draft = "word " * 50
    result = critique({"main_task": "x", "draft": long_draft, "revision_number": 3})
    assert "APPROVED" in result.upper()
