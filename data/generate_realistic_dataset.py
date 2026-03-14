import json
import random

# -------------------------
# Categories
# -------------------------

categories = {
    "Education": [
        ("National Scholarship Scheme", "nsp"),
        ("Higher Education Support Scheme", "hes"),
        ("Digital Learning Grant", "dlg"),
        ("Student Financial Aid Program", "sfap"),
    ],
    "Agriculture": [
        ("Farmer Income Support Scheme", "fiss"),
        ("Crop Insurance Program", "cip"),
        ("Organic Farming Promotion Scheme", "ofps"),
        ("Agriculture Equipment Subsidy", "aes"),
    ],
    "Startup": [
        ("Startup India Seed Fund", "sisf"),
        ("Young Innovators Grant", "yig"),
        ("Technology Startup Support Scheme", "tsss"),
    ],
    "Women Empowerment": [
        ("Women Entrepreneurship Scheme", "wes"),
        ("Self Help Group Financial Support", "shgfs"),
        ("Women Skill Development Program", "wsdp"),
    ],
    "MSME": [
        ("Small Business Growth Scheme", "sbgs"),
        ("MSME Credit Support Program", "mcsp"),
        ("Micro Enterprise Development Scheme", "meds"),
    ],
    "Healthcare": [
        ("Rural Health Assistance Scheme", "rhas"),
        ("Healthcare Insurance Support", "his"),
    ],
    "Skill Development": [
        ("Skill India Training Program", "sitp"),
        ("Youth Employment Skill Program", "yesp"),
    ],
}

# -------------------------
# Other Data
# -------------------------

occupations = [
    "Student",
    "Farmer",
    "Entrepreneur",
    "Unemployed Youth",
    "Small Business Owner",
    "Woman Entrepreneur",
]

states = [
    "Tamil Nadu",
    "Karnataka",
    "Kerala",
    "Maharashtra",
    "Delhi",
    "Gujarat",
    "Punjab",
    "Uttar Pradesh",
]

documents_required = [
    "Aadhaar Card",
    "Income Certificate",
    "Bank Account Details",
    "Residence Proof",
    "Passport Size Photo",
]

schemes = []

# -------------------------
# Generate 500 Schemes
# -------------------------

for i in range(1, 1001):

    category = random.choice(list(categories.keys()))
    scheme_name, slug = random.choice(categories[category])

    min_age = random.choice([18, 21])
    max_age = random.choice([35, 40, 50, 60])

    income_min = random.choice([0, 50000, 100000])
    income_max = random.choice([300000, 500000, 800000])

    scheme = {
        "scheme_id": i,

        "scheme_name": f"{scheme_name} {i}",

        "category": category,

        "state": random.choice(states),

        "min_age": min_age,
        "max_age": max_age,

        "income_min": income_min,
        "income_max": income_max,

        "target_occupation": random.choice(occupations),

        "eligibility": f"{random.choice(occupations)} aged {min_age}-{max_age} with income between {income_min} and {income_max}",

        "benefits": f"Financial assistance up to ₹{random.randint(50000,500000)}",

        "documents_required": random.sample(documents_required, 3),

        # Realistic application link structure
        "application_link": f"https://www.myscheme.gov.in/schemes/{slug}-{i}"
    }

    schemes.append(scheme)

# -------------------------
# Save Dataset
# -------------------------

with open("schemes_500.json", "w", encoding="utf-8") as f:
    json.dump(schemes, f, indent=4)

print("✅ 500 realistic schemes generated successfully!")