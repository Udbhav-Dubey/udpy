import numpy as np
from scipy import stats

# Example data
# Suppose we have heights of mice in a control group and a treatment group
control_group = [5.1, 5.5, 5.3, 5.0, 5.2]
treatment_group = [5.8, 6.0, 6.1, 5.9, 6.2]

# Calculate means
mean_control = np.mean(control_group)
mean_treatment = np.mean(treatment_group)

print(f"Control mean: {mean_control:.2f}")
print(f"Treatment mean: {mean_treatment:.2f}")

# Perform independent t-test (assumes equal variances by default)
t_stat, p_value = stats.ttest_ind(control_group, treatment_group)

print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")

# Interpret result
alpha = 0.05
if p_value < alpha:
    print("✅ The difference is statistically significant.")
else:
    print("❌ No significant difference.")

