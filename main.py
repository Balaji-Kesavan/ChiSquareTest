"""
Main script for Titanic Analysis Project
"""

import os
from src.data_loader import load_titanic_data, get_data_info
from src.eda import chi_square_analysis, plot_survival_by_gender

def main():
    # Define paths
    data_path = os.path.join("data", "titanic.csv")
    figures_path = os.path.join("reports", "figures")
    
    # Load data
    print("Loading Titanic dataset...")
    df = load_titanic_data(data_path)
    
    # Display data info
    print("\nDataset Information:")
    info = get_data_info(df)
    print(f"Shape: {info['shape']}")
    print(f"Columns: {info['columns']}")
    
    # Chi-Square Analysis
    print("\n" + "="*50)
    print("CHI-SQUARE TEST: Gender vs Survival")
    print("="*50)
    results = chi_square_analysis(df)
    
    # Create visualizations
    print("\nGenerating visualizations...")
    plot_filepath = os.path.join(figures_path, "survival_by_gender.png")
    plot_survival_by_gender(df, filepath=plot_filepath)
    
    print(f"\nFigure saved to: {plot_filepath}")
    print("Analysis complete!")

if __name__ == "__main__":
    main()
