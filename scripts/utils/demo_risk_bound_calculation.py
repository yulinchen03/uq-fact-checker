import scipy.stats as stats
import numpy as np

def verify_risk_bound(m_accepted: int, k_errors: int, delta: float = 0.05):
    """
    Verifies that the Beta PPF method perfectly solves the Binomial CDF 
    equation from Lemma 3.1 (Geifman & El-Yaniv, 2017).
    """
    # 1. The Inverse Problem (Our Script's Approach)
    # Solve for b* (The Guaranteed Maximum Risk)
    b_star = stats.beta.ppf(1 - delta, k_errors + 1, m_accepted - k_errors)
    
    # 2. The Forward Problem (The Verification)
    # If b* is correct, plugging it into the standard Binomial CDF should 
    # perfectly reconstruct our target delta (0.001).
    calculated_delta = stats.binom.cdf(k_errors, m_accepted, b_star)
    
    # 3. Print Results
    empirical_error = k_errors / m_accepted if m_accepted > 0 else 0
    print(f"--- Testing Scenario: {m_accepted} accepted, {k_errors} errors ---")
    print(f"Empirical Error:      {empirical_error:.4f} ({empirical_error*100:.2f}%)")
    print(f"Guaranteed Risk (b*): {b_star:.4f} ({b_star*100:.2f}%)")
    
    # We use scientific notation here to show the exact floating-point precision
    print(f"Target Delta:         {delta:.6e}")
    print(f"Calculated Delta:     {calculated_delta:.6e}")
    
    # Check if they mathematically match (accounting for standard floating-point drift)
    is_match = np.isclose(calculated_delta, delta, rtol=1e-5)
    print(f"Proof Successful:     {'✅ YES' if is_match else '❌ NO'}\n")

if __name__ == "__main__":
    print("Verifying Geifman & El-Yaniv Lemma 3.1 Math...\n")
    
    # Test Case 1: Standard realistic RAG scenario
    verify_risk_bound(m_accepted=1000, k_errors=40)
    
    # Test Case 2: Small dataset, zero errors (Edge case)
    verify_risk_bound(m_accepted=100, k_errors=0)
    
    # Test Case 3: Very small dataset, high empirical error
    verify_risk_bound(m_accepted=90, k_errors=45)
    
    # Test Case 4: Massive dataset (Proving scale doesn't break it)
    verify_risk_bound(m_accepted=50000, k_errors=1200)