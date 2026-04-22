HIGH_KEYWORDS = {
    'urgent', 'critical', 'emergency', 'asap', 'immediately', 'hack',
    'breach', 'down', 'broken', 'crash', 'fraud', 'stolen', 'lost',
    'legal', 'lawsuit', 'compliance', 'data loss', 'security', 'unauthorized'
}

LOW_KEYWORDS = {
    'question', 'wondering', 'curious', 'would love', 'nice', 'could',
    'suggestion', 'idea', 'someday', 'eventually', 'might', 'maybe'
}


def rule_based_priority_boost(text: str, ml_priority: str) -> str:
    lower = text.lower()
    word_set = set(lower.split())
    
    if any(k in lower for k in HIGH_KEYWORDS):
        if ml_priority == 'low':
            return 'medium'
        return 'high'
    
    if any(k in word_set for k in LOW_KEYWORDS):
        if ml_priority == 'high':
            return 'medium'
    
    return ml_priority