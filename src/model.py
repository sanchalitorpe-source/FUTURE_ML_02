from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report, accuracy_score, f1_score
from sklearn.preprocessing import LabelEncoder

from src.preprocessing import clean_text


def build_pipeline(clf):
    return Pipeline([
        ('tfidf', TfidfVectorizer(ngram_range=(1,2), max_features=10000, sublinear_tf=True, min_df=2)),
        ('clf', clf)
    ])


def train_and_evaluate(df):
    df['clean_text'] = df['text'].apply(clean_text)

    X = df['clean_text']
    y_cat = df['category']
    y_pri = df['priority']

    le_cat = LabelEncoder()
    le_pri = LabelEncoder()

    y_cat_enc = le_cat.fit_transform(y_cat)
    y_pri_enc = le_pri.fit_transform(y_pri)

    X_train, X_test, yc_train, yc_test, yp_train, yp_test = train_test_split(
        X, y_cat_enc, y_pri_enc, test_size=0.2, random_state=42, stratify=y_cat_enc
    )

    cat_pipe = build_pipeline(LogisticRegression(C=5.0, max_iter=1000, random_state=42, class_weight='balanced'))
    pri_pipe = build_pipeline(LinearSVC(C=1.0, max_iter=2000, random_state=42, class_weight='balanced'))

    cat_pipe.fit(X_train, yc_train)
    pri_pipe.fit(X_train, yp_train)

    yc_pred = cat_pipe.predict(X_test)
    yp_pred = pri_pipe.predict(X_test)

    metrics = {
        "category": {
            "accuracy": round(accuracy_score(yc_test, yc_pred)*100,2),
            "f1_weighted": round(f1_score(yc_test, yc_pred, average='weighted')*100,2),
        },
        "priority": {
            "accuracy": round(accuracy_score(yp_test, yp_pred)*100,2),
            "f1_weighted": round(f1_score(yp_test, yp_pred, average='weighted')*100,2),
        }
    }

    return cat_pipe, pri_pipe, le_cat, le_pri, metrics