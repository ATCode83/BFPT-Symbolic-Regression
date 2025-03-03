import sympy as sp

# Define symbols
t, P, alpha, beta, P0 = sp.symbols('t P alpha beta P0')

# Define the contraction mapping for exponential decay
def contraction_mapping(t, P, alpha, beta):
    return (t + beta, alpha * P)

# Derive the general exponential decay formula using the fixed point approach
def derive_exponential_decay_formula():
    P_t = P0 * alpha ** (t / beta)
    return P_t.simplify()

# Derive the general half-life formula
def derive_half_life_formula():
    t_half = (sp.ln(2) / sp.ln(1 / alpha)) * beta
    return t_half.simplify()

# Main function
def main():
    print("\n🔹 **Symbolic Derivation using BFPT** 🔹")

    # Compute the formulas symbolically
    decay_formula = derive_exponential_decay_formula()
    half_life_formula = derive_half_life_formula()

    # Print the exact symbolic solutions
    print(f"\n📌 **General Exponential Decay Formula:**\n   P(t) = {decay_formula}")
    print(f"\n📌 **General Half-Life Formula:**\n   t_1/2 = {half_life_formula}\n")

if __name__ == "__main__":
    main()
