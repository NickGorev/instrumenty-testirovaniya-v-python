from what_is_year_now import what_is_year_now
from unittest.mock import patch
import pytest
from io import StringIO


@pytest.mark.parametrize(
    "source_date, result",
    [
        ('2019-03-01', 2019),
        ('1917-09-25', 1917),
        ('0825-03-30', 825),
        ('0001-01-01', 1),
        ('01.03.2020', 2020),
        ('05.22.1974', 1974),
        ('01.11.532', 532),
        ('02.10.68', 68),
        ('99.99.2022', 2022),
    ],
)
def test_get_cases_parameric(source_date, result):
    """
    Parametric test of function decode
    date formats: YYYY-MM-DD, DD.MM.YYYY
    """
    with patch("what_is_year_now.urllib.request.urlopen") as mock_urlopen:
        json_str = f'{{"currentDateTime": "{source_date}"}}'
        mock_urlopen.return_value = StringIO(json_str)
        assert what_is_year_now() == result


@pytest.mark.parametrize(
    "source_date",
    [
        ('2019/03/01'),
        ('01/03/2020'),
        ('01-03-2020'),
        ('2019.03.01'),
        ('17-03-95'),
        ('aaaaaaaaa'),
        ('01-II-ABCD'),
        ('532-11-01'),
        ('68-10-02')
    ],
)
def test_get_cases_exception(source_date):
    """unknown date format"""
    with patch("what_is_year_now.urllib.request.urlopen") as mock_urlopen:
        json_str = f'{{"currentDateTime": "{source_date}"}}'
        mock_urlopen.return_value = StringIO(json_str)

        with pytest.raises(ValueError) as err:
            what_is_year_now()
        assert err.value.args[0] == 'Invalid format'
