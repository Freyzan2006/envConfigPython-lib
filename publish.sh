#!/bin/bash

# Очищаем старые сборки
echo "🧹 Чистим старые сборки..."
rm -rf build/ dist/ *.egg-info

# Собираем проект
echo "📦 Собираем проект..."
python3 -m build

# Публикуем на PyPI
echo "🚀 Публикуем на PyPI..."
python3 -m twine upload dist/*

echo "✅ Готово!"
