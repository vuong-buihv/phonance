def nir(real_risk_free_rate: float, expected_inflation_rate: float) -> float:
    """
    Calculate the nominal interest rate using the Fisher equation (approximate form).

    Parameters:
        real_risk_free_rate (float): The real interest rate (excluding inflation).
        expected_inflation_rate (float): The expected rate of inflation.

    Returns:
        float: The nominal interest rate.
    """
    return real_risk_free_rate + expected_inflation_rate
