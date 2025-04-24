def nir_approx(real_risk_free_rate: float, expected_inflation_rate: float) -> float:
    """
    Calculate the nominal interest rate using the approximate Fisher equation.

    Approximate Formula:
        nominal_rate ≈ real_rate + expected_inflation_rate

    Parameters:
        real_risk_free_rate (float): The real risk-free interest rate (as a decimal).
        expected_inflation_rate (float): The expected rate of inflation (as a decimal).

    Returns:
        float: The nominal interest rate (approximate).
    """
    return real_risk_free_rate + expected_inflation_rate


def nir_exact(real_risk_free_rate: float, expected_inflation_rate: float) -> float:
    """
    Calculate the nominal interest rate using the exact Fisher equation.

    Exact Formula:
        nominal_rate = (1 + real_rate) * (1 + inflation_rate) - 1

    Parameters:
        real_risk_free_rate (float): The real risk-free interest rate (as a decimal).
        expected_inflation_rate (float): The expected rate of inflation (as a decimal).

    Returns:
        float: The nominal interest rate (exact).
    """
    return (1 + real_risk_free_rate) * (1 + expected_inflation_rate) - 1
