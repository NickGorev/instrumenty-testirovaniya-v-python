from morse import decode
import pytest


@pytest.mark.parametrize(
    "source_string, result",
    [
        ('.-', 'A'),
        ('-.-. --.-', 'CQ'),
        ('... --- ...', 'SOS'),
        ('... -- ...', 'SMS'),
        ('.- ...- .. - ---', 'AVITO'),
        ('--... ...--', '73'),
    ],
)
def test_morse_decode(source_string: str, result: str):
    """Parametric test of function decode"""
    assert decode(source_string) == result


@pytest.mark.parametrize(
    "source_string, err_type",
    [
        ('---------', KeyError),
        (';', KeyError),
        (0, AttributeError),
        (None, AttributeError)
    ],
)
def test_morse_decode_exceptions(source_string: str, err_type: type):
    """Parametric test of exceptions raising"""
    with pytest.raises(err_type):
        decode(source_string)
