```
>>> python -m pytest -v tests/test_what_is_year_now.py --cov --cov-report html
===================================== test session starts =====================================
platform win32 -- Python 3.10.7, pytest-7.2.0, pluggy-1.0.0 -- C:\Users\Nick\Documents\AVITO\python\instrumenty-testirovaniya-v-python\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Nick\Documents\AVITO\python\instrumenty-testirovaniya-v-python
plugins: cov-4.0.0
collected 18 items

tests/test_what_is_year_now.py::test_get_cases_parameric[2019-03-01-2019] PASSED         [  5%]
tests/test_what_is_year_now.py::test_get_cases_parameric[1917-09-25-1917] PASSED         [ 11%]
tests/test_what_is_year_now.py::test_get_cases_parameric[0825-03-30-825] PASSED          [ 16%]
tests/test_what_is_year_now.py::test_get_cases_parameric[0001-01-01-1] PASSED            [ 22%]
tests/test_what_is_year_now.py::test_get_cases_parameric[01.03.2020-2020] PASSED         [ 27%]
tests/test_what_is_year_now.py::test_get_cases_parameric[05.22.1974-1974] PASSED         [ 33%]
tests/test_what_is_year_now.py::test_get_cases_parameric[01.11.532-532] PASSED           [ 38%]
tests/test_what_is_year_now.py::test_get_cases_parameric[02.10.68-68] PASSED             [ 44%]
tests/test_what_is_year_now.py::test_get_cases_parameric[99.99.2022-2022] PASSED         [ 50%]
tests/test_what_is_year_now.py::test_get_cases_exception[2019/03/01] PASSED              [ 55%] 
tests/test_what_is_year_now.py::test_get_cases_exception[01/03/2020] PASSED              [ 61%] 
tests/test_what_is_year_now.py::test_get_cases_exception[01-03-2020] PASSED              [ 66%] 
tests/test_what_is_year_now.py::test_get_cases_exception[2019.03.01] PASSED              [ 72%] 
tests/test_what_is_year_now.py::test_get_cases_exception[17-03-95] PASSED                [ 77%]
tests/test_what_is_year_now.py::test_get_cases_exception[aaaaaaaaa] PASSED               [ 83%] 
tests/test_what_is_year_now.py::test_get_cases_exception[01-II-ABCD] PASSED              [ 88%] 
tests/test_what_is_year_now.py::test_get_cases_exception[532-11-01] PASSED               [ 94%] 
tests/test_what_is_year_now.py::test_get_cases_exception[68-10-02] PASSED                [100%] 

---------- coverage: platform win32, python 3.10.7-final-0 -----------
Coverage HTML written to dir htmlcov


===================================== 18 passed in 0.24s ======================================
```