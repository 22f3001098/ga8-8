import pandas as pd

# Quarterly patient satisfaction scores
data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "Score": [-2.83, -0.02, 6.7, 2.85]
}

df = pd.DataFrame(data)

# Calculate statistics
average_score = df["Score"].mean()
industry_target = 4.5

print("Quarterly Data:\n", df)
print("\nAverage Score:", round(average_score, 2))
print("Industry Target:", industry_target)

# Check performance status
if average_score >= industry_target:
    print("\nStatus: Meeting or exceeding target.")
else:
    print("\nStatus: Below industry target. Improvement required.")
