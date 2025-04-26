## Как собировать проект для PIP:

1. version = "<Поставить новую версию>" в pyproject.toml
2. Удалить прошлую сборку (dict, env_config_lib)
3. python -m build
4. python -m twine upload dist/*

или

1. ./publish.sh


Все новая версия библеоткеки доступна в pip.

# Test:

1. Создать новый проект.
2. скачать pip install env-config-lib
3. Использовать в коде.