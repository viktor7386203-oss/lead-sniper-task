#!/usr/bin/env python3
"""
Основной скрипт для сбора компаний с CAT-системами
"""

import pandas as pd
import logging
from pathlib import Path
from datetime import datetime

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def main():
    """Основная функция скрипта"""
    print("=" * 60)
    print("Сборщик компаний с CAT-системами")
    print("=" * 60)
    
    # Пути к файлам
    base_dir = Path(__file__).parent.parent
    data_dir = base_dir / "data"
    data_dir.mkdir(exist_ok=True)
    
    output_path = data_dir / "companies.csv"
    
    # Загружаем данные (в реальном проекте здесь был бы сбор)
    logger.info("Загрузка данных о компаниях...")
    
    # В данном упрощенном примере просто проверяем существование файла
    if output_path.exists():
        df = pd.read_csv(output_path, encoding="utf-8")
        logger.info(f"Загружено {len(df)} компаний из {output_path}")
        
        # Показываем статистику
        print(f"
📊 Статистика:")
        print(f"  Всего компаний: {len(df)}")
        print(f"  Выручка: от {df['revenue'].min():,.0f} до {df['revenue'].max():,.0f} ₽")
        print(f"  Средняя выручка: {df['revenue'].mean():,.0f} ₽")
        
        # Показываем примеры
        print(f"
🏆 Примеры компаний:")
        for i, row in df.head(3).iterrows():
            print(f"  {row['name']} - {row['revenue']:,.0f} ₽")
            print(f"    CAT: {row.get('cat_product', 'не указано')}")
            print()
    else:
        logger.warning(f"Файл {output_path} не найден")
        print("Для запуска полного сбора используйте скрипты в notebooks/")
    
    print("=" * 60)
    print("Готово!")

if __name__ == "__main__":
    main()
