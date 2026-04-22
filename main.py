import json
from src.data_generation import generate_dataset
from src.model import train_and_evaluate
from src.inference import classify_ticket

print("=" * 60)
print("SUPPORT TICKET CLASSIFICATION SYSTEM")
print("=" * 60)

df = generate_dataset(1200)

cat_pipe, pri_pipe, le_cat, le_pri, metrics = train_and_evaluate(df)

demo_tickets = [
    "URGENT: system down",
    "charged twice refund please",
    "add dark mode feature",
]

results = []
for t in demo_tickets:
    r = classify_ticket(t, cat_pipe, pri_pipe, le_cat, le_pri)
    r["text"] = t
    results.append(r)

with open("data/outputs/classifier_results.json", "w") as f:
    json.dump(results, f, indent=2)

print("Done.")