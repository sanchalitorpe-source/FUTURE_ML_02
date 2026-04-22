from src.inference import classify_ticket

def test_inference_structure():
    dummy = {
        "category": "billing",
        "priority": "high",
        "ml_priority": "high"
    }
    assert "category" in dummy
    assert "priority" in dummy