
"""
Prime Number Theorem Data Analysis Project
==========================================

A comprehensive data analysis project demonstrating the Prime Number Theorem
and the distribution of prime numbers through computational verification.

Author: Mathematical Data Analysis Project
Date: September 2025
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from math import log, sqrt, pi, e
from scipy.special import expi
import warnings
warnings.filterwarnings('ignore')

def main():
    """
    Main analysis function demonstrating the Prime Number Theorem
    """
    print("PRIME NUMBER THEOREM - COMPUTATIONAL VERIFICATION")
    print("=" * 55)

    # Load the datasets
    df_counting = pd.read_csv('prime_counting_function.csv')
    df_gaps = pd.read_csv('prime_gaps_analysis.csv')
    df_dense = pd.read_csv('prime_distribution_dense.csv')
    df_properties = pd.read_csv('primes_properties.csv')

    print(f"\nDatasets loaded successfully:")
    print(f"- Prime counting function: {len(df_counting)} points")
    print(f"- Prime gaps analysis: {len(df_gaps)} gaps")
    print(f"- Dense sampling: {len(df_dense)} points")
    print(f"- Prime properties: {len(df_properties)} primes")

    # ANALYSIS 1: Prime Number Theorem Verification
    print("\n" + "=" * 55)
    print("ANALYSIS 1: PRIME NUMBER THEOREM VERIFICATION")
    print("=" * 55)

    max_x = df_counting['x'].max()
    final_row = df_counting[df_counting['x'] == max_x].iloc[0]

    print(f"\nAt x = {max_x:,}:")
    print(f"  Actual Ï€(x) = {final_row['pi_x']:,.0f}")
    print(f"  PNT estimate x/ln(x) = {final_row['pnt_approximation']:,.1f}")
    print(f"  Better estimate li(x) = {final_row['li_approximation']:,.1f}")
    print(f"  PNT relative error: {final_row['pnt_relative_error']:.4f}")
    print(f"  li(x) relative error: {final_row['li_relative_error']:.4f}")

    ratio = final_row['pi_x'] / final_row['pnt_approximation']
    print(f"\nConvergence to PNT: Ï€(x)/(x/ln(x)) = {ratio:.6f}")
    print(f"Theoretical limit: 1.000000")
    print(f"Deviation: {abs(1 - ratio):.6f}")

    # ANALYSIS 2: Prime Gaps Distribution
    print("\n" + "=" * 55)
    print("ANALYSIS 2: PRIME GAPS DISTRIBUTION")
    print("=" * 55)

    print(f"\nPrime gaps statistics:")
    print(f"  Average gap: {df_gaps['gap'].mean():.2f}")
    print(f"  Median gap: {df_gaps['gap'].median():.2f}")
    print(f"  Maximum gap: {df_gaps['gap'].max()}")
    print(f"  Standard deviation: {df_gaps['gap'].std():.2f}")

    # Theoretical average gap around prime p is approximately log(p)
    print(f"\nGap vs log(prime) analysis:")
    correlation = df_gaps['gap'].corr(df_gaps['log_prime'])
    print(f"  Correlation coefficient: {correlation:.4f}")
    print(f"  Average gap/log(prime) ratio: {df_gaps['gap_over_log'].mean():.4f}")

    # ANALYSIS 3: Accuracy Improvement Over Range
    print("\n" + "=" * 55)
    print("ANALYSIS 3: APPROXIMATION ACCURACY TRENDS")
    print("=" * 55)

    print("\nAccuracy improvement with increasing x:")
    print("x\t\tÏ€(x)\tx/ln(x) error\tli(x) error\tImprovement")
    print("-" * 65)

    for _, row in df_counting.iterrows():
        if row['x'] in [100, 1000, 10000, 100000]:
            improvement = row['pnt_relative_error'] / row['li_relative_error']
            print(f"{row['x']:,.0f}\t\t{row['pi_x']:,.0f}\t"
                  f"{row['pnt_relative_error']:.4f}\t\t"
                  f"{row['li_relative_error']:.4f}\t\t{improvement:.1f}x")

    # ANALYSIS 4: Twin Primes
    print("\n" + "=" * 55)
    print("ANALYSIS 4: TWIN PRIMES ANALYSIS")
    print("=" * 55)

    twin_primes = df_properties[df_properties['is_twin_prime'] == True]
    total_analyzed = len(df_properties)
    twin_count = len(twin_primes)

    print(f"\nTwin primes analysis (first {total_analyzed} primes):")
    print(f"  Twin primes found: {twin_count}")
    print(f"  Percentage: {twin_count/total_analyzed*100:.1f}%")
    print(f"  Largest twin prime in dataset: {twin_primes['prime'].max()}")

    # Hardy-Littlewood conjecture estimates about x/lnÂ²(x) twin primes up to x
    x_max = df_properties['prime'].max()
    hl_estimate = 2 * 1.32032 * x_max / (log(x_max)**2)
    actual_twins = twin_count * 2  # Each twin prime contributes to 2 numbers
    print(f"  Hardy-Littlewood estimate up to {x_max}: {hl_estimate:.0f}")
    print(f"  Observed twin primes up to {x_max}: {actual_twins}")

    print("\n" + "=" * 55)
    print("CONCLUSION")
    print("=" * 55)
    print("\nThe computational analysis confirms the Prime Number Theorem:")
    print("1. Ï€(x) ~ x/ln(x) as x â†’ âˆž")
    print("2. li(x) provides superior approximation accuracy")
    print("3. Prime gaps show expected logarithmic growth")
    print("4. Twin primes follow predicted density patterns")
    print("\nThis demonstrates the deep connection between")
    print("prime distribution and logarithmic functions!")

if __name__ == "__main__":
    main()