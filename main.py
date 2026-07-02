# main.py
from data.generate_dataset import generate_sales_data
from src.loader import load_sales
from src.reporter import print_summary
import numpy as np

def main():
    # Step 1: Generate (first run only) or load from disk
    sales, branch_names = generate_sales_data(seed=42)
    np.save("S:\Jason\Python libraries\Retail Store Performance analyser\data\sales_data.npy", sales)

    # Step 2: Load with validation
    sales = load_sales("S:\Jason\Python libraries\Retail Store Performance analyser\data\sales_data.npy")

    # Step 3: Generate and print report
    print_summary(sales, branch_names)

if __name__ == "__main__":
    main()