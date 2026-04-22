import re

STOPWORDS = {
    'i','me','my','myself','we','our','ours','ourselves','you','your','yours',
    'yourself','he','him','his','himself','she','her','hers','herself','it',
    'its','itself','they','them','their','theirs','themselves','what','which',
    'who','whom','this','that','these','those','am','is','are','was','were',
    'be','been','being','have','has','had','having','do','does','did','doing',
    'a','an','the','and','but','if','or','because','as','until','while','of',
    'at','by','for','with','about','against','between','into','through',
    'during','before','after','above','below','to','from','up','down','in',
    'out','on','off','over','under','again','further','then','once','here',
    'there','when','where','why','how','all','both','each','few','more','most',
    'other','some','such','no','nor','not','only','own','same','so','than',
    'too','very','s','t','can','will','just','don','should','now','d','ll',
    'm','o','re','ve','y','ain','aren','couldn','didn','doesn','hadn','hasn',
    'haven','isn','ma','mightn','mustn','needn','shan','shouldn','wasn',
    'weren','won','wouldn','also','get','got','getting','please','hi','hello',
    'hey','dear','thanks','thank','regards','sincerely','truly'
} # keep exactly same (copy from your code)

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^a-z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    
    tokens = [w for w in text.split() if w not in STOPWORDS and len(w) > 2]
    
    stemmed = []
    for w in tokens:
        for suffix in ('ing','tion','ed','er','est','ly','ness','ment'):
            if w.endswith(suffix) and len(w) - len(suffix) > 2:
                w = w[:-len(suffix)]
                break
        stemmed.append(w)
    
    return ' '.join(stemmed)