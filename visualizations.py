import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
plt.plot(df["Quarter"], df["Score"], marker='o')
plt.title("Patient Satisfaction Scores by Quarter")
plt.xlabel("Quarter")
plt.ylabel("Score")
plt.grid(True)
plt.show()
