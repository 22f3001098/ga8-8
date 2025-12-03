"""
Healthcare Performance Analysis
Patient Satisfaction Score Analysis - 2024 Quarterly Data
Analyst: 22f3001098@ds.study.iitm.ac.in
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Quarterly Data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
satisfaction_scores = [-2.83, -0.02, 6.7, 2.85]

# Create DataFrame
df = pd.DataFrame({
    'Quarter': quarters,
    'Satisfaction_Score': satisfaction_scores
})

# Calculate metrics
average_score = np.mean(satisfaction_scores)
industry_target = 4.5
gap_to_target = industry_target - average_score

print("=" * 60)
print("HEALTHCARE PERFORMANCE ANALYSIS - 2024")
print("=" * 60)
print(f"\nQuarterly Patient Satisfaction Scores:")
print(df.to_string(index=False))
print(f"\nAverage Satisfaction Score: {average_score:.2f}")
print(f"Industry Target: {industry_target}")
print(f"Gap to Target: {gap_to_target:.2f}")
print(f"Performance vs Target: {(average_score/industry_target)*100:.1f}%")

# Statistical Analysis
print("\n" + "=" * 60)
print("STATISTICAL INSIGHTS")
print("=" * 60)
print(f"Standard Deviation: {np.std(satisfaction_scores):.2f}")
print(f"Variance: {np.var(satisfaction_scores):.2f}")
print(f"Min Score: {min(satisfaction_scores)} (Q1)")
print(f"Max Score: {max(satisfaction_scores)} (Q3)")
print(f"Range: {max(satisfaction_scores) - min(satisfaction_scores):.2f}")

# Trend Analysis
print("\n" + "=" * 60)
print("TREND ANALYSIS")
print("=" * 60)

q1_to_q2_change = satisfaction_scores[1] - satisfaction_scores[0]
q2_to_q3_change = satisfaction_scores[2] - satisfaction_scores[1]
q3_to_q4_change = satisfaction_scores[3] - satisfaction_scores[2]

print(f"Q1 to Q2 Change: {q1_to_q2_change:+.2f}")
print(f"Q2 to Q3 Change: {q2_to_q3_change:+.2f}")
print(f"Q3 to Q4 Change: {q3_to_q4_change:+.2f}")

# Key Findings
print("\n" + "=" * 60)
print("KEY FINDINGS")
print("=" * 60)
print("1. High Volatility: Scores range from -2.83 to 6.7")
print("2. Below Target: Average of 1.68 is 2.82 points below target")
print("3. Inconsistent Performance: Large swings between quarters")
print("4. Q3 Success: Q3 exceeded target, indicating potential solutions")
print("5. Q1 Crisis: Negative score suggests critical service issues")

# Recommendations
print("\n" + "=" * 60)
print("RECOMMENDATIONS")
print("=" * 60)
print("PRIMARY SOLUTION: Improve service quality and wait times")
print("\nSpecific Actions:")
print("1. Implement Q3 best practices across all quarters")
print("2. Reduce wait times through better staff scheduling")
print("3. Enhance service quality training programs")
print("4. Monitor satisfaction metrics in real-time")
print("5. Address root causes of Q1 negative performance")

print("\n" + "=" * 60)
print("Analysis completed by: 22f3001098@ds.study.iitm.ac.in")
print("=" * 60)
