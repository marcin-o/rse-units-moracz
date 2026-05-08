import pytest

from rse_units_moracz import air_density, ureg


def test_air_density_units():
    rho = air_density(300 * ureg.kelvin, 1000 * ureg.hectopascal)

    assert rho.check("[mass] / [length] ** 3")


def test_air_density_value():
    rho = air_density(300 * ureg.kelvin, 1000 * ureg.hectopascal)

    assert rho.magnitude == pytest.approx(1.161, rel=1e-3)