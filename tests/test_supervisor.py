from agents import create_supervisor_chain


def test_routes_to_researcher_when_no_research():
    supervisor = create_supervisor_chain()
    decision = supervisor({"main_task": "AI safety trends"})
    assert decision["next_step"] == "researcher"


def test_routes_to_writer_when_research_but_no_draft():
    supervisor = create_supervisor_chain()
    decision = supervisor({
        "main_task": "AI safety trends",
        "research_findings": ["some findings"],
        "draft": "",
    })
    assert decision["next_step"] == "writer"


def test_routes_to_writer_for_revision_when_critique_pending():
    supervisor = create_supervisor_chain()
    decision = supervisor({
        "main_task": "AI safety trends",
        "research_findings": ["some findings"],
        "draft": "a draft",
        "critique_notes": "Needs more evidence.",
        "revision_number": 1,
    })
    assert decision["next_step"] == "writer"


def test_ends_when_critique_approved():
    supervisor = create_supervisor_chain()
    decision = supervisor({
        "main_task": "AI safety trends",
        "research_findings": ["some findings"],
        "draft": "a draft",
        "critique_notes": "APPROVED - looks great",
    })
    assert decision["next_step"] == "END"


def test_ends_after_max_revisions():
    supervisor = create_supervisor_chain()
    decision = supervisor({
        "main_task": "AI safety trends",
        "research_findings": ["some findings"],
        "draft": "a draft",
        "critique_notes": "Still needs work.",
        "revision_number": 3,
    })
    assert decision["next_step"] == "END"
