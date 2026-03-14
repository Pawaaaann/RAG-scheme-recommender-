import json
import random

# Categories
categories = [
    "Agriculture", "Healthcare", "Education", "Women Empowerment",
    "MSME", "Startup", "Housing", "Skill Development",
    "Social Security", "Insurance", "Energy"
]

states = [
    "All", "Karnataka", "Tamil Nadu", "Maharashtra",
    "Delhi", "Uttar Pradesh", "Gujarat", "Rajasthan",
    "West Bengal", "Kerala"
]

occupations = [
    "Farmer", "Student", "Entrepreneur", "Street Vendor",
    "Unemployed Youth", "Woman", "Senior Citizen",
    "Startup Founder", "Small Business Owner"
]

def random_income():
    low = random.choice([100000, 200000, 300000, 500000])
    high = low + random.choice([200000, 300000, 500000])
    return low, high

schemes = []

for i in range(1, 221):   # Generates 220 schemes
    
    category = random.choice(categories)
    state = random.choice(states)
    occupation = random.choice(occupations)
    income_min, income_max = random_income()
    min_age = random.choice([18, 21, 25, 30])
    max_age = random.choice([40, 45, 50, 60])

    scheme = {
        "scheme_id": f"SCH{i:03}",
        "scheme_name": f"{category} Development Scheme {i}",
        "state": state,
        "category": category,
        "eligibility": f"{occupation} aged {min_age}-{max_age} with income between ₹{income_min} and ₹{income_max}.",
        "min_age": min_age,
        "max_age": max_age,
        "income_min": income_min,
        "income_max": income_max,
        "target_occupation": occupation,
        "benefits": f"Financial assistance up to ₹{random.randint(50000, 500000)}.",
        "documents_required": [
            "Aadhaar Card",
            "Income Certificate",
            "Bank Account Details"
        ],
        "application_link": f"https://gov.example/scheme/{i}"
    }

    schemes.append(scheme)

# Save file
with open("data/schemes_220.json", "w", encoding="utf-8") as f:
    json.dump(schemes, f, indent=2, ensure_ascii=False)

print("✅ 220 schemes generated successfully!")