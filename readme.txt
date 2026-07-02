What This Project Does
This project simulates a real-world retail analytics pipeline. It demonstrates how data moves from raw generation, through Excel (so non-technical stakeholders can see it), and back into Python for deep NumPy-powered analysis.

Phase	What Happens	Key Python Used
1  Generate	Create 30-day synthetic sales for 8 store branches	np.random.normal()
2  Export	Save the NumPy array to a readable Excel workbook	pd.ExcelWriter()
3  Load	Read Excel back into Python as a NumPy ndarray	pd.read_excel()
4  Inspect	Print array shape, dtype, memory usage	.shape  .dtype  .ndim
5  Analyse	Compute KPIs using axis operations and ufuncs	np.sum / mean / std
6  Detect	Flag anomaly days using Boolean Masking	np.where()
7  Report	Print formatted console report + save summary sheet	pd.ExcelWriter()

Who This Is For
•	Python students who have completed NumPy fundamentals (Days 1–5)
•	Analysts who want to see how NumPy connects to real business workflows
•	Instructors who need a complete, runnable teaching project

Tech Stack & Installation
# Install all dependencies in one command
pip install numpy pandas openpyxl

# Verify installations
python -c "import numpy, pandas, openpyxl; print('All good!')"

Library	Version	Purpose
numpy	1.24+	2D array storage, axis ops, ufuncs, boolean masking
pandas	2.0+	Excel I/O bridge — read_excel() and ExcelWriter
openpyxl	3.1+	Engine behind pandas Excel writing, required dependency

How to Run
# Step 1: Clone or create the project folder
mkdir retail-performance-analyzer
cd    retail-performance-analyzer

# Step 2: Create the data folder (script writes here)
mkdir data

# Step 3: Run the procedural version
python main.py

# Step 4: Run the OOP version
python oop_main.py

# Step 5: Open the Excel output
# data/sales_report.xlsx  ->  open in Microsoft Excel or LibreOffice Calc

Expected Output
Console Output (what you see when main.py runs)
>>> PHASE 1: Generating dataset and saving to Excel
Excel file saved:  data/sales_report.xlsx
  Sheet 1: Daily Sales   (30 days x 8 branches)
  Sheet 2: Summary Stats (KPIs per branch)

>>> PHASE 2: Loading from Excel into NumPy
Loaded: 30 rows x 8 columns

>>> PHASE 3: Array Inspection
  Shape      : (30, 8)
  Dimensions : 2D array
  Data type  : float64
  Memory     : 1.88 KB

>>> PHASE 4: Branch Analysis
  Best branch  :  Juhu   (Rs 2,104,870)
  Needs attention:  Malad  (Rs 847,000)

>>> PHASE 5: Anomaly Detection
  Day 8   Dadar    Rs  7,523   Threshold: Rs 19,000

Excel Output (what students open in Excel)
Sheet 1 — Daily Sales: 30 rows x 8 columns, one cell per (day, branch) revenue figure. Students can see the raw data and manually verify any calculation the code produces.
Sheet 2 — Summary Stats: One row per branch with Total Revenue, Daily Average, Std Deviation, Min, Max, and Volatility %. Students can recreate these figures with Excel formulas as a cross-check.

Key Learning Concepts
Concept	Where It Appears	Line(s) to Study
NumPy 2D array creation	generate_sales_data()	baselines * noise
Broadcasting	generate_sales_data()	shape (30,8) * (8,)
axis=0 vs axis=1	analyse_by_branch() / by_day()	np.sum(arr, axis=0)
Boolean masking	flag_bad_days()	arr < threshold
ufuncs (log, sqrt, where)	apply_ufuncs()	np.log / np.where
Excel I/O round-trip	save / load functions	df.values  ->  ndarray
OOP encapsulation	oop_main.py	class SalesAnalyzer

 
Execution Flow — Step by Step
This diagram shows every step taken when you run main.py, in order. Each step maps to a specific function and a core Python/NumPy concept.
STEP
1	ENTRY POINT
python main.py executes
Python reads main.py top to bottom. It hits the if __name__ == '__main__' block and begins calling functions in sequence. No code outside this block runs automatically.

STEP
2	DATA GENERATION
generate_sales_data() called
np.random.seed(42) locks the randomness. baselines array (shape 8,) is multiplied with noise (shape 30,8) using NumPy broadcasting. Three anomaly injections simulate real-world events.

STEP
3	EXCEL EXPORT
save_summary_to_excel() called
The NumPy array is wrapped in a Pandas DataFrame with branch names as column headers and 'Day 1...Day 30' as the index. pd.ExcelWriter writes two sheets: raw data and KPI summary.

STEP
4	EXCEL LOAD
load_from_excel() called
pd.read_excel() reads the file back. df.values strips headers and index, returning a clean NumPy ndarray of shape (30, 8). This round-trip proves the data survived Excel formatting intact.

STEP
5	ARRAY INSPECTION
inspect_array() called
Prints .shape, .ndim, .dtype, .size, .nbytes. Students see the array printed as a 2D grid. This is the teaching moment for array properties before any calculations run.

STEP
6	BRANCH ANALYSIS (AXIS=0)
analyse_by_branch() called
np.sum, np.mean, np.std, np.min, np.max all called with axis=0. This collapses the 30 rows into one value per branch column. Output shape (8,). argmax() finds the best branch index.

STEP
7	DAILY ANALYSIS (AXIS=1)
analyse_by_day() called
Same ufuncs called with axis=1. This collapses the 8 branch columns into one value per day row. Output shape (30,). Shows how changing axis flips the direction of aggregation.

STEP
8	ANOMALY DETECTION
flag_bad_days() called
np.mean(axis=0) calculates each branch's average. Multiplied by 0.5 gives the threshold. Boolean mask = arr < threshold produces a (30,8) True/False array. np.where() extracts the flagged positions.

STEP
9	UFUNC DEMOS
apply_ufuncs() called
np.log() compresses the revenue scale. np.sqrt() dampens outliers. np.where() labels each cell Good or Low without any Python loop. np.round() cleans display precision.

STEP
10	PROGRAM ENDS
Script completes, Excel file ready
All output is printed to console. data/sales_report.xlsx exists with both sheets populated. Students open it in Excel to cross-check every figure the script produced.

DATA FLOW DIAGRAM
How the data changes shape at each stage:

Stage	Data Form	Shape	Type
After generate_sales_data()	NumPy ndarray in memory	(30, 8)	float64
After save_to_excel()	Excel .xlsx file on disk	30 rows	openpyxl
After pd.read_excel()	Pandas DataFrame	(30, 8)	DataFrame
After df.values	NumPy ndarray again	(30, 8)	float64
After np.sum(axis=0)	1D array per-branch totals	(8,)	float64
After np.sum(axis=1)	1D array per-day totals	(30,)	float64
After boolean mask	True/False grid	(30, 8)	bool

 
