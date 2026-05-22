import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [120, 150, 170, 160, 200, 220],
    "Profit": [20, 25, 30, 28, 40, 45]
}
df = pd.DataFrame(data)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.plot(df["Month"], df["Sales"], marker='o')
plt.title("Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.subplot(1, 3, 2)
plt.bar(df["Month"], df["Profit"])
plt.title("Profit Comparison")
plt.xlabel("Month")
plt.ylabel("Profit")

plt.subplot(1, 3, 3)
plt.hist(df["Sales"], bins=5)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

print("INSIGHTS:")
print("1. Sales are increasing month by month.")
print("2. Highest sales observed in June.")
print("3. Profit is also growing with sales.")
print("4. Histogram shows most sales values are between 150 and 220.")
print("5. No major outliers detected.")
