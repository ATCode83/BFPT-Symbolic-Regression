# BFPT Half-Life Symbolic Regression

This repository demonstrates how the **Banach Fixed Point Theorem (BFPT)** can be used in **symbolic regression** to derive the **general half-life formula** for particle decay using Python. Traditionally, differential equations serve as the foundation for modeling physical phenomena, but this novel approach highlights how metric spaces and contraction mappings can be leveraged as a complementary tool in mathematical modelling.

## 🔹 Origins of the Discovery
The inspiration for applying BFPT to derive new symbolic regression formulas emerged from email exchanges with Dr. Rainer Weiss, co-founder of LIGO. The core method presented was used to find a general half-life formula for particle decay and Dr. Weiss thought it novel enough for further exploration. This repository is an outgrowth of those conversations.

## 🔹 Overview of This Project
- Uses **complete metric spaces** and **contraction mappings** instead of differential equations.
- Applies **BFPT** to automatically find a **closed-form formula**.
- Derives the **general half-life formula** from first principles.
- Demonstrates the **convergence of the fixed-point iteration** to the classical decay formula.

## 📂 Project Structure
```
📦 BFPT-HalfLife-SymbolicRegression
├── 📄 README.md          # Explanation & Instructions
├── 📂 data               # Example CSV datasets
│   ├── exponential_decay.csv
├── 📂 src                # Python script for deriving formulas
│   ├── bfpt_half_life.py
├── 📄 LICENSE            # Open-source license
```

## ⚡ How It Works
### **Step-by-Step Method**
1️⃣ **Define a Metric Space:** Represent data as points in a complete metric space with a well-defined distance function.

2️⃣ **Identify a Contraction Mapping:** Explore potential mappings that satisfy the contraction property.

3️⃣ **Verify Contraction Condition:** Ensure the mapping meets the contraction criteria, guaranteeing convergence.

4️⃣ **Apply Banach Fixed Point Theorem:** Iterate the contraction mapping until a stable solution is reached.

5️⃣ **Derive a Closed-Form Formula:** Express the fixed point as a symbolic equation to reveal the general law.

### **Running the Script**
1️⃣ **Clone the repository**:
```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/BFPT-HalfLife-SymbolicRegression.git
```
2️⃣ **Run the script**:
```sh
python src/bfpt_half_life.py
```
3️⃣ **Enter the CSV file path and column names when prompted**.

## 📊 Example Output
```
📌 General Exponential Decay Formula: P(t) = P0 * α^(t / β)
📌 General Half-Life Formula: t_1/2 = (ln(2) / ln(1/α)) * β
```

## 🔭 Future Investigations
This project is just the beginning. Future updates will explore:
- Discovering **new formulas for physical phenomena** using BFPT.
- Investigating **thermodynamic laws and energy dissipation** using contraction mappings.
- Applying BFPT-based symbolic regression to **general relativity and quantum mechanics**.
- Comparing BFPT-based methods with traditional **differential equation approaches**.

## 🏆 Acknowledgments
A special thanks to **Dr. Rainer Weiss**, co-founder of **LIGO**, for his invaluable guidance, insightful discussions, and encouragement in exploring this novel approach to deriving closed-form formulas in physics.

Additionally, some of the Python code in this repository was generated using **Generative AI**, further demonstrating how computational tools can assist in automating symbolic regression and formula discovery.

## 📝 License
This project is licensed under the **MIT License**.

---
🚀 **This repository showcases a revolutionary method for deriving closed-form formulas in physics. Stay tuned for updates!** 🔥

