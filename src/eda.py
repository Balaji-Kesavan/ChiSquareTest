import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

def chi_square_analysis(df):
    """
    Perform Chi-Square test for independence between Gender and Survival.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Titanic dataset
    
    Returns:
    --------
    dict
        Chi-Square test results
    """
    # Create contingency table
    table = pd.crosstab(df['Sex'], df['Survived'])
    
    print("Contingency Table:\n", table)
    
    # Chi-Square Test
    chi2, p, dof, expected = chi2_contingency(table)
    
    print("\nChi-Square Value:", chi2)
    print("p-value:", p)
    print("Degrees of Freedom:", dof)
    
    # Interpretation
    if p < 0.05:
        result = "Reject H0 → Gender affects survival"
    else:
        result = "Accept H0 → Gender does not affect survival"
    
    print("Result:", result)
    
    return {
        'chi2': chi2,
        'p_value': p,
        'dof': dof,
        'expected': expected,
        'contingency_table': table,
        'interpretation': result
    }

def plot_survival_by_gender(df, filepath=None):
    """
    Create bar chart showing survival count by gender.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Titanic dataset
    filepath : str, optional
        Path to save the figure
    """
    table = pd.crosstab(df['Sex'], df['Survived'])
    table.plot(kind='bar', figsize=(8, 6))
    
    plt.title("Survival Count by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Count")
    plt.xticks(rotation=0)
    plt.legend(["Not Survived", "Survived"])
    
    plt.tight_layout()
    
    if filepath:
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
    
    plt.show()
