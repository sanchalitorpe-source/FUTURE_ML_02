import random
import pandas as pd

random.seed(42)

TICKET_TEMPLATES = {
    "billing": {
        "high": [
            "I was charged twice for my subscription this month. Please refund immediately.",
            "Unauthorized charge of $299 on my credit card. This is fraud!",
            "My account was suspended despite paying on time. Urgent billing issue.",
            "Double billing issue - $150 charged twice, need immediate resolution.",
            "Payment failed but money deducted from my account. Emergency!",
        ],
        "medium": [
            "I need an invoice for my recent purchase for tax purposes.",
            "Can you explain the extra charge on my last bill?",
            "I want to upgrade my plan but the pricing page is confusing.",
            "How do I update my credit card on file? The form isn't working.",
            "My promo code didn't apply to the checkout. Need adjustment.",
        ],
        "low": [
            "Can I get a detailed breakdown of my monthly invoice?",
            "What payment methods do you accept?",
            "How does annual vs monthly billing work?",
            "Can I get a receipt for my last payment?",
            "Is there a student discount available?",
        ]
    },
    "technical": {
        "high": [
            "System is completely down! Production environment not responding.",
            "Critical data loss - database corrupted after latest update.",
            "Security vulnerability found - users can access other accounts.",
            "API returning 500 errors for all requests. Business halted.",
            "Login broken for all users since last deployment. URGENT.",
        ],
        "medium": [
            "The mobile app crashes when uploading files larger than 5MB.",
            "Integration with Salesforce stopped working after your update.",
            "Dashboard graphs not loading in Firefox browser.",
            "Export to CSV feature broken - file downloads as empty.",
            "Two-factor authentication emails not being received.",
        ],
        "low": [
            "Minor UI glitch - button slightly misaligned on settings page.",
            "Dark mode colors look off on the analytics dashboard.",
            "Can you add keyboard shortcut support for bulk actions?",
            "The tooltip text has a typo in the onboarding wizard.",
            "Search results take 3 seconds to load, could be faster.",
        ]
    },
    "account": {
        "high": [
            "Account hacked! Someone changed my password and email. Need recovery now.",
            "All my data is gone after account merge. Years of work lost!",
            "Account permanently locked - cannot access any data. Critical.",
            "Receiving threatening messages from another user. Safety concern.",
            "Identity theft suspected - strange login from another country.",
        ],
        "medium": [
            "Cannot reset my password - reset email never arrives.",
            "Team member cannot accept invitation to join organization.",
            "Need to transfer ownership of account to new admin.",
            "Profile photo won't upload - keeps showing error.",
            "Two accounts were accidentally merged. Need them separated.",
        ],
        "low": [
            "How do I change my display name in the profile settings?",
            "I want to add a bio to my account. Where is that option?",
            "Can I have two email addresses linked to one account?",
            "How do I set up my notification preferences?",
            "Is there a way to customize my profile theme?",
        ]
    },
    "shipping": {
        "high": [
            "Package marked delivered but nothing received. Order worth $500.",
            "Wrong item shipped for time-sensitive event tomorrow. Emergency.",
            "Package severely damaged - contents destroyed. Need replacement.",
            "Order missing for 3 weeks - complete silence from logistics.",
            "Perishable items arrived spoiled due to shipping delay.",
        ],
        "medium": [
            "Tracking number shows no movement for 5 days. Is it lost?",
            "I need to change delivery address before shipment goes out.",
            "Package stuck in customs for 2 weeks. Any help?",
            "Received only part of my order - 2 items missing.",
            "Shipping estimate was 3 days, now showing 2 weeks.",
        ],
        "low": [
            "Can I schedule a specific delivery time window?",
            "Do you ship to PO boxes?",
            "What carriers do you use for international shipping?",
            "How do I return an item I no longer need?",
            "Can I pick up my order from a local warehouse?",
        ]
    },
    "feature_request": {
        "high": [
            "Compliance requirement: need audit logs by next week or we lose contract.",
            "GDPR data export feature missing - legal deadline approaching.",
            "API rate limit blocking our enterprise integration. Deal-breaker.",
            "Need SSO/SAML support for enterprise client. Blocking purchase.",
            "Bulk import feature critical for migration. Blocking go-live.",
        ],
        "medium": [
            "Please add dark mode to the mobile application.",
            "Would love a way to export reports directly to Google Sheets.",
            "Can you add multi-language support for our global team?",
            "A Zapier integration would save us hours every week.",
            "Please add the ability to duplicate project templates.",
        ],
        "low": [
            "It would be nice to have more chart color options.",
            "Can you add a confetti animation when goals are completed?",
            "Would love to see more font choices in the editor.",
            "A weekly digest email would be a great addition.",
            "Can we get custom emoji reactions on comments?",
        ]
    },
    "refund": {
        "high": [
            "I was charged for a service I cancelled 3 months ago. $900 total. Need full refund.",
            "Defective product - returning entire order. Urgent refund required.",
            "Service never worked as advertised. Demanding immediate refund.",
            "Chargeback filed - willing to resolve if refunded today.",
            "Annual plan charged after I cancelled. $1200 unauthorized charge.",
        ],
        "medium": [
            "I accidentally purchased the wrong plan. Can I get a refund?",
            "Returned item 2 weeks ago but refund not processed yet.",
            "Partial refund request for unused portion of service.",
            "Duplicate order placed. Need refund for second order.",
            "Gift purchase went to wrong email. Need refund to reorder.",
        ],
        "low": [
            "What is your refund policy for digital products?",
            "How long does a refund take to appear on my card?",
            "Can I exchange instead of getting a refund?",
            "Is there a restocking fee for returns?",
            "I might want to return something. What's the process?",
        ]
    }
}


def generate_dataset(n_samples: int = 1200) -> pd.DataFrame:
    records = []
    categories = list(TICKET_TEMPLATES.keys())
    priorities = ["high", "medium", "low"]
    
    for _ in range(n_samples):
        cat = random.choice(categories)
        pri = random.choices(priorities, weights=[0.25, 0.45, 0.30])[0]
        templates = TICKET_TEMPLATES[cat][pri]
        text = random.choice(templates)
        
        prefixes = ["", "Hello, ", "Hi there, ", "Dear support, ", "URGENT: ",
                    "Hi, I need help - ", "Good day, ", "To whom it may concern, "]
        suffixes = ["", " Please help.", " Thank you.", " Appreciate your quick response.",
                    " This is very frustrating.", " Looking forward to your reply.",
                    " I hope this can be resolved quickly.", ""]
        
        text = random.choice(prefixes) + text + random.choice(suffixes)
        
        records.append({
            "ticket_id": f"TKT-{random.randint(10000, 99999)}",
            "text": text,
            "category": cat,
            "priority": pri,
        })
    
    return pd.DataFrame(records)