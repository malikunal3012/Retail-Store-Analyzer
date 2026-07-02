import numpy as np

# --- Generate data .py  ---
np.random.seed(32)


bandra_sales = np.random.randint(45000, 60000, 30)
print("Bandra first 5 days:", bandra_sales[:5])

# --- The Scaling Up Moment ---
# Instead of doing this 8 times, let's establish our branches
BRANCH_NAMES = ["Andheri", "Bandra", "Dadar", "Juhu", "Kurla", "Malad", "Thane", "Worli"]
print(f"Targeting {len(BRANCH_NAMES)} branches simultaneously over 30 days.")

np.random.seed(42)

# Base daily average revenue for our 8 Mumbai branches (1D Array)
# Shape: (8,)
baselines = np.array([45000, 62000, 38000, 71000, 55000, 29000, 67000, 41000])
#baselines = np.random.randint(28000,75000,size = 8)
#print(baselines)
# Generate 30 days of random variance noise (+/- 15%) for all 8 branches
# Shape: (30, 8) -> Rows = Days, Columns = Branches
noise = np.random.normal(loc=1.0, scale=0.15, size=(30, 8))

# BROADCASTING: (30, 8) multiplied by (8,) stretch-matches columns automatically
sales = baselines * noise

# Let's inject 3 realistic store emergencies (low sales events) using coordinates
sales[7, 2]  *= 0.20   # Day 8, Dadar: 
sales[14, 5] *= 0.10   # Day 15, Malad: 
sales[22, 0] *= 0.30   # Day 23, Andheri: 

# Clean up values to two decimal places
sales = np.round(sales, 2)
print("Matrix Generation Complete! Shape:", sales.shape)

# Numpy analysis.py ---- 

print("=== NUMPY MATRIX AUDIT ===")
print(f"Data Object Type : {type(sales)}")
print(f"Matrix Dimension : {sales.ndim}D Array")
print(f"Matrix Shape     : {sales.shape} (30 Rows/Days, 8 Columns/Branches)")
print(f"Total Data Points: {sales.size} individual sales figures")
print(f"Data Element Type: {sales.dtype}")
print(f"Memory Allocated : {sales.nbytes / 1024:.2f} KB\n")

print("First 3 days of sales data across all branches:\n", sales[:3])



print("=== BRANCH PERFORMANCE ANALYSIS (axis=0) ===")
# Data analysis ---
# Compute aggregate statistics down the columns
totals     = np.sum(sales, axis=0)
daily_avg  = np.mean(sales, axis=0)
daily_max  = np.max(sales, axis=0)

# Format and print results directly using plain Python formatting
header = f"{'Branch':<10} | {'Total Revenue':>14} | {'Daily Avg':>12} | {'Max Day':>10}"
print(header)
print("-" * len(header))

for i, name in enumerate(BRANCH_NAMES):
    print(f"{name:<10} | Rs {totals[i]:>12,.0f} | Rs {daily_avg[i]:>10,.0f} | Rs {daily_max[i]:>8,.0f}")

# Point out index positions of top performers
print("\n" + "="*40)
print(f"🏆 Top Branch   : {BRANCH_NAMES[np.argmax(totals)]} (Rs {totals.max():,.0f})")
print(f"⚠️ Lowest Branch : {BRANCH_NAMES[np.argmin(totals)]} (Rs {totals.min():,.0f})")
print("="*40)


print("\n=== TOTAL DAILY WALLET SHARE (axis=1) ===")

daily_corporate_totals = np.sum(sales, axis=1)

# Display first 5 days out of the 30 days
for day in range(5):
    print(f"Day {day+1}: Total Network Revenue = Rs {daily_corporate_totals[day]:,.0f}")

best_day_idx = np.argmax(daily_corporate_totals)
print(f"\n🚀 Best Network Day: Day {best_day_idx + 1} with Rs {daily_corporate_totals[best_day_idx]:,.0f}")



print("\n=== ANOMALY DETECTION WITH BOOLEAN MASKING ===")

# Create a customized low-performance threshold for each branch
# Anomaly = Day's sales are below 40% of that specific branch's monthly average
branch_averages = np.mean(sales, axis=0)
thresholds = branch_averages * 0.40

# Generate a Boolean Mask matrix of True/False values via broadcasting
anomaly_mask = sales < thresholds

# Extract exact coordinate arrays where condition is true
bad_days, bad_branches = np.where(anomaly_mask)

print(f"{'Date':<8} | {'Branch Name':<12} | {'Flagged Sales':>14} | {'Target Guardrail':>14}")
print("-" * 55)
for d, b in zip(bad_days, bad_branches):
    print(f"Day {d+1:<4} | {BRANCH_NAMES[b]:<12} | Rs {sales[d, b]:>12,.0f} | Rs {thresholds[b]:>12,.0f}")