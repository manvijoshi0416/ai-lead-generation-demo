import pandas as pd

def role_score(role):
    return {
        "Senior": 30,
        "Mid": 20,
        "Junior": 5
    }.get(role, 0)

def scientific_score(pub, recency):
    if pub == "Yes" and recency == "Last 2 Years":
        return 40
    elif pub == "Yes":
        return 25
    return 0

def funding_score(stage):
    return {
        "Series A": 20,
        "Series B": 20,
        "Public": 15,
        "Private": 5,
        "Non-funded": 0
    }.get(stage, 0)

def location_score(hub):
    return 10 if hub == "Yes" else 0

df = pd.read_csv("leads_dataset.csv")
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")


df["propensity_score"] = (
    df["role_seniority"].apply(role_score) +
    df.apply(lambda x: scientific_score(x["relevant_publication"], x["publication_recency"]), axis=1) +
    df["company_funding_stage"].apply(funding_score) +
    df["biotech_hub_location"].apply(location_score)
)

df = df.sort_values(by="propensity_score", ascending=False)
df["rank"] = range(1, len(df) + 1)

def priority(score):
    if score >= 75:
        return "High"
    elif score >= 40:
        return "Medium"
    return "Low"

df["lead_priority"] = df["propensity_score"].apply(priority)

df.to_csv("ranked_leads.csv", index=False)
print("Ranked leads saved to ranked_leads.csv")
