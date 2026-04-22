from src.preprocessing import clean_text
from src.rules import rule_based_priority_boost


def classify_ticket(text, cat_pipe, pri_pipe, le_cat, le_pri):
    clean = clean_text(text)

    cat_pred = le_cat.inverse_transform(cat_pipe.predict([clean]))[0]
    pri_pred = le_pri.inverse_transform(pri_pipe.predict([clean]))[0]

    final_priority = rule_based_priority_boost(text, pri_pred)

    return {
        "category": cat_pred,
        "priority": final_priority,
        "ml_priority": pri_pred
    }