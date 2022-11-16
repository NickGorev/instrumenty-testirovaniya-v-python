```
>>> python -m pytest -v tests/test_decode.py
=================================== test session starts ===================================
platform win32 -- Python 3.10.7, pytest-7.2.0, pluggy-1.0.0 -- C:\Users\Nick\Documents\AVITO\python\instrumenty-testirovaniya-v-python\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Nick\Documents\AVITO\python\instrumenty-testirovaniya-v-python
plugins: cov-4.0.0
collected 10 items                                                                          

tests/test_decode.py::test_morse_decode[.--A] PASSED                                 [ 10%] 
tests/test_decode.py::test_morse_decode[-.-. --.--CQ] PASSED                         [ 20%] 
tests/test_decode.py::test_morse_decode[... --- ...-SOS] PASSED                      [ 30%] 
tests/test_decode.py::test_morse_decode[... -- ...-SMS] PASSED                       [ 40%]
tests/test_decode.py::test_morse_decode[.- ...- .. - ----AVITO] PASSED               [ 50%]
tests/test_decode.py::test_morse_decode[--... ...---73] PASSED                       [ 60%]
tests/test_decode.py::test_morse_decode_exceptions[----------KeyError] PASSED        [ 70%]
tests/test_decode.py::test_morse_decode_exceptions[;-KeyError] PASSED                [ 80%]
tests/test_decode.py::test_morse_decode_exceptions[0-AttributeError] PASSED          [ 90%]
tests/test_decode.py::test_morse_decode_exceptions[None-AttributeError] PASSED       [100%]

=================================== 10 passed in 0.05s ====================================
```