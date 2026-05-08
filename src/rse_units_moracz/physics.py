import pint

ureg = pint.UnitRegistry()


def air_density(temperature, pressure):
    """
    Calculate air density using the ideal gas law.

    Parameters
    ----------
    temperature
        Temperature with units, e.g. 300 * ureg.kelvin.
    pressure
        Pressure with units, e.g. 1000 * ureg.hectopascal.

    Returns
    -------
    pint.Quantity
        Air density in base SI units.
    """
    r_air = 287 * ureg.joule / ureg.kelvin / ureg.kilogram
    return (pressure / (r_air * temperature)).to_base_units()