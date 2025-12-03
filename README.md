# Healthcare Patient Satisfaction Analysis

**Email:** 22f3001098@ds.study.iitm.ac.in  
**Objective:** Analyze quarterly patient satisfaction scores and compare them with the industry benchmark of **4.5**.

---

## 📊 Quarterly Scores
| Quarter | Score |
|--------|-------|
| Q1     | -2.83 |
| Q2     | -0.02 |
| Q3     | 6.70 |
| Q4     | 2.85 |

**Average Score:** 1.68  
**Industry Target:** 4.5

---

## 🔍 Key Findings

1. **Significant volatility** exists across quarters, with scores ranging from -2.83 to 6.7.  
2. **Q1 and Q2 performed poorly**, with negative or near-zero satisfaction scores.  
3. **Q3 shows strong performance**, reaching 6.7 — above the industry target.  
4. **Q4 dropped again**, indicating inconsistency in patient experience delivery.  
5. The **overall average score (1.68) is far below the target of 4.5**, signaling systemic issues.

---

## 💼 Business Implications

- **Patient dissatisfaction may lead to loss of trust**, reduced repeat visits, and negative hospital reputation.
- Falling below the industry standard can negatively impact:
  - Accreditation renewal
  - Insurance partnerships
  - Government quality ratings  
- The inconsistency in scores suggests **operational instability**, likely affecting workforce productivity.

---

## 🎯 Recommendations to Reach the 4.5 Target

### **1. Improve Service Quality (Primary Recommendation)**  
- Conduct service quality audits  
- Offer empathy & service training for staff  
- Implement patient-first customer service protocols  

### **2. Reduce Patient Wait Times (Primary Recommendation)**
- Optimize appointment scheduling  
- Improve triage process  
- Increase staffing during peak hours  

### **3. Implement Real-Time Feedback Systems**
- Collect patient feedback directly at discharge  
- Use quick surveys to identify issues before they escalate  

### **4. Strengthen Process Standardization**
- Ensure all departments follow consistent care protocols  
- Monitor deviation through weekly dashboards  

### **5. Focus on Q1 & Q2 Pain Points**
- Identify root causes for poor early-year performance  
- Possibly staffing shortages, process resets, or seasonal overloads  

---

## 📈 Visualizations

### Line Chart & Bar Chart Generation (Matplotlib)

```python
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "Score": [-2.83, -0.02, 6.7, 2.85]
}

df = pd.DataFrame(data)

# Line chart
plt.figure(figsize=(8, 5))
plt.plot(df["Quarter"], df["Score"], marker='o')
plt.title("Patient Satisfaction Scores by Quarter")
plt.xlabel("Quarter")
plt.ylabel("Score")
plt.grid(True)
plt.show()

# Bar chart
plt.figure(figsize=(8, 5))
plt.bar(df["Quarter"], df["Score"])
plt.title("Patient Satisfaction Quarterly Comparison")
plt.xlabel("Quarter")
plt.ylabel("Score")
plt.show()
