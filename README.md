# ДЗ инструменты тестирования в python

## issue-01
Тестирование функции `encode` из файла [morse.py](morse.py) с использованием `doctest`.

Тесты записаны в docstring тестируемой функции.

Для запуска тестов выполняется команда:
```commandline
python -m doctest -v -o NORMALIZE_WHITESPACE morse.py
```
Команда и результаты запуска скопированы в файл [results/result_1.md](results/result_1.md).

## issue-02
Тестирование функции `decode` из файла [morse.py](morse.py) с использованием `pytest.mark.parametrize`.

Параметрические тесты находятся в файле [tests/test_decode.py](tests/test_decode.py).

Для запуска тестов выполняется команда:
```commandline
python -m pytest -v tests/test_decode.py
```
Команда и результаты запуска скопированы в файл [results/result_2.md](results/result_2.md)

## issue-03
Тестирование функции `fit_transform` из файла [one_hot_encoder.py](one_hot_encoder.py) с использованием `unittest`.

Тесты находятся в файле [tests/test_fit_transform_unittest.py](tests/test_fit_transform_unittest.py).

Для запуска тестов выполняется команда:
```commandline
python -m unittest -v tests/test_fit_transform_unittest.py
```
Команда и результаты запуска скопированы в файл [results/result_3.md](results/result_3.md)

## issue-04
Тестирование функции `fit_transform` из файла [one_hot_encoder.py](one_hot_encoder.py) с использованием `pytest`.

Тесты находятся в файле [tests/test_fit_transform_pytest.py](tests/test_fit_transform_pytest.py).

Для запуска тестов выполняется команда:
```commandline
python -m pytest -v tests/test_fit_transform_pytest.py
```
Команда и результаты запуска скопированы в файл [results/result_4.md](results/result_4.md)
## issue-05
Тестирование функции `what_is_year_now` из файла [what_is_year_now.py](what_is_year_now.py).
Эта функция получает текущее время из API-worldclock и извлекает из поля 'currentDateTime' год.

Тесты находятся в файле [tests/test_what_is_year_now.py](tests/test_what_is_year_now.py). В тестах используется `unittest.mock` для замены реального обращения к API.

Для запуска тестов с одновременным созданием html отчёта о покрытии выполняется команда:
```commandline
python -m pytest -v tests/test_what_is_year_now.py --cov --cov-report html
```
Команда и результаты запуска скопированы в файл [results/result_5.md](results/result_5.md)

Отчёт о покрытии содержится в директории [htmlcov](htmlcov) в файле [htmlcov/what_is_year_now_py.html](https://htmlpreview.github.io/?https://github.com/NickGorev/instrumenty-testirovaniya-v-python/blob/my-tests/htmlcov/what_is_year_now_py.html).

Из отчёта видно, что тесты покрывают 100% кода.

