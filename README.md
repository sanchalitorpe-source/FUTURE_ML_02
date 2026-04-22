# 🎫 Support Ticket Classification System

A machine learning-based system that automatically classifies support tickets into **categories** and assigns **priority levels** using NLP techniques.

---

## 🚀 Features

* 🧠 **Text Preprocessing**

  * Lowercasing, cleaning, stopword removal
  * Lightweight stemming (no external NLP libraries)

* 📂 **Ticket Classification**

  * Categories: billing, technical, account, shipping, feature_request, refund

* ⚡ **Priority Prediction**

  * Levels: high, medium, low

* 🔀 **Hybrid Intelligence**

  * Machine Learning (TF-IDF + models)
  * Rule-based priority boosting

* 📊 **Model Evaluation**

  * Accuracy, F1-score
  * Cross-validation

* 🧪 **Synthetic Dataset Generation**

  * Realistic support ticket simulation

---

## 🛠️ Tech Stack

* Python
* NumPy
* Pandas
* Scikit-learn

---

## 📁 Project Structure

```
support-ticket-classifier/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── outputs/
│       └── classifier_results.json
│
├── models/
│
├── src/
│   ├── data_generation.py
│   ├── preprocessing.py
│   ├── rules.py
│   ├── model.py
│   └── inference.py
│
├── tests/
├── config/
├── app/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

1. Clone the repository:

```
git clone https://github.com/your-username/ticket-classifier.git
cd ticket-classifier
```

2. Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```
python main.py
```

---

## 📤 Output

Results are saved in:

```
data/outputs/classifier_results.json
```

Example output:

```json
{
  "category": "technical",
  "priority": "high",
  "ml_priority": "high",
  "text": "URGENT: system down"
}
```

---

## 🧪 Example Use Cases

* Customer support automation
* Ticket triaging systems
* Helpdesk prioritization
* Chatbot backend logic

---

## 📈 Model Details

| Task     | Model Used                   |
| -------- | ---------------------------- |
| Category | Logistic Regression + TF-IDF |
| Priority | LinearSVC + TF-IDF           |

---

## 🔮 Future Improvements

* Replace TF-IDF with embeddings (BERT / Sentence Transformers)
* Add Streamlit UI
* Deploy as API (FastAPI)
* Real-world dataset integration
* Model persistence (save/load)

---

## 🤝 Contributing

Feel free to fork the repo and improve the system!

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👤 Author

Developed by *Your Name*

---

⭐ If you found this project useful, give it a star!
