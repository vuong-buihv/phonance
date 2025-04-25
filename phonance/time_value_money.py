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


def required_interest_rate(
        nominal_risk_free_rate: float,
        default_risk_premium: float,
        liquidity_premium: float,
        maturity_risk_premium: float
) -> float:
    """
    Calculate the required interest rate on a security.

    Formula:
        required_rate = nominal_risk_free_rate + default_risk_premium
                        + liquidity_premium + maturity_risk_premium

    Parameters:
        nominal_risk_free_rate (float): The nominal risk-free interest rate (as a decimal).
        default_risk_premium (float): The premium for default risk (as a decimal).
        liquidity_premium (float): The premium for liquidity risk (as a decimal).
        maturity_risk_premium (float): The premium for maturity risk (as a decimal).

    Returns:
        float: The required interest rate on the security.

    Raises:
        ValueError: If any of the inputs are negative.
    """
    # Validate inputs
    if any(param < 0 for param in
           [nominal_risk_free_rate, default_risk_premium, liquidity_premium, maturity_risk_premium]):
        raise ValueError("All input parameters must be non-negative.")

    # Calculate the required interest rate
    return (
            nominal_risk_free_rate
            + default_risk_premium
            + liquidity_premium
            + maturity_risk_premium
    )
